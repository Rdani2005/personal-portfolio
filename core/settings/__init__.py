from .Apps import SECRET_KEY, DEBUG, ALLOWED_HOSTS, INSTALLED_APPS, WSGI_APPLICATION
from .Auth import AUTH_PASSWORD_VALIDATORS, LANGUAGE_CODE, TIME_ZONE, USE_I18N, USE_TZ
from .storage import DATABASES, STATIC_URL, STATICFILES_DIRS, DEFAULT_AUTO_FIELD, MEDIA_URL, MEDIA_ROOT, EMAIL_BACKEND, EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_USE_TLS
from .Middlewares import MIDDLEWARE, ROOT_URLCONF, TEMPLATES

"""
    Importing all the configs from diferent files
   
    Apps File contains all the configs of the django application, including the Allowed Hosts, and Apps that need to be use, and WSGI_APPLICATION config
   
    Auth File contains all the contains all the validations configs of the django application, and the encoded credentials
   
    Storage File contains all the Storage that we are using, and it's configs
   
    Middlewares contains all the middlewares, Root and Templates configs
"""

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
