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


