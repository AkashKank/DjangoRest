from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Country
from rest_framework import generics
from .serializer import CountrySerializer

# class MedalCountListCreateView(generics.ListCreateAPIView):
#     serializer_class = CountrySerializer
#     def get_queryset(self):
#         return Country.objects.order_by('-gold', '-silver', '-bronze')
    

class MedalCountListView(generics.ListCreateAPIView):
    serializer_class = CountrySerializer

    def get_queryset(self):
        # all data from country model
        queryset = Country.objects.all()
        
        # convert data into list
        data = list(queryset.values('country','gold', 'silver', 'bronze'))

        sorted_data = self.manual_sort(data)

        return sorted_data

    def manual_sort(self, data):
        # Empty list for storing sorted data
        sorted_data = []

        while data:
            # find index of max element
            max = 0
            for i in range(1, len(data)):
                if self.compare(data[i], data[max]) > 0:
                
                    max = i

            # append max in sorted_data and pop max from data
            sorted_data.append(data.pop(max))
            print(data)

        return sorted_data

    def compare(self, country1, country2):
        # compair two contries medals by gold, silver and bronze
        if country1['gold'] > country2['gold']:
            return 1
        elif country1['gold'] < country2['gold']:
            return 0
        else:
            if country1['silver'] > country2['silver']:
                return 1
            elif country1['silver'] < country2['silver']:
                return 0
            else:
                if country1['bronze'] > country2['bronze']:
                    return 1
                elif country1['bronze'] < country2['bronze']:
                    return 0
                else:
                    return 0


# class CountryViewSet(APIView):
#     def get(self, request):
#         country = Country.objects.all()
#         Serializer = CountrySerializer(country, many=True)
#         return Response(Serializer.data)
    
#     def post(self, request):
#         Serializer = CountrySerializer(data = request.data)
#         if Serializer.is_valid():
#             Serializer.save()
#             return Response(Serializer.data, status=status.HTTP_201_CREATED)
#         return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)

