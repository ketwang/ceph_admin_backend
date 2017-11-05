from common_models.models import Osd, OsdCapacity, Cluster, Rule, Crush
from serializers import OsdSerializer, OsdCapacitySerializer, RuleSerializer
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import GenericAPIView, ListAPIView

class RuleList(APIView):
    def get(self, request, pk,format=None):
        cluster = Cluster.objects.get(pk=pk)
        rules = Rule.objects.filter(cluster=cluster)
        serializer = RuleSerializer(rules, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, pk, format=None):
        cluster = Cluster.objects.get(pk = pk)
        rules = Rule.objects.filter(cluster=cluster)
        data = request.data
        data['cluster'] = pk
        data['step1'] = Crush.objects.get(crush_id=data['step1'], cluster=cluster).id
        for rule in rules:
            if rule.rule_id == request.data['rule_id']:
                serializer = RuleSerializer(rule, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer = RuleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print serializer.errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)