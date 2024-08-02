from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# Create your views here.
# User Registration class
from rest_framework_simplejwt.tokens import RefreshToken
class UserRegistration(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        serializer.save()

        user = User.objects.get(username = serializer.data['username'])
        # token_obj , _ = Token.objects.get_or_create(user=user)
        refresh = RefreshToken.for_user(user)

        return Response({'status':200, 'payload':serializer.data,
                        'refresh': str(refresh),
                        'access': str(refresh.access_token), 'message':"Token created sucessfully"})

class ConversationTopicListCreateView(generics.ListCreateAPIView):
    queryset = ConversationTopic.objects.all()
    serializer_class = ConversationTopicSerializer

class MessageCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    # def perform_create(self, serializer):
    #     user = self.request.user

    #     if user.is_superuser:
    #         # If user is superuser, pass message in each topic
    #         topics = ConversationTopic.objects.all()
    #         for topic in topics:
    #             serializer.save(sender=user, topic=topic)
    #     else:
    #         topic_id = self.request.data.get('conversation')
    #         topic = ConversationTopic.objects.get(id=topic_id)
    #         serializer.save(topic=topic, sender=user)
