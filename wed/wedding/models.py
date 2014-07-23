from django.db import models
from django.contrib.auth.models import User


class Vendor(models.Model):
    # user = models.OneToOneField(
    #     User,
    #     related_name='vendor',
    #     blank=True,
    #     null=True)
    mobile = models.CharField(max_length=20)
    about = models.CharField(max_length=60)
    website = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    invites_allowed = models.IntegerField(null=True, blank=True)
    invites_left = models.IntegerField(null=True, blank=True)
# images        = GenericImage
# locations     = Location
# booking_amount= Range
# experience    = Experience

# Vedios        = Custom Type Array    # Later
# availablity   = CustomType           # Later
# rating        = IntegerRangeField(min_value=1, max_value=10)


class Display(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now=True)
    experience = models.FloatField()
    number = models.IntegerField()
    image = models.ImageField(upload_to='image', null=True, blank=True)
    # class GenericImage(models.Model):
    #     GALLERY_IMAGE, PROFILE_IMAGE, HEADER_IMAGE = 0, 1, 2
    #     ImageType = ((GALLERY_IMAGE, 'GALLERY_IMAGE'),
    #                  (PROFILE_IMAGE, 'PROFILE_IMAGE'),
    #                  (HEADER_IMAGE, 'HEADER_IMAGE'),
    #                  )
    #     vendor = models.ForeignKey(Vendor, related_name='images')
    #     image = models.ImageField(
    #         upload_to='GALLERY_OF_IMAGES/',
    #         default=GALLERY_IMAGE,
    #         choices=ImageType)
