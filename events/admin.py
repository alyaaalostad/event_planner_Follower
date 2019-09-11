from django.contrib import admin
from .models import Event, UserEvent, Profile, Contact

admin.site.register(Event)
admin.site.register(UserEvent)
admin.site.register(Profile)
admin.site.register(Contact)