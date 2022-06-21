from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Profile

def Profile_signals(sender,instance,created,**kwarg):
    if created :
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Profile.objects.create(
            user = instance,
            name = instance.username,
            first_name = instance.first_name,
            last_name = instance.last_name,
            email = instance.email
        )

post_save.connect(Profile_signals,sender=User)