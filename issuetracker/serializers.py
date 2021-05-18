
from rest_framework import serializers
import uuid

from issuetracker.models import Contributor, Project, Issue, Comment
from users.models import User
from users.serializers import UserSerializer


class ContributorListSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Contributor
        fields = ('user', 'role')


class ContributorDetailsSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Contributor
        fields = ('user', 'role')


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'type')


class IssueListSerializer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField()
    author = UserSerializer(read_only=True)
    assignee = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    created_time = serializers.ReadOnlyField()

    class Meta:
        model = Issue
        fields = ('id', 'title', 'description', 'tag', 'priority',
                  'status', 'author', 'assignee', 'created_time')


class CommentSerializer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField()
    author = UserSerializer(read_only=True)
    created_time = serializers.ReadOnlyField()
    issue = serializers.PrimaryKeyRelatedField(queryset=Issue.objects.all())

    class Meta:
        model = Comment
        fields = ('id', 'description', 'author', 'issue', 'created_time')
