from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import status
from .serializers import ImportSerializers, PaginationSerializers
from rest_framework.parsers import MultiPartParser, FormParser
import pandas as pd
from .mypagination import MyCursorPagination
from .models import Profile
from django.core.paginator import Paginator
# Create your views here.

class ImportAPIView(APIView):
    serializer_class = ImportSerializers
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        # try:
            data = request.FILES
            serializer=self.serializer_class(data=data)
            if not serializer.is_valid():
                return Response({'status':False, 'message':'provide a valid file'}, status=status.HTTP_400_BAD_REQUEST)
            excel_file = data.get('file')
            df = pd.read_excel(excel_file, sheet_name=0)
      
            #fill missing values
            df['name'] = df['name'].fillna(value='Unknown')
            df['mobile'] = df['mobile'].fillna(value='empty')


            profiles = []
            for index,row in df.iterrows():
                name = row['name']
                mobile = row['mobile']
                valu = Profile.objects.filter(name=name)
                if valu.exists():
                    continue
                else:
                    valu = Profile(
                        name = name,
                        mobile = mobile
                    )
                    profiles.append(valu)
                    
            print(profiles)
            print("##############")
            Profile.objects.bulk_create(profiles)
            return Response({'status':True, 'message':'File Imported sucessfully'}, status=status.HTTP_201_CREATED)

        # except Exception as e:
        #     return Response({'status':False, 'message':'We could not complete'}, status=status.HTTP_400_BAD_REQUEST)

class PaginationAPIView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = PaginationSerializers
    pagination_class = MyCursorPagination


              
