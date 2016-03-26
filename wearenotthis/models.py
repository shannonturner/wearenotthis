from django.db import models

# Create your models here.

class Supporter(models.Model):

    # Name of the company or organization in support
    name = models.CharField(max_length=255)
    
    # Short, snappy version to display
    support_snippet = models.TextField()
    
    # Full version of the text in support
    support_long = models.TextField(default='')
    
    # Link to "prove" the support
    link = models.CharField(max_length=255)

    # URL of the logo
    logo = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
