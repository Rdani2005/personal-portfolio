# ----------------------- Libraries --------------------
# Django: http://docs.djangoproject.com/
from django.db import models # used for create DB Models
from django.urls import reverse # 
from django.contrib.auth.models import User
# -------------------------- DB Models ------------------------
class ProjectManager(models.Manager):
    def get_queryset(self):
        return super(ProjectManager, self).get_queryset().filter(is_active=True)

"""
    Model to define the diferent categories from the projects 
    that we are updating.
"""
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
    
    # Return absolute url
    def get_absolute_url(self):
        return reverse('project:category_list', args=[self.slug])

    # Return the name of the category
    def __str__(self):
        return self.name  


"""
    Model to uplod the diferent projects tht we've worked on.
"""
class Project(models.Model):
    category = models.ForeignKey(Category, related_name='project', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project_creator")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    code_link = models.URLField(blank=True)
    view_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='images', default='images/default.png')
    slug = models.SlugField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    objects = models.Manager()
    projects = ProjectManager()

    # Extra instructions
    class Meta:
        verbose_name_plural = 'Projects'
        ordering = ('-created',)

    #Return the URL
    def get_absolute_url(self):
        return reverse('project:project_detail', args=[self.slug])
    # Return the title of the project, in case of needing it
    def __str__(self):
        return self.title

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