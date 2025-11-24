from django import forms
from .models import Transaction, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ex: Alimentação'
            })
        }
        labels = {
            'name': 'Categoria'
        }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'amount', 'category', 'transaction_type']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Transaction name'}),
            'amount': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01'}),
            'category': forms.Select(attrs={'class': 'form-input'}),
            'transaction_type': forms.Select(attrs={'class': 'form-input'}),
        }
        labels = {
            'title': 'Title',
            'amount': 'Value',
            'category': 'category',
            'transaction_type': 'Transaction Type',
        }

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError("The amount must be bigger than 0")
        return amount
