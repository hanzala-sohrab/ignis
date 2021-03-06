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
    is_liked = models.ManyToManyField(Profile, blank=False, default=False, related_name='likes')

    def __str__(self):
        return self.name


class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    value = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}-{self.event}-{self.value}"
