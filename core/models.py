from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Título')
    content = models.TextField(null=True, blank=True, verbose_name='Conteúdo')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Criado em')
    tags = models.ManyToManyField('Tag', related_name='blogs')
    
    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name