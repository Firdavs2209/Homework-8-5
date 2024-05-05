from django.db import models


class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()
    description = models.TextField()


    def __str__(self):
        return self.title



    class Meta:
        db_table = 'announcements'
        verbose_name = 'Announcement'