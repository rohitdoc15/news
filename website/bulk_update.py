import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
django.setup()

from pages.models import NewsChannel


news_channels = [
    
]

        



for channel_data in news_channels:
    slug = channel_data['slug']
    channel, created = NewsChannel.objects.get_or_create(slug=slug, defaults=channel_data)
    if not created:
        for key, value in channel_data.items():
            setattr(channel, key, value)
        channel.save()
