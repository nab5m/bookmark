from django.db import models


class Bookmark(models.Model):
    site_name = models.CharField("사이트 이름", max_length=50)
    site_url = models.URLField("URL")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.site_name
