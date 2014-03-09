from rest_framework import routers

import accounts.views as acc
import experiences.views as exp

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', acc.UserViewSet)
router.register(r'experiences', exp.ExperienceViewSet)
