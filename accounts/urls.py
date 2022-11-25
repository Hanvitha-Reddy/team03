from django.urls import re_path
from accounts import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'accounts'
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'register/$', views.register, name='register'),
    re_path(r'login/$', views.login_user, name='login'),
    re_path(r'home/$', views.home, name='home'),
    re_path(r'home_t/$', views.home_t, name='home_t'),
    re_path(r'logout/$', views.logout_user, name='logout'),
    re_path(r'upload/$', views.upload_book,  name='upload_book'),
    re_path(r'upload_t/$', views.upload_book_t,  name='upload_book_t'),
    re_path(r'assigns251/$', views.assigns_251,  name='assigns_251'),
    re_path(r'assigns215/$', views.assigns_215,  name='assigns_215'),
    re_path(r'assigns293/$', views.assigns_293,  name='assigns_293'),
    re_path(r'course_251/$', views.course_251, name='251'),
    re_path(r'course_293/$', views.course_293, name='293'),
    re_path(r'course_215/$', views.course_215, name='215'),
    re_path(r'profile/$', views.profile, name='profile'),
    re_path(r'course/$', views.course, name='course'),
    re_path(r'assignments/$', views.assignments, name='assignments'),
    re_path(r'assignments_s/$', views.assignments, name='assignments_s'),
    re_path(r'vsc/$', views.vsc, name='vsc'),
    re_path(r'new_upload/$', views.new_upload, name='new_upload'),
    re_path(r'new_upload_t/$', views.new_upload_t, name='new_upload_t'),
    re_path(r'view/$', views.view, name='view'),
    re_path(r'courseview/$', views.courseview, name='courseview'),
    re_path(r'grade/(?P<course>.*)$', views.grade, name='grade'),
    re_path(r'submissions/$', views.submissions, name='submissions'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)