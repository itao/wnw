from rest_framework import routers

import accounts.views
import klasses.views
import students.views
import notes.views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', accounts.views.UserViewSet)
router.register(r'klasses', klasses.views.KlassViewSet)
router.register(r'students', students.views.StudentViewSet)
router.register(r'notes', notes.views.NoteViewSet)
