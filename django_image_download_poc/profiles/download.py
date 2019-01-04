import os
from urllib.parse import urlparse
from urllib.request import urlretrieve

from django.core.files import File
from filer.models import Image

from profiles.models import Profile


def download(url):
    path, headers = urlretrieve(url)
    url_path = urlparse(url).path
    original_filename = os.path.basename(url_path)

    with open(path, 'rb') as f:

        file = File(f)

        profile = Profile(name='test')
        profile.image.save(
            original_filename,
            file,
        )
        profile.save()

        image = Image.objects.create(
            original_filename=original_filename,
            file=file,
        )
        image.save()
        profile.filer_image = image
        profile.save()
