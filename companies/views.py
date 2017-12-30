from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.views import status
from .models import Stock
from .serializers import StockSerialzer


class StockList(APIView):

    def get(self,request):
        stocks = Stock.objects.all()
        serializer= StockSerialzer(stocks,many=True)
        return Response(serializer.data)





    def post(self,request):
        pass




