from django.db import models
from django.core.validators import FileExtensionValidator
from profiles.models import Profile


class Event(models.Model):
    name = models.CharField(max_length=100, blank=False)
    date = models.DateField()
    time = models.TimeField()
    location = models.TextField()
    image = models.ImageField(
        upload_to='images',
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])],
        blank=True
    )
    is_liked = models.ManyToManyField(Profile, blank=False, related_name='likes')

    def __str__(self):
        return str(self.name)

    def num_likes(self):
        return self.is_liked.all().count()


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}-{self.event}-{self.value}"
