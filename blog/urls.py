from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'blog.views.index', name = 'index'),
    url(r'^(?P<pk>\d+)/$', 'blog.views.post_detail', name='post_detail'),
    url(r'^(?P<pk>\d+)/comments/new/$', 'blog.views.comment_new', name='comments_new'),

]