from django.db import models

class BlogRecord(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.__str__() + ' ' + self.title.__str__()[:30]