from django.shortcuts import render

# Create your views here.
from common_models.models import Osd, OsdCapacity, Cluster, OsdProperty
from serializers import OsdSerializer, OsdCapacitySerializer, OsdPropertySerializer
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from django.http import Http404

class OsdList(APIView):
    def get(self, request, pk, format=None):
        start = request.query_params.get('start', 0)
        num = request.query_params.get('num', 20)  # for pagination
        cluster = Cluster.objects.get(pk = pk)
        osds = Osd.objects.filter(cluster=cluster)
        serializer = OsdSerializer(osds, many=True)
        return Response(serializer.data)
    def post(self, request, pk, format=None):
        data = request.data
        data['cluster'] = pk
        cluster = Cluster.objects.get(pk = pk)
        osds = Osd.objects.filter(cluster=cluster)
        for osd in osds:
            if data['osd_id'] == osd.osd_id:
                serializer = OsdSerializer(osd, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer = OsdSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer = OsdSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class OsdDetail(APIView):
    pass


class OsdCapacityList(APIView):
    def get(self, request, pk, format=None):
        osdCapac = OsdCapacity.objects.filter(osd_id=pk)
        serializer = OsdCapacitySerializer(osdCapac, many=True)
        return Response(serializer.data)
    def post(self, request, pk, format=None):
        cluster = Cluster.objects.get(pk = pk)
        data = request.data
        osd = Osd.objects.filter(cluster=cluster, osd_id=data['id'])
        if len(osd) == 0:
            raise Http404
        data['osd'] = osd[0].id
        del data['id']
        serializer = OsdCapacitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OsdPropertyList(APIView):
    def get(self, request, pk, format=None):
        cluster = Cluster.objects.get(pk = pk)
        osdProperty = OsdProperty.objects.get(cluster=cluster)
        serializer = OsdPropertySerializer(osdProperty)
        return Response(serializer.data)
    def post(self, request, pk, format=None):
        data = request.data
        data['cluster'] = pk
        osdProrperty = OsdProperty.objects.filter(cluster=Cluster.objects.filter(pk=pk))
        if len(osdProrperty) == 0:
            serializer = OsdPropertySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if len(osdProrperty) == 1:
            serializer = OsdPropertySerializer(osdProrperty[0], data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'pool_property exits >= 2 '}, status=status.HTTP_400_BAD_REQUEST)
