from django.contrib import admin
from .models.donor import Donor
from .models.donation import Donation
    
admin.site.register(Donor) #register donor in admin site
admin.site.register(Donation)
