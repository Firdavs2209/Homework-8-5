from django.db import models


class BuildingModel(models.Model):
    name = models.CharField(max_length=255)
    code = models.IntegerField()
    number = models.IntegerField()
    pdf_file = models.FileField(upload_to='documents/')



    def __str__(self):
        return self.name


    class Meta:
        db_table = 'building'
        verbose_name = 'Building'