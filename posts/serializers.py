from rest_framework import serializers


class PostsSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    userId = serializers.IntegerField(required=True)
    title = serializers.CharField(max_length=500, required=True)
    body = serializers.CharField(max_length=2000, required=True)

    class Meta:
        fields = ['id', 'userId', 'title', 'body']


class CommentsSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    postId = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=500)
    email = serializers.EmailField(max_length=100)
    body = serializers.CharField(max_length=2000)

    class Meta:
        fields = ['id', 'postId', 'email', 'name', 'body']
