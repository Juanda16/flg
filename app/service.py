
from app.models import Donor
from django.contrib.auth.models import User

def gettingUser (id):

      user = User.objects.get(id=id)
      donor=Donor.objects.get(user_id=user.id)
      return donor
    