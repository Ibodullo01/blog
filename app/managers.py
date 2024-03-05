from django.db import models


class BlogManager(models.Manager):

    # def get_queryset(self):
    #     return super().get_queryset().filter(is_published=True)

    def published(self):
        return self.get_queryset().filter(is_published=True)