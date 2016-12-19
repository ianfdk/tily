from django.test import TestCase
from django.urls import reverse

from .models import Link


class IndexViewTests(TestCase):
    def test_static_index(self):
        url = reverse('link_shortener:index')
        with self.assertTemplateUsed('link_shortener/index.html', count=1):
            self.client.get(url)

    def test_post(self):
        url = reverse('link_shortener:index')
        response = self.client.post(url, {'url': 'test.com'})
        self.assertContains(response, 'tiny_url', count=1, status_code=200)

    def test_post_existing_url(self):
        url = reverse('link_shortener:index')
        response1 = self.client.post(url, {'url': 'test.com'}).json()
        response2 = self.client.post(url, {'url': 'test.com'}).json()
        self.assertEqual(response1['tiny_url'], response2['tiny_url'])

    def test_post_no_url(self):
        url = reverse('link_shortener:index')
        response = self.client.post(url)
        self.assertContains(response, 'No "url" param.', count=1,
                            status_code=400)

    def test_redirection(self):
        url = reverse('link_shortener:index')
        response1 = self.client.post(url, {'url': 'test.com'}).json()
        response2 = self.client.get(response1['tiny_url'])
        self.assertEqual(301, response2.status_code)
        self.assertEqual('test.com', response2.url)

        link = Link.objects.get(url='test.com')
        self.assertEqual(1, link.visits)

    def test_redirection_404(self):
        url = reverse('link_shortener:index')
        url_get = '{}abcdef'.format(url)
        response = self.client.get(url_get)
        self.assertEqual(404, response.status_code)


class LinkModelTests(TestCase):
    def test_tiny_url(self):
        link = Link(id=1, url='test.com')
        self.assertEqual('867nv', link.tiny_url)

    def test_unsaved_tiny_url(self):
        link = Link(url='test.com')
        self.assertEqual(None, link.tiny_url)
