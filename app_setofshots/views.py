from rest_framework.decorators import api_view
from rest_framework.response import Response
from http import HTTPStatus

from .models import Bar
from .serializers import BarSerializer


@api_view(['GET'])
def get_list_of_bars(request):
    bars = Bar.objects.all()
    serializer = BarSerializer(bars, many=True)
    return Response(serializer.data, status=HTTPStatus.OK)
