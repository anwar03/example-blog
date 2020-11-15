import time

import requests
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import PostsSerializer, CommentsSerializer
from .paginations import StandardPagination


class PostsListApiView(ListAPIView):
    serializer_class = PostsSerializer
    permission_classes = (AllowAny,)
    pagination_class = StandardPagination

    def get_queryset(self):
        url = "https://jsonplaceholder.typicode.com/posts"
        data = get_external_api_data(self, url=url)
        return data


class PostsDetailsApiView(RetrieveAPIView):
    serializer_class = PostsSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'post_id'

    def get_object(self):
        url = "https://jsonplaceholder.typicode.com/posts/{}".format(str(self.kwargs.get('post_id')))
        data = get_external_api_data(self, url=url)
        return data


class CommentsListApiView(ListAPIView):
    serializer_class = CommentsSerializer
    permission_classes = (AllowAny,)
    pagination_class = StandardPagination

    def get_queryset(self):
        url = "https://jsonplaceholder.typicode.com/posts/{}/comments".format(str(self.kwargs.get('post_id')))
        data = get_external_api_data(self, url=url)
        return data


def get_external_api_data(self, url=None):

    max_tries = 5
    if self.request.method == "GET":
        attempt_num = 0
        while attempt_num < max_tries:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                data = r.json()
                return data
            else:
                attempt_num += 1
                time.sleep(5)
        return Response({"error": "Request failed"}, status=r.status_code)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)


# # POSTS VIEW ENDPOINT
# def posts(request):
#     return render(request, 'blog-listing.html')
#
#
# # POST DETAILS VIEW ENDPOINT
# def post_details(request):
#     return render(request, 'blog-post.html')
