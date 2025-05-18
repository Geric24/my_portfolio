from django.shortcuts import render
from django.http import HttpResponse
from . import models

def main_content(request):
    content_imgs = models.Content.objects.all()
    project_imgs = models.Projects.objects.all()
    landscape_project_img = models.LandscapeProjects.objects.all()
    nc_img = models.NCModel.objects.get()
    geric_img = models.Geric.objects.get()
    return render(request, 'contents/contents.html', {"content_imgs":content_imgs, "project_imgs":project_imgs,"nc_img":nc_img, "geric_img":geric_img, "landscape_project_imgs":landscape_project_img})