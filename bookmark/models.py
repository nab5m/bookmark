from django.db import models
from django.urls import reverse_lazy

from accounts.models import UserProfile


class BookmarkList(models.Model):
    list_name = models.CharField("리스트 이름", max_length=50)
    description = models.CharField("설명", max_length=255)

    models.ManyToManyField(UserProfile)
    ACCESS_LEVEL_CHOICES = (
        ('P', '개인'),
        ('S', '공개'),
    )
    access_level = models.CharField(max_length=1, choices=ACCESS_LEVEL_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BookmarkItem(models.Model):
    belonged_list = models.ForeignKey(BookmarkList, on_delete=models.CASCADE)

    site_name = models.CharField("사이트 이름", max_length=50)
    site_url = models.URLField("URL")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.site_name

    def get_absolute_url(self):
        return reverse_lazy('bookmark:detail', args=[self.id])
        # TODO: CBV에서 처리할 수 있는 방법은 없는가 - get_success_url 오버라이딩