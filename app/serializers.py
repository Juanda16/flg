from .models.donor import Donor
from rest_framework import routers, serializers, viewsets
from django.urls import path, include
from django.contrib.auth.models import User

#serializer implemented to send JSON response
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= User
        fields= ('id','username','first_name','last_name','email') 

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user
        #instance.username = validated_data.get('username', instance.user.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.password = validated_data.get('email', instance.password)
        instance.user.email = validated_data.get('password', instance.email)
        user.save()

        return instance


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

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user
        #instance.user.username = validated_data.get('username', instance.user.username)
        instance.user.first_name = validated_data.get('first_name', instance.user.first_name)
        instance.user.last_name = validated_data.get('last_name', instance.user.last_name)
        instance.user.password = validated_data.get('email', instance.email)
        instance.user.email = validated_data.get('password', instance.user.password)
        instance.user.save()
        user.is_premium_member = user_data.get(
            'is_premium_member',
            user.is_premium_member
        )
        user.has_support_contract = user_data.get(
            'has_support_contract',
            user.has_support_contract
         )
        instance.documentId = validated_data.get('content', instance.documentId)
        instance.documentType = validated_data.get('created', instance.documentTyp)
        instance.legalNature = validated_data.get('created', instance.legalNature)
        instance.save()
        return instance
        
          

        

 
#data = serializers.serialize("json", DonorModel.objects.all())       