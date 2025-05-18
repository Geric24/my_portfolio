from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Content)
admin.site.register(models.Projects)
admin.site.register(models.LandscapeProjects)
admin.site.register(models.NCModel)
admin.site.register(models.Geric)