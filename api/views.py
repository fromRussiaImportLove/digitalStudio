from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from api.serializers import BudgetStatusSerializer
from api.models import BudgetStatus, GlavBudgetClass


class BudgetStatusViewSet(viewsets.ModelViewSet):
    queryset = BudgetStatus.objects.all()
    serializer_class = BudgetStatusSerializer