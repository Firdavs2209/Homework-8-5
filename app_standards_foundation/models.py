from django.db import models


class StandardModel(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    description = models.TextField()


    def __str__(self):
        return self.name



    class Meta:
        db_table = 'standardslar'
        verbose_name = 'standart'
        verbose_name_plural = 'standart'
