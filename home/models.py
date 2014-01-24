from django.db import models

class Newsartikel(models.Model):
    head = models.CharField(max_length=200)
    pic = models.CharField(max_length=30)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.head
