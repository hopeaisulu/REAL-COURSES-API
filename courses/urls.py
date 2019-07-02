from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from courses import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api-auth/', include ('rest_framework.urls', namespace='rest_framework')),
    url(r'^courses/$', views.CourseApiViews.as_view(), name='create'),
    url(r'^courses/(?P<pk>[0-9]+)/$', views.CourseDetail.as_view(), name='details'),
    url(r'^category/$', views.CategoryApiViews.as_view(), name='category'),

#path('courses/<int:pk>/', views.courses_detail),
]