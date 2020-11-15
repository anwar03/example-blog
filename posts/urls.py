# from django.urls import path
# from posts.views import posts, post_details
#
# urlpatterns = [
#     path('', posts),
#     path('<int:post_id>', post_details)
# ]

from django.urls import path

from .views import PostsListApiView, PostsDetailsApiView, CommentsListApiView

urlpatterns = [
    path('', PostsListApiView.as_view(), name='posts-list'),
    path('<int:post_id>', PostsDetailsApiView.as_view(), name='post-details'),
    path('<int:post_id>/comments', CommentsListApiView.as_view(), name='comment-list'),
]
