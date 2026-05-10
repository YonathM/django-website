import os
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils import timezone

from django.contrib.auth.models import User  # <-- import User here
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
class Department(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    DEPARTMENT_TYPE_CHOICES = (
        ('outcome_based', 'Outcome-Based'),
        ('industry_extension', 'Industry Extension'),
    )

    name = models.CharField(max_length=100)
    department_type = models.CharField(
        max_length=30,
        choices=DEPARTMENT_TYPE_CHOICES,
        default='outcome_based'
    )
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="departments/", blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.name
class Statistic(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=50)
    value = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Statistic"
        verbose_name_plural = "Statistics"

    def __str__(self):
        return self.title
class Testimonial(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
     # Store the user who created this testimonial
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
class Vacancy(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField(blank=True, null=True)  # optional
    published_date = models.DateTimeField(default=timezone.now)
    application_deadline = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    attachment = models.FileField(upload_to='vacancies/', blank=True, null=True)  # optional
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

class TuitionFee(models.Model):
    sector = models.CharField(max_length=100)   # User can write any sector
    occupation = models.CharField(max_length=100)  # e.g., "Doctor", "Teacher"
    fee = models.DecimalField(max_digits=10, decimal_places=2)  # e.g., 2500.00
    created_at = models.DateTimeField(auto_now_add=True)  # auto-store date/time when added

    def __str__(self):
        return f"{self.sector} - {self.occupation} : {self.fee}"
class HeroImage(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="hero_images/")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title or f"Hero Image {self.id}"

class DigitalLibrary(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=255)
    department = models.TextField()
    description = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    attachment = models.FileField(upload_to='vacancies/', blank=True, null=True)  # optional
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

class ProductionUnit(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=255)
    product_type = models.TextField()
    description = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    attachment = models.FileField(upload_to='vacancies/', blank=True, null=True)  # optional
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

class Tender(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField(blank=True, null=True)  # optional
    published_date = models.DateTimeField(default=timezone.now)
    closing_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    attachment = models.FileField(upload_to='vacancies/', blank=True, null=True)  # optional
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title
    
class DeanMessage(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    name =  models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    attachment = models.FileField(upload_to='vacancies/', blank=True, null=True)  # optional
    def __str__(self):
        return self.title or f"Hero Image {self.id}"