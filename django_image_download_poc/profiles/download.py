import os
from urllib.parse import urlparse
from urllib.request import urlretrieve

from django.core.files import File

from profiles.models import Profile


def download(url):
    path, headers = urlretrieve(url)
    url_path = urlparse(url).path
    original_filename = os.path.basename(url_path)
    file = File(open(path, 'rb'))

    profile = Profile(name='test')
    profile.image.save(
        original_filename,
        file,
    )
    profile.save()
