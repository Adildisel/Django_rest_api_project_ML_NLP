from rest_framework import serializers

from django.contrib.auth.models import User

from .models import (
                        ParserVideoId,
                        ParserComments,
                    )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id", 
            "username", 
            "email",
            )


class ParserCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParserComments
        fields = (
            'video',
            # 'auth_comment', 
            # 'date_comment', 
            'comment',
            'assessment',
            )

class VideoIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParserVideoId
        fields = (
            'id',
            'creater',
            'video_id',
            'name_video',
        )

class VideoUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParserVideoId
        fields = (
            'video_id',
        )