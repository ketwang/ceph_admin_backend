from common_models.models import Osd, OsdCapacity, Cluster, Crush
from serializers import OsdSerializer, OsdCapacitySerializer, CrushSerializer
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

import json
class CrushList(APIView):
    def get(self, request, pk, format=None):
        cluster = Cluster.objects.get(pk = pk)
        crush = Crush.objects.filter(cluster=cluster)
        serializer = CrushSerializer(crush, many=True)
        return Response(serializer.data)
    def post(self, request, pk, format=None):
        cluster = Cluster.objects.get(pk = pk)
        crushs = Crush.objects.filter(cluster=cluster, crush_id=request.data.get('crush_id'))
        data = request.data
        if data.has_key('children'):
            data['children'] = json.dumps(data['children'])
        if len(crushs) == 0:
            serializer = CrushSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if len(crushs) != 1:
            return Response({'message': '>=2 record exists'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = CrushSerializer(crushs[0], data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)