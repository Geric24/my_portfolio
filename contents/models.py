from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class Geric(models.Model):
    abt_img = models.ImageField(upload_to="self_img/")
    
    def image_tag(self):
        return mark_safe('<img src"%s" width="80" />' % (self.abt_img.url))

class Content(models.Model):
    content_img = models.ImageField(upload_to="content_img/")

    def image_tag(self):
        return mark_safe('<img src"%s" width="80" />' % (self.content_img.url))

class Projects(models.Model):
    project_img = models.ImageField(upload_to="projects_img/")
    
    def image_tag(self):
        return mark_safe('<img src"%s" width="80" />' % (self.project_img.url))
    
class NCModel(models.Model):
    nc_img = models.ImageField(upload_to="nc_img/")
    
    def image_tag(self):
        return mark_safe('<img src"%s" width="80" />' % (self.nc_img.url))
    
class LandscapeProjects(models.Model):
    landscape_project_img = models.ImageField(upload_to="landscape_projects_img/")
    
    def image_tag(self):
        return mark_safe('<img src"%s" width="80" />' % (self.nc_img.url))