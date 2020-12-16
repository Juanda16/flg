from .models.donor import Donor
from .models.donation import Donation
from rest_framework import routers, serializers, viewsets
from django.urls import path, include
from django.contrib.auth.models import User
from django.contrib.auth import password_validation, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator




#serializer implemented to send JSON response
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= User
        fields= ('id','username','first_name','last_name','email','is_active') 

    """ def validate(self, data):
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        password_validation.validate_password(passwd)

        return data """

    def create(self, data):
        user = User.objects.create_user(**data)
        user.is_active = True
        user.save()

        return user

    """   def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()
        return user

        

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user
        #instance.username = validated_data.get('username', instance.user.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.password = validated_data.get('password', instance.password)
        instance.user.email = validated_data.get('email', instance.email)
        user.save()

        return instance """

class UserLoginSerializer(serializers.Serializer):

    # Campos que vamos a requerir
    email = serializers.EmailField()
    password = serializers.CharField(max_length=64)

    # Primero validamos los datos
    def validate(self, data):

        # authenticate recibe las credenciales, si son válidas devuelve el objeto del usuario
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Las credenciales no son válidas')

        # Guardamos el usuario en el contexto para posteriormente en create recuperar el token
        self.context['user'] = user
        return data

    def create(self, data):
        """Generar o recuperar token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


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
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()
        
        donor= Donor.objects.create(user=user, **validated_data)
        
        return donor      
   
    def update(self, instance, validated_data):
        #user_data = validated_data.pop('user')
        #user = instance.user
        #instance.user.username = validated_data.get('username', instance.user.username)
        instance.user.first_name = validated_data.get('first_name', instance.user.first_name)
        instance.user.last_name = validated_data.get('last_name', instance.user.last_name)
        instance.user.email = validated_data.get('email', instance.user.email)
        instance.user.password = validated_data.get('password', instance.user.password)
        instance.save()
        return instance # agregado
    '''
        user.is_premium_member = user_data.get(
            'is_premium_member',
            user.is_premium_member
        )
        user.has_support_contract = user_data.get(
            'has_support_contract',
            user.has_support_contract
         )
        
        instance.documentId = validated_data.get('content', instance.documentId)
        instance.documentType = validated_data.get('created', instance.documentType)
        instance.legalNature = validated_data.get('created', instance.legalNature)
    
        instance.save()
        return instance
        '''
        
        
class DonationSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Donation
        fields = ('valueDonation','dateDonation','statusTransactionState','legalState','donorId')      

        

 
#data = serializers.serialize("json", DonorModel.objects.all())       