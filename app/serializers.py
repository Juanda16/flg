from rest_framework import routers, serializers, viewsets
from .models import Donor
from django.core import serializers

class DonorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Donor
        fields = ('user.username', 'documentType','documentId')

 
data = serializers.serialize("json", DonorModel.objects.all())       