from django.db import models

# Create your models here.
class Application(models.Model):
    application = models.FileField(upload_to="applications")
    package_name = models.CharField(max_length=120, null=True)
    package_version_code = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name