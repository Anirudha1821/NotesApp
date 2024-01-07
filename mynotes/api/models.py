from django.db import models

# Create your models here.
class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True) #each time updated
    created = models.DateTimeField(auto_now_add=True) #auto_now_add only take when model is created

    def __str__(self):
        return self.body[0:50]
    class Meta:
        db_table = 'tbl_Notes'