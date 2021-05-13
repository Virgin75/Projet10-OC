from rest_framework import serializers
from issuetracker.models import Project, Issue, Comment
from users.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):

    contributors = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'type', 'contributors')
        depth = 1
