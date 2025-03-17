from django.db import models

class Homework(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    json_data = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.title
