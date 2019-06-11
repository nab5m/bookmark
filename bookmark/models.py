from django.db import models


class Bookmark(models.Model):
    site_name = models.CharField("사이트 이름", max_length=50)
    site_url = models.URLField("URL")
