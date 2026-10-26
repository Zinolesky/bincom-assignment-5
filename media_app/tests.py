import os
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
        self.pdf_file = SimpleUploadedFile(
            name="test_doc.pdf",
            content=b"%PDF-1.4 sample content",
            content_type="application/pdf"
        )
        self.pdf_item = MediaItem.objects.create(
            title="Sample PDF Cheat Sheet",
            description="Testing PDF cheat sheet",
            media_type="pdf",
            category=self.category,
            media_file=self.pdf_file,
        )

    def tearDown(self):
        for item in [self.media_item, self.pdf_item]:
            if item.media_file:
                try:
                    if os.path.exists(item.media_file.path):
                        os.remove(item.media_file.path)
                except Exception:
                    pass

    def test_gallery_view_status_code(self):
        response = self.client.get(reverse('media_gallery'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Tech Image")
        self.assertContains(response, "Sample PDF Cheat Sheet")

    def test_detail_view_increments_views(self):
        initial_views = self.media_item.views_count
        response = self.client.get(reverse('media_detail', args=[self.media_item.pk]))
        self.assertEqual(response.status_code, 200)
        self.media_item.refresh_from_db()
        self.assertEqual(self.media_item.views_count, initial_views + 1)

    def test_filter_by_media_type(self):
        # Filter image
        response = self.client.get(reverse('media_gallery') + '?type=image')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Tech Image")
        self.assertNotContains(response, "Sample PDF Cheat Sheet")

        # Filter pdf
        response_pdf = self.client.get(reverse('media_gallery') + '?type=pdf')
        self.assertEqual(response_pdf.status_code, 200)
        self.assertContains(response_pdf, "Sample PDF Cheat Sheet")
        self.assertNotContains(response_pdf, "Sample Tech Image")

        # Filter video
        response_video = self.client.get(reverse('media_gallery') + '?type=video')
        self.assertEqual(response_video.status_code, 200)
        self.assertNotContains(response_video, "Sample Tech Image")
        self.assertNotContains(response_video, "Sample PDF Cheat Sheet")

    def test_pdf_detail_view_contains_interactive_reader(self):
        response = self.client.get(reverse('media_detail', args=[self.pdf_item.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Interactive PDF Reader")
        self.assertContains(response, "application/pdf")
