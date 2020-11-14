from django.db import models
from django.db import models
from django.utils import timezone
# Create your models here.

class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #este comentario es para saber los cambios de la nueva rama 
    documentType = models.TextField(null=True,blank=True)
    legalNature = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True )
    #birthday = models.DateField(null=True,blank=True)
    mobile = models.CharField(max_length=64, null=True,blank=True)
    #image = models.ImageField(upload_to='profile_pics/',null=True,blank=True, default='profile_pics/no_img.png')
   
    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '%s %s (%s)' % (self.user.first_name, self.user.last_name, self.user.username)
    
