from django.db import models


class NewsModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'news'
        verbose_name = 'News'


class StandardsModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateField()
    description = models.TextField()
    standard_code = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'standards'
        verbose_name = 'Standards'
        verbose_name_plural = 'Standards'
        unique_together = (('standard_code', 'title'),)
        ordering = ('title',)


class UnitsModel(models.Model):
    position=models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.name


    class Meta:
        db_table = 'units'
        verbose_name = 'Units'
        verbose_name_plural = 'Units'
        unique_together = (('position', 'name'),)
        ordering = ('position', 'name')


class LeadershipModel(models.Model):
    position=models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    phone=models.CharField(max_length=100)
    specialty=models.CharField(max_length=100)
    Reception_days=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'leadership'
        verbose_name = 'Leadership'
        verbose_name_plural = 'Leadership'
        unique_together = (('position', 'name'),)
        ordering = ('position', 'name')

