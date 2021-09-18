from django.conf.urls import url
from apps.cotacoes.serializers import CotacaoSerializer
from rest_framework import viewsets, status 
from rest_framework.response import Response
from rest_framework.decorators import action
import requests
from .models import Cotacao, Wallet


class CotacaoViewSet(viewsets.ModelViewSet):
    queryset = Cotacao.objects.all()
    serializer_class = CotacaoSerializer
    http_method_names = ['get', 'post']

    @action(detail=False, methods=['post'])
    def create_wallet(self, request: Cotacao):

        if request.method == 'POST': # verify if the request is a POST

            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }

            data = request.data

            if type(data['wallet']) == list:

                payload = []

                for ticker in data['wallet']:

                    url = f"https://api.tiingo.com/tiingo/daily/{ticker}/prices?startDate={data['startDate']}&endDate={data['endDate']}&token=ded39ee54a425cc9015140762871aae22d48288c"

                    response = requests.get(url, headers=headers).json()

                    for item in response:

                        wallet = Wallet.objects.create(
                            close=item['close'],
                            high=item['high'],
                            low=item['low'],
                            open=item['open'],
                            volume=item['volume']
                        )
    
                        payload.append({
                            'ticker': ticker,
                            'date': item['date'],
                            'open': item['open'],
                            'high': item['high'],
                            'low': item['low'],
                            'close': item['close'],
                            'volume': item['volume']
                        })

                return Response({
                    'status': 'success',
                    'data': payload
                }, status=status.HTTP_201_CREATED)
            
            url = f"https://api.tiingo.com/tiingo/daily/{data['wallet']}/prices?startDate={data['startDate']}&endDate={data['endDate']}&token=ded39ee54a425cc9015140762871aae22d48288c"

            response = requests.get(url, headers=headers).json()

            for item in response: # verify if the response is a list
                wallet = Wallet.objects.create(
                    close=item['close'],
                    high=item['high'],
                    low=item['low'],
                    open=item['open'],
                    volume=item['volume']
                )

                payload = {
                    'ticker': data['wallet'],
                    'date': item['date'],
                    'open': item['open'],

                    'high': item['high'],
                    'low': item['low'],
                    'close': item['close'],
                    'volume': item['volume']
                }

            return Response({
                'status': "success",
                'data': payload
            }, status=status.HTTP_201_CREATED)


        