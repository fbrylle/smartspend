from django.forms import ModelForm
from .models import Loan, Payment

class LoanForm(ModelForm):
    class Meta:
        model = Loan
        fields = ['loan_name','description', 'created']


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ['loan', 'amount','description']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['loan'].queryset = Loan.objects.filter(user=user)