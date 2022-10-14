# ----------------------- Libraries and Modules --------------------
# Django: http://docs.djangoproject.com/
from django.conf import settings 
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

"""
    URLS FOR The project
    1. Admin site
    2. Projects and home pages
    3. Contact page
"""
urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('', include('projects.urls', namespace='projects')),
    path('contact/', include('contact.urls', namespace='contact')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

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