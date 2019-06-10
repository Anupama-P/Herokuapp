from django.db.models import Avg, Sum
from rest_framework import serializers

from .models import Site


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ('id', 'name')

    def to_representation(self, obj):
        if self.context['view'].action == 'sum':
            total_a = obj.site_holdings.all().aggregate(Sum('a_value'))['a_value__sum']
            total_b = obj.site_holdings.all().aggregate(Sum('b_value'))['b_value__sum']
            return {
                'id': obj.id,
                'name': obj.name,
                'sum_a': total_a,
                'sum_b': total_b
            }
        elif self.context['view'].action == 'average':
            avg_a = obj.site_holdings.all().aggregate(Avg('a_value'))['a_value__avg']
            avg_b = obj.site_holdings.all().aggregate(Avg('b_value'))['b_value__avg']
            return {
                'id': obj.id,
                'name': obj.name,
                'average_a': avg_a,
                'average_b': avg_b
            }
        elif self.context['view'].action == 'retrieve':
            site_holdings = []
            for holding in obj.site_holdings.all():
                site_holdings.append({
                    'id': holding.id,
                    'a_value': holding.a_value,
                    'b_value': holding.b_value,
                    'create_date': holding.created_date
                })
            return {
                'id': obj.id,
                'name': obj.name,
                'number': obj.site_holdings.count(),
                'site_holdings': site_holdings
            }
        else:
            return {
                'id': obj.id,
                'name': obj.name,
                'number': obj.site_holdings.count()
            }
