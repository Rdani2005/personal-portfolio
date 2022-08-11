from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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
