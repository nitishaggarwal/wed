from django.contrib.auth.models import User
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource
from wedding.models import Display, Vendor


# class UserResource(ModelResource):

#     class Meta:
#         queryset = User.objects.all()
#         resource_name = 'user'


class DisplayResource(ModelResource):

    class Meta:
        queryset = Display.objects.all()
        resource_name = 'display'
        authorization = Authorization()
        always_return_data = True


class VendorResource(ModelResource):
    # user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Vendor.objects.all()
        resource_name = 'vendor'
