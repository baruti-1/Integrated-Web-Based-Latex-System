from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

class TemplateClass(models.Model):
    template_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    template_file = models.FileField(upload_to='template_folder/')
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Template'

class Report(models.Model):
    template_file = models.FileField(upload_to='template_folder/')
    user = models.ForeignKey(User, on_delete=CASCADE)
 

    