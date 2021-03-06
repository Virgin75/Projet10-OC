from django.db import models
from django.conf import settings
from users.models import User
import uuid


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    type = models.CharField(max_length=50)
    author_user_id = models.ForeignKey(User, null=True,
                                       on_delete=models.CASCADE)
    contributors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='Contributor',
        related_name='contributor_user',
        related_query_name='contributor_user')


class Contributor(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)


class Issue(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    tag = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)
    project_id = models.ForeignKey(
        Project,
        on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='%(class)s_issue_author')
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='%(class)s_issue_assignee')
    created_time = models.DateTimeField()


class Comment(models.Model):
    description = models.CharField(max_length=500)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    issue = models.ForeignKey(
        Issue,
        on_delete=models.CASCADE)
    created_time = models.DateTimeField()
