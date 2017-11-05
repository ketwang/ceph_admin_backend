from django.shortcuts import render

# Create your views here.
from common_models.models import Cluster, ClusterCapacity, Osd, OsdCapacity, Pool, PoolCapacity, Crush, RBD
from django.forms import  model_to_dict
from django.http.response import JsonResponse
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
import json
import logging

logger = logging.getLogger('stand_rest_frame.api')

def getAllCluster(request):
    ret = []
    for cluster in Cluster.objects.all():
        cc = ClusterCapacity.objects.filter(cluster=cluster).last()
        cluster = model_to_dict(cluster)
        ret.append(cluster)
    return JsonResponse(ret, safe=False)

#used for changing queryset to json
class ClusterCapacSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClusterCapacity
        fields = '__all__'
def getClusterCapac(request, pk):
    cluster = Cluster.objects.get(pk=pk)
    cc = ClusterCapacity.objects.filter(cluster=cluster).last()
    serializer = ClusterCapacSerializer(cc)
    return JsonResponse(serializer.data, safe=False)

# for frontend osd dashboard
class OsdCapacitySerializer(serializers.ModelSerializer):
    class Meta:
        model = OsdCapacity
        fields = '__all__'
        depth = 1
def getOSDs(request, pk):
    ret = []
    cluster = Cluster.objects.get(pk = pk)
    osds = Osd.objects.filter(cluster=cluster)
    for osd in osds:
        osdCapac = OsdCapacity.objects.filter(osd=osd).last()
        serializer = OsdCapacitySerializer(osdCapac)
        ret.append(serializer.data)
    return JsonResponse(ret, safe=False)


# for frontend pool dashboard
class PoolCapacitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PoolCapacity
        fields = '__all__'
        depth = 3
class PoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pool
        fields = '__all__'
        depth = 1
def getPools(request, pk):
    ret =[]
    cluster = Cluster.objects.get(pk = pk)
    pools = Pool.objects.filter(cluster=cluster)
    for pool in pools:
        poolCapac = PoolCapacity.objects.filter(pool=pool).last()
        serializer = PoolCapacitySerializer(poolCapac)
        ret.append(serializer.data)
    return JsonResponse(ret, safe=False)

class CrushSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crush
        fields = '__all__'
def getCrush(request, pk):
    cluster = Cluster.objects.get(pk=pk)
    crushs = Crush.objects.filter(cluster=cluster)
    serializer = CrushSerializer(crushs, many=True)
    return JsonResponse(serializer.data, safe=False)

class CrushTreeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    def get_children(self, obj):
        crushes = Crush.objects.filter(cluster=obj.cluster, crush_id__in=json.loads(obj.children_list))
        #serializer = CrushSerializer(crushes, many=True)
        serializer = self.__class__(crushes, many=True)
        return serializer.data
    class Meta:
        model = Crush
        fields = '__all__'
        depth = 5
def getCrushTree(request, pk):
    logger.error('some one get crush message')
    cluster = Cluster.objects.get(pk = pk)
    crushes = Crush.objects.filter(cluster=cluster, type_id=10) #this is the top level hirech
    serializer = CrushTreeSerializer(crushes, many=True)
    return JsonResponse(serializer.data, safe=False)



'''
class RBDSerializer(serializers.ModelSerializer):
    class Meta:
            model = RBD
            fields = '__all__'
class PoolWithImagesSerializer(serializers.ModelSerialzier):
    images = RBDSerializer(many=True, read_only=True)
    class Meta:
            model = Pool
            fileds = '__all__'
'''
class PoolWithImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pool
        fields = ('id', 'pool_name', 'images')
def getImages(request, pk):
    pool = Pool.objects.get(pk = pk)
    serializer = PoolWithImagesSerializer(pool)
    return JsonResponse(serializer.data, safe=False)