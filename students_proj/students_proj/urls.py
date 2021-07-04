from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from students.views import students, groups, journal

urlpatterns = [
    # Students urls
    path('', students.students_list, name="home"),
    path('students/add/', students.students_add, name="students_add"),
    path('student/<int:sid>/edit/', students.students_edit, name="students_edit"),
    path('student/<int:sid>/delete/', students.students_delete, name="students_delete"),

    # Groups urls
    path('groups/', groups.groups_list, name="groups"),
    path('groups/add/', groups.groups_add, name="groups_add"),
    path('group/<int:sid>/edit/', groups.groups_edit, name="groups_edit"),
    path('group/<int:sid>/delete/', groups.groups_delete, name="groups_delete"),

    # Journal url
    path('journal/', journal.journal, name="journal"),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
