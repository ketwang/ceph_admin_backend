from common_models.models import Cluster, Pool, PoolCapacity, Rule, RBD
from serializers import PoolSerializer, PoolCapacitySerializer, RBDSerializer
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.forms.models import model_to_dict


class PoolList(APIView):
    def get(self, request, pk, format=None):
        cluster = Cluster.objects.get(pk = pk)
        pools = Pool.objects.filter(cluster=cluster)
        serializer = PoolSerializer(pools, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, pk, format=None):
        cluster = Cluster.objects.get(pk = pk)
        pool = Pool.objects.filter(cluster = cluster, pool_id=request.data['pool_id'])
        data = request.data
        rule = Rule.objects.get(cluster=cluster, rule_id = data['rule'])
        data['rule'] = rule.id
        #data['rule'] = 10
        data['cluster'] = pk
        if len(data['tier_pool']):
            tier_pool = Pool.objects.filter(pool_id = data['tier_pool'][0], cluster=cluster) #only support one tiering layer
            if len(tier_pool) == 1:
                data['tier_pool'] = tier_pool[0].id
        else:
            del data['tier_pool']
        if len(pool) == 0:
            serializer = PoolSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if len(pool) == 1:
            print data
            serializer = PoolSerializer(pool[0], data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                print serializer.data
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'exit two record'}, status=status.HTTP_400_BAD_REQUEST)

class PoolCapacityList(APIView):
    def get(self, request, pk, format=None):
        pools = PoolCapacity.objects.filter(pool_id=pk)
        serializer = PoolCapacitySerializer(pools, many=True)
        return Response(serializer.data)
    def post(self, request, pk, format=None):
        data = request.data
        cluster = Cluster.objects.get(pk = pk)
        pool = Pool.objects.filter(cluster=cluster, pool_id=data['pool_id'])
        if len(pool) == 0:
            raise Http404
        data['pool'] = pool[0].id
        serializer = PoolCapacitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RBDList(APIView):
    def get(self, request, pk, format=None):
        cluster = Cluster.objects.get(pk = pk)
        pools = Pool.objects.filter(cluster=cluster)
        RBDs = RBD.objects.filter(pool__in=pools)
        serializer = RBDSerializer(RBDs, many=True)
        return Response(serializer.data)
    def post(self, request, pk, format=None):
        data = request.data
        cluster = Cluster.objects.get(pk = pk)
        pool = Pool.objects.get(cluster=cluster, pool_name=data['pool_name'])
        data['pool'] = pool.id
        try:
            parent_rbd = RBD.objects.get(name = data['parent_name'], cluster=cluster)
            data['parent'] = parent_rbd.id
        except RBD.DoesNotExist:
            pass
        data['name'] = data['rbd_name']
        rbd = RBD.objects.filter(pool=pool, name=data['rbd_name'])
        if len(rbd) == 0:
            serializer = RBDSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if len(rbd) == 1:
            serializer = RBDSerializer(rbd[0], data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'exits more than one'}, status=status.HTTP_400_BAD_REQUEST)