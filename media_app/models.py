from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class MediaItem(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio / Podcast'),
        ('pdf', 'PDF Cheat Sheet'),
    ]

    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='media_items'
    )
    media_file = models.FileField(upload_to='multimedia/%Y/%m/')
    thumbnail = models.ImageField(upload_to='thumbnails/%Y/%m/', blank=True, null=True)
    step_number = models.PositiveIntegerField(default=0, help_text="Order in roadmap sequence (0 for non-roadmap items)")
    views_count = models.PositiveIntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['step_number', '-uploaded_at']

    def __str__(self):
        return f"{self.title} ({self.get_media_type_display()})"
