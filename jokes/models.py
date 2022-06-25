from uuid import uuid4

from django.db import models

class Subscription(models.Model):
    """Represents a user's subscription to the service that sends a random joke 
    from a certain category every day"""
    
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    
    email = models.EmailField(
        unique=True, 
        blank=False, 
        null=False, 
    )
    
    category = models.CharField(max_length=255, blank=False, null=False)
    
    class Meta:
        indexes = [
            models.Index(fields=["email"]),
        ]
        
    def __str__(self) -> str:
        return f'{self.email}-{self.category}'
    
    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        self.category = self.category.lower()
        
        super(Subscription, self).save(*args, **kwargs)
