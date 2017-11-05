from rest_framework import serializers
from common_models.models import Cluster, ClusterCapacity
from common_models.models import Pool, PoolCapacity
from common_models.models import Osd, OsdCapacity, OsdProperty
from common_models.models import Crush, Rule
from common_models.models import RBD


#for cluster
class ClusterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cluster
        fields = '__all__'
        #fields = ('id', )
class ClusterCapacitySerializer(serializers.ModelSerializer):
    '''def create(self, validated_data):
        validated_data['cluster'] = Cluster.objects.get(pk=validated_data['cluster'])
        clusterCapa = Cluster.objects.create(**validated_data)
        return clusterCapa
    '''
    class Meta:
        model = ClusterCapacity
        fields = '__all__'


#for osd
class OsdPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = OsdProperty
        fields = '__all__'
class OsdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osd
        fields = '__all__'
    '''def create(self, validated_data):
        validated_data['cluster'] = Cluster.objects.get(pk=validated_data['cluster'])
        osd = Osd.objects.create(**validated_data)
        return osd
    '''
class OsdCapacitySerializer(serializers.ModelSerializer):
    class Meta:
        model = OsdCapacity
        fields = '__all__'
    '''def create(self, validated_data):
        validated_data['osd'] = Osd.objects.get(pk=validated_data['osd'])
        osdCapa = OsdCapacity.objects.create(**validated_data)
        return osdCapa
    '''

#for pool
class PoolSerializer(serializers.ModelSerializer):
    '''def create(self, validated_data):
        validated_data['cluster'] = Cluster.objects.create(pk=validated_data['cluster'])
        pool = Pool.objects.create(**validated_data)
        return pool
    '''
    class Meta:
        model = Pool
        fields = '__all__'
        #depth = 1

class PoolCapacitySerializer(serializers.ModelSerializer):
    '''def create(self, validated_data):
        validated_data['pool'] = Pool.objects.get(pk=validated_data['pool'])
        poolCapac = PoolCapacity.objects.create(**validated_data)
        return poolCapac
    '''
    class Meta:
        model = PoolCapacity
        fields = '__all__'

class CrushSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crush
        fields = '__all__'

class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = '__all__'
        depth = 1


class RBDSerializer(serializers.ModelSerializer):
    class Meta:
        model = RBD
        fields = '__all__'
        depth = 1