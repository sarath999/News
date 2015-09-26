from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
class Warning(models.Model):
    headLine = models.CharField(max_length=100)
    news_content = models.TextField()
    
    #authors = models.ManyToManyField(Author)
    #publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.headLine
class Information(models.Model):
    headLine = models.CharField(max_length=100)
    news_content = models.TextField()
    
    #authors = models.ManyToManyField(Author)
    #publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.headLine
class Succes(models.Model):
    headLine = models.CharField(max_length=100)
    news_content = models.TextField()
    
    #authors = models.ManyToManyField(Author)
    #publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.headLine
