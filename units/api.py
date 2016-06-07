from tastypie.resources import ModelResource, ALL
from tastypie.contrib.gis.resources import ModelResource as GeoModelResource
from units.models import Provider, ServiceAreas
from tastypie.authorization import Authorization
from tastypie.cache import SimpleCache
from tastypie import fields


class ProviderResource(ModelResource):

    class Meta:
        queryset = Provider.objects.all()
        resource_name = "provider"
        authorization = Authorization()
        always_return_data = True
        cache = SimpleCache(timeout=10)


class ServiceAreasResource(GeoModelResource):
    # Maps `ServiceAreas.provider` to a Tastypie `ForeignKey` field named `provider`,
    # which gets serialized using `ProviderResource`. The first appearance of
    # 'provider' on the next line of code is the Tastypie field name, the 2nd
    # appearance tells the `ForeignKey` it maps to the `provider` attribute of
    # `ServiceAreas`. Field names and model attributes don't have to be the same.
    provider = fields.ForeignKey(ProviderResource, 'provider')

    class Meta:
        queryset = ServiceAreas.objects.all()
        resource_name = "service_areas"
        excludes = ['id']
        authorization = Authorization()
        always_return_data = True
        cache = SimpleCache(timeout=10)

        filtering = {
            'geom': ALL,
        }

    def dehydrate(self, bundle):
        bundle.data['provider'] = bundle.obj.provider.name
        return bundle
