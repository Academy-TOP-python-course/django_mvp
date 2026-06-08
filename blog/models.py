from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='articles', blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-published_date']
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'


# class User(models.Model):
#     profile = models.OneToOneField("UserProfile", on_delete=models.CASCADE, related_name='user')
#     mail = models.TextField(blank=True)
#     articles = models.OneToOneField("Article", on_delete=models.CASCADE, related_name='author')
#
#
# class UserProfile(models.Model):
#     user = models.OneToOneField("User", on_delete=models.CASCADE, related_name='profile')
#     bio = models.TextField(blank=True)
#     birth_date = models.DateField(null=True, blank=True)
#     avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
#
# class Tag(models.Model):
#     name = models.CharField(max_length=50, unique=True)
#     slug = models.SlugField(unique=True)
#     articles = models.ManyToManyField("Article", related_name='tags', blank=True)
#
#     def __str__(self):
#         return self.name
