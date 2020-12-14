from .models.donor import Donor
from rest_framework import routers, serializers, viewsets
from django.urls import path, include
from django.contrib.auth.models import User

#serializer implemented to send JSON response
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= User
        fields= ('id','username','first_name','last_name','email') 


class DonorSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(
        many=False,
        read_only=False,
        )

    class Meta:
        model = Donor
        fields = ('id','documentId', 'documentType','legalNature','user')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        donor= Donor.objects.create(user=user, **validated_data)
        
        return donor

        

 
#data = serializers.serialize("json", DonorModel.objects.all())       