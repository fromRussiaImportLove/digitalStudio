from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from api.views import BudgetStatusViewSet

router = DefaultRouter()
router.register('budget_status', BudgetStatusViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
