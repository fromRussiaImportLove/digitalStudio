from rest_framework import serializers
from api.models import BudgetStatus


class SerializeBuilder(serializers.ModelSerializer):
    def __init__(self, model):
        self.model = model
        super().__init__()

    class Meta:
        fields = '__all__'


class BudgetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetStatus
        fields = '__all__'
