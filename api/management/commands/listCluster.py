from django.core.management.base import BaseCommand, CommandError
from common_models.models import Cluster
from django.forms.models import model_to_dict
class Command(BaseCommand):
    help = 'show all cluster info'
    def add_arguments(self, parser):
        parser.add_argument('cluster_name', nargs='+', type=str)
    def handle(self, *args, **options):
        for cluster_name in options['cluster_name']:
            try:
                cluster = Cluster.objects.get(name=cluster_name)
            except Cluster.DoesNotExist:
                raise CommandError('cluster "%s" does not exists' % cluster_name)
            print model_to_dict(cluster)