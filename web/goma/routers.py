from rest_framework import routers

import accounts.views
import klasses.api_views as klasses_views
import students.api_views as students_views
import notes.api_views as notes_views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', accounts.views.UserViewSet)
router.register(r'klasses', klasses_views.KlassViewSet)
router.register(r'students', students_views.StudentViewSet)
router.register(r'notes', notes_views.NoteViewSet)
