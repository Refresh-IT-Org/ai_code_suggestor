from django.db import models

class CodeProject(models.Model):
    name = models.CharField(max_length=100)
    repository_url = models.URLField()

    # Add other relevant fields


class CodeSnippet(models.Model):
    code_project = models.ManyToOneRel(to=CodeProject, field_name="code_snippets")
    filename = models.CharField(max_length=255)
    contents = models.TextField()