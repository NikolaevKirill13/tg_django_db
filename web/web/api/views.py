from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from core.models import Faq, Block
from . import serializers


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'faq': 'api/faq',
        'faq detail': 'api/faq/pk',
        'block list': 'api/block',
        'block detail': 'api/block/user_id',

    }
    return Response(api_urls)


class FaqList(generics.ListCreateAPIView):
    queryset = Faq.objects.all()
    serializer_class = serializers.FaqSerializer


class FaqDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faq.objects.all()
    serializer_class = serializers.FaqSerializer


class BlockList(generics.ListCreateAPIView):
    queryset = Block.objects.all()
    serializer_class = serializers.BlockSerializer


class BlockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Block.objects.all()
    serializer_class = serializers.BlockSerializer
    lookup_field = 'user'
