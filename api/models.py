from django.db import models
import subprocess
import os

# Create your models here.
class Application(models.Model):
    application = models.FileField(upload_to="applications")
    package_name = models.CharField(max_length=120)
    package_version_code = models.CharField(max_length=50)

    def __str__(self):
        return self.application.name

    def set_application(self):
        file_path = os.path.join('./media/applications/',self.application.name)
        self.application = str(file_path)

    def set_package_name(self):
        file_path = os.path.join('./media/applications/',self.application.name)
        package_name_std = subprocess.run(['./bin/apk_package_name.sh',str(file_path)],stdout=subprocess.PIPE)
        self.package_name = package_name_std.stdout

    def set_package_version_code(self):
        file_path = os.path.join('./media/applications/',self.application.name)
        package_version_code_std = subprocess.run(['./bin/apk_package_version_code.sh',str(file_path)],stdout=subprocess.PIPE)
        self.package_version_code = package_version_code_std.stdout
    
    def save(self, *args, **kwargs):
        self.set_application()
        self.set_package_name()
        self.set_package_version_code()
        return super(Application,self).save(*args,**kwargs)