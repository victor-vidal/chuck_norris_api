from rest_framework import serializers

from jokes.models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    """Subscription objects's serializer"""
    
    class Meta:
        model = Subscription
        fields = [
            'id',
            'email',
            'category'
        ]
        
        read_only_fields = ['id']
        