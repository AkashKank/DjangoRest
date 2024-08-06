from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import *
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
import pandas as pd
from .serializer import TopicSerializer, MessageSerializer
from io import BytesIO

# Create your views here
class TopicListCreateView(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticated]

#Working
class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            # Superuser broadcasting
            content = request.data.get('content', '')
            if not content:
                return Response({'error': 'content is required'}, status=status.HTTP_400_BAD_REQUEST)
            
            topics = Topic.objects.all()
            for topic in topics:
                Message.objects.create(topic=topic, user=request.user, content=content)
            
            return Response({'status': 'messages broadcasted'}, status=status.HTTP_201_CREATED)
        
        # Regular user can send a message to a specific topic
        return super().post(request, *args, **kwargs)
    

class ExportAPIView(APIView):
    def post(self, request):
        try:
            messages = Message.objects.all()
            df = pd.DataFrame.from_records(messages.values('topic','user','content'))
            df.columns = ['Topic', 'User', 'Message from user']
            df.to_excel('MessagesExportss.xlsx', index=False)
            return Response({
                'status': True,
                'message':'Messages exported Sucessfully'
            },status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                'status':False,
                'message':'We could not complete Export'
            }, status=status.HTTP_400_BAD_REQUEST)


# class ExportAPIView(APIView):
#     def post(self, request):
#         try:
#             messages = Message.objects.all()
#             df = pd.DataFrame.from_records(messages.values('topic','user','content'))
#             df.columns = ['Topic', 'User', 'Message from user']
#             df.to_excel('MessagesExport.xlsx', index=False)
#             return Response({
#                 'status': True,
#                 'message':'Messages exported Sucessfully'
#             },status=status.HTTP_200_OK)
        
#         except Exception as e:
#             return Response({
#                 'status':False,
#                 'message':'We could not complete Export'
#             }, status=status.HTTP_400_BAD_REQUEST)

# Testing  
# class NewMessageListCreateView(generics.ListCreateAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         topic_id = self.request.data.get('topic')
#         user = self.request.user
#         print(user)
#         topic_id = self.request.data.get('topic')

#         if user.is_superuser:
#             topics = Topic.objects.all()
#             print(topics)
#             for topic in topics:
#                 serializer.save(user=user, topic=topic)
#         else:
#             topic = Topic.objects.get(id=topic_id)
#             serializer.save(user=user, topic=topic)
