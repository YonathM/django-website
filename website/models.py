import os
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Function to generate unique image paths
def news_image_path(instance, filename):
    """
    File will be uploaded to MEDIA_ROOT/news_images/<slug>-<timestamp>.<ext>
    """
    base, ext = os.path.splitext(filename)
    timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
    slug = slugify(instance.title)
    new_filename = f"{slug}-{timestamp}{ext}"
    return f"news_images/{new_filename}"
# Function to generate unique video paths
def news_video_path(instance, filename):
    base, ext = os.path.splitext(filename)
    timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
    slug = slugify(instance.title)
    return f"news_videos/{slug}-{timestamp}{ext}"

# News model
class News(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to=news_image_path, blank=True, null=True)  # Updated line
    video = models.FileField(upload_to=news_video_path, blank=True, null=True)  # Added video field
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title