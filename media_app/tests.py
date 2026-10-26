from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Category, MediaItem


class MediaAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Tech", slug="tech")
        self.sample_file = SimpleUploadedFile(
            name="test_image.png",
            content=b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR",
            content_type="image/png"
        )
        self.media_item = MediaItem.objects.create(
            title="Sample Tech Image",
            description="Testing description",
            media_type="image",
            category=self.category,
            media_file=self.sample_file,
        )

    def test_gallery_view_status_code(self):
        response = self.client.get(reverse('media_gallery'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Tech Image")

    def test_detail_view_increments_views(self):
        initial_views = self.media_item.views_count
        response = self.client.get(reverse('media_detail', args=[self.media_item.pk]))
        self.assertEqual(response.status_code, 200)
        self.media_item.refresh_from_db()
        self.assertEqual(self.media_item.views_count, initial_views + 1)

    def test_filter_by_media_type(self):
        response = self.client.get(reverse('media_gallery') + '?type=image')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Tech Image")

        # Filtering for video should not return the image
        response_video = self.client.get(reverse('media_gallery') + '?type=video')
        self.assertEqual(response_video.status_code, 200)
        self.assertNotContains(response_video, "Sample Tech Image")
