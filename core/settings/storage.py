# ------------ Libraries --------------------
import os
from pathlib import Path
import dj_database_url
# Base Dir of the entire project
BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'sample123',
            'USER': 'rdani2005',
            'PASSWORD': 'Seque1505',
            'HOST': 'localhost',
            'PORT': '',
        }
}

# Static files URL (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Static files (CSS, JavaScript, Images)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
# DB Models config
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Using Gmail with DJango
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_HOST_USER = 'rdani2005dev@gmail.com'

EMAIL_HOST_PASSWORD = 'fcuelvfeyfkbyybo'

EMAIL_USE_TLS = True

# Media Files
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": "dgb2lhvj4", 
    "API_KEY": "595827643384846", 
    "API_SECRET": "IJXsJ9FtVsQvzbm3xBHczEV0jUs" 
}


DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

"""
MIT License

Copyright (c) 2022 Daniel Ricardo Sequeira Campos

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""