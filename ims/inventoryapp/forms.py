from django import forms
from .models import Stock,Sales
import django_filters

class StockCreateForm(forms.ModelForm):
   class Meta:
     model = Stock
     fields = ['category', 'item_name', 'quantity','price']

   def clean_category(self):
       category = self.cleaned_data.get('category')
       if not category:
           raise forms.ValidationError('This field is required')
       return category

   def clean_item_name(self):
       item_name = self.cleaned_data.get('item_name')
       for instance in Stock.objects.all():
           if instance.item_name == item_name:
               raise forms.ValidationError(str(item_name) + ' is already created')

       return item_name




class IssueForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['issue_by','issue_quantity','phone_number','price_per_product']

class ReceiveForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['receive_by','receive_quantity']

class StockSearchForm(forms.ModelForm):
   class Meta:
       model = Stock
       fields = ['category', 'item_name']

class StockUpdateForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['category', 'item_name', 'quantity','reorder_level']