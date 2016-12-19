from __future__ import unicode_literals

import short_url
from django.db import models


class Link(models.Model):
    url = models.CharField(max_length=2083)
    visits = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.url)

    @property
    def tiny_url(self):
        if self.id:
            return short_url.encode_url(self.id)
        return None


def decode_tiny_url(tiny_url):
    return short_url.decode_url(tiny_url)
