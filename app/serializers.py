from .models.donor import Donor
from rest_framework import routers, serializers, viewsets
from django.urls import path, include

#serializer implemented to send JSON response

class DonorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Donor
        fields = ('id','documentId', 'documentType','legalNature','user_id')

 
#data = serializers.serialize("json", DonorModel.objects.all())       