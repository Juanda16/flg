from .models.donor import Donor
from rest_framework import routers, serializers, viewsets
from django.urls import path, include

#serializer implemented to send JSON response

class DonorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Donor
        fields = ('documentId', 'documentType','legalNature')

 
#data = serializers.serialize("json", DonorModel.objects.all())       