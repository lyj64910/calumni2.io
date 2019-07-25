from django.db import models


class Cal(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(null=True)
    apply = models.TextField(null=True)
    score = models.TextField(null=True)
    write = models.TextField(null=True)
    act = models.TextField(null=True)
    schoolact = models.TextField(null=True)
    cer = models.CharField(null=True, max_length=50)
    pub_date = models.DateTimeField("data published")
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]