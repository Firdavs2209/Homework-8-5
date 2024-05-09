from django.db import models


class ConnectionModel(models.Model):
    fullname= models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    management= models.TextField()
    text=models.TextField()


    def __str__(self):
        return self.fullname



    class Meta:
        db_table = 'connection'
        verbose_name = 'connections'
        verbose_name_plural = 'Connections'