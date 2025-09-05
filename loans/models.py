from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Loan(models.Model):
    loan_name = models.CharField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.loan_name

class Payment(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='payments')
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.loan.loan_name