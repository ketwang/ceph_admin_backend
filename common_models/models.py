from django.db import models

# Create your models here.

#models for cluster
class Cluster(models.Model):
    name = models.CharField(max_length=50)
    api = models.GenericIPAddressField()
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    #created_at.editable = True  # used for model_to_dict function
    updated_at = models.DateTimeField(auto_now=True)
    #updated_at.editable = True  # used for model_to_dict function
    class Meta:
        db_table = 'cluster'
class ClusterCapacity(models.Model):
    total_kb = models.FloatField(null=True)
    total_kb_avail = models.FloatField(null=True)
    total_kb_used = models.FloatField(null=True)
    #created_at.editable = True #used for model_to_dict function
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    class Meta:
        db_table = 'cluster_capacity'

class Rack(models.Model):
    name = models.CharField(max_length=30)
    idc = models.CharField(max_length=30)
    room = models.CharField(max_length=30)
    row = models.IntegerField()
    column = models.IntegerField()
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    class Meta:
        db_table = 'rack'

class Server(models.Model):
    sn = models.CharField(max_length=10)
    manufacture = models.CharField(max_length=10)
    server_model = models.CharField(max_length=20)
    ip = models.IPAddressField()
    admin_ip = models.IPAddressField()
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
    class Meta:
        db_table = 'server'

#model for osd
POOL_FROM_CHOICES = (
    ('CMD', 'pool created by command'),
    ('WEB', 'pool created by web page')
)

OSD_CLASS_CHOICES = (
    ('ssd', 'solid state disk'),
    ('sata', 'sata disk')
)
class Osd(models.Model):
    osd_id = models.IntegerField()
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    up = models.IntegerField(default=0)
    _in = models.IntegerField(default=0)
    exists = models.IntegerField(default=0)
    comeFrom = models.CharField(max_length=3, choices=POOL_FROM_CHOICES)
    uuid = models.UUIDField(null=True)
    weight = models.FloatField(default=.0)
    public_addr = models.CharField(max_length=100, null=True)
    cluster_addr = models.CharField(max_length=100, null=True)
    heartbeat_back_addr = models.CharField(max_length=100, null=True)
    heartbeat_front_addr = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    osd_class = models.CharField(max_length=20, choices=OSD_CLASS_CHOICES, default='sata')
    class Meta:
        db_table='osd'

class OsdCapacity(models.Model):
    osd = models.ForeignKey(Osd, on_delete=models.CASCADE)
    crush_weight = models.FloatField()
    reweight = models.FloatField()
    kb_avail = models.IntegerField()
    kb_used = models.IntegerField()
    kb = models.IntegerField()
    pgs = models.IntegerField()
    utilization = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    class Meta:
        db_table='osd_capacity'

class Rule(models.Model):
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    ruleset = models.IntegerField()
    rule_id = models.IntegerField()
    rule_name = models.CharField(max_length=100)
    type = models.IntegerField()
    max_size = models.IntegerField()
    min_size = models.IntegerField()
    step1 = models.ForeignKey('Crush')
    step2 = models.CharField(max_length=100)
    step3 = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
            db_table = 'rule'
# model for crush rule
#models for pool
COME_FROM_CHOICES = (
    ('CMD', 'pool created by command'),
    ('WEB', 'pool created by web page')
)
class Pool(models.Model):
    pool_name = models.CharField(max_length=50)
    pool_id = models.IntegerField()
    type = models.IntegerField(default=1)
    size = models.IntegerField(default=1)
    min_size = models.IntegerField(default=3)
    rule = models.ForeignKey(Rule, null=True)
    pg_num = models.IntegerField(default=0)
    pg_placement_num = models.IntegerField(default=0)
    crash_replay_interval = models.IntegerField(default=0)
    quota_max_bytes = models.IntegerField(default=0)
    quota_max_objects = models.IntegerField(default=0)
    tier_pool = models.ForeignKey('self', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cluster = models.ForeignKey(Cluster)
    comeFrom = models.CharField(max_length=3, choices=COME_FROM_CHOICES)
    class Meta:
        db_table='pool'


class PoolCapacity(models.Model):
    bytes_used = models.BigIntegerField()
    max_avail = models.BigIntegerField()
    objectsNum = models.IntegerField()
    kb_used = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    pool = models.ForeignKey(Pool, on_delete=models.CASCADE)
    class Meta:
        db_table = 'pool_capacity'


class Crush(models.Model):
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    crush_id = models.IntegerField()
    type = models.CharField(max_length=25)
    type_id = models.IntegerField()
    name = models.CharField(max_length=25)
    children_list = models.CharField(max_length=100, default='[]')
    #all above is used for osd
    crush_weight = models.FloatField(default=.0)
    reweight = models.FloatField(default=.0)
    primary_affinity = models.FloatField(default=.0)
    depth = models.IntegerField(default=0)
    exists = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'crush_type'



class OsdProperty(models.Model):
    full_ratio = models.FloatField()
    backfillfull_ratio = models.FloatField()
    nearfull_ratio = models.FloatField()
    pool_max = models.IntegerField()
    max_osd = models.IntegerField()
    require_min_compat_client = models.CharField(max_length=20)
    min_compat_client = models.CharField(max_length=20)
    min_compat_client_version = models.FloatField()
    cluster = models.ForeignKey(Cluster, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'osd_property'


class RBD(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True)
    ip = models.GenericIPAddressField(null=True)
    pool = models.ForeignKey(Pool, on_delete=models.CASCADE, related_name='images')
    num_objs = models.IntegerField(null=True)
    block_name_prefix = models.CharField(max_length=100, null=True)
    obj_size = models.IntegerField(null=True)
    size = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    class Meta:
        db_table = 'rbd'