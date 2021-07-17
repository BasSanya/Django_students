from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.auth.decorators import login_required
from django.views.i18n import JavaScriptCatalog

from students.views import students, groups, journal, contact_admin, students_class, students_update, \
    students_delete

urlpatterns = [
                  path('jsi18n/', JavaScriptCatalog.as_view(packages=['students']), name='javascript-catalog'),
                  # Students urls
                  path('', students.students_list, name="home"),
                  path('students_list/', students_class.StudentList.as_view()),
                  path('students/add/', students.students_add, name="students_add"),
                  path('student/<int:pk>/edit/', students_update.StudentUpdateView.as_view(), name="students_update"),
                  path('student/<int:pk>/delete/', students_delete.StudentDeleteView.as_view(), name="students_delete"),

                  # Groups urls
                  path('groups/', login_required(groups.groups_list), name="groups"),
                  path('groups/add/', login_required(groups.groups_add), name="groups_add"),
                  path('group/<int:sid>/edit/', login_required(groups.groups_edit), name="groups_edit"),
                  path('group/<int:sid>/delete/', login_required(groups.groups_delete), name="groups_delete"),

                  # Journal url
                  # path('journal/', journal.JournalView.as_view(), name="journal"),
                  re_path(r'journal/(?:(?P<pk>\d+)/)?$', journal.JournalView.as_view(), name="journal"),

                  path('contact-admin/', contact_admin.contact_admin, name="contact_admin"),

                  #  Login
                  path('accounts/', include('allauth.urls')),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
