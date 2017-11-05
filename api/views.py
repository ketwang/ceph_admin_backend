from django.shortcuts import render

# Create your views here.
from common_models.models import Cluster, ClusterCapacity
from serializers import ClusterSerializer, ClusterCapacitySerializer
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from django.http import Http404

class ClusterList(APIView):
    def get(self, request, format=None):
        start = request.query_params.get('start', 0)
        num = request.query_params.get('num', 20)  # for pagination
        clusters = Cluster.objects.all()
        serializer = ClusterSerializer(clusters, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ClusterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ClusterDetail(APIView):
    def get_object(self, pk):
        try:
            return Cluster.objects.get(pk=pk)
        except Cluster.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        cluster = self.get_object(pk)
        serializer = ClusterSerializer(cluster)
        return Response(serializer.data)
    def delete(self, request, pk, format=None):
        cluster = self.get_object(pk)
        cluster.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self, request, pk, format=None):
        cluster = self.get_object(pk)
        serializer = ClusterSerializer(cluster, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClusterCapacityList(APIView):
    def get(self, request, format=None):
        start_time = request.query_params.get('start_time', 1)
        end_time = request.query_params.get('end_time', 2)
        cluster_id = request.query_params.get('cluster_id', False)
        if not cluster_id:
            return Response({'cluster': 'required'}, status=status.HTTP_400_BAD_REQUEST)
        clusterCapacity = ClusterCapacity.objects.filter(cluster = Cluster.objects.get(pk=cluster_id))
        serializer = ClusterCapacitySerializer(clusterCapacity, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ClusterCapacitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)