from django.contrib import admin

# Register your models here.
from django.apps import apps  # Import the apps module

app = apps.get_app_config('web')  # Get the application configuration

for model in app.get_models():
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
    
    
