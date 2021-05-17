
from rest_framework import serializers
import uuid

from issuetracker.models import Contributor, Project, Issue, Comment
from users.models import User
from users.serializers import UserSerializer


class ContributorSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Contributor
        fields = ('user', 'role')


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'type')
