from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from article.models import Article

@receiver(pre_save, sender=Article)
def article_pre_save(sender, instance, *args, **kwargs):
    # print("pre_save worlked")
    if instance.slug is None:
        instance.slug = slugify(instance.title)


pre_save.connect(article_pre_save, sender=Article)