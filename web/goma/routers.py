from rest_framework import routers

import accounts.views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', accounts.views.UserViewSet)
