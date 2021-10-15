from django import forms
from employee.models import Employee,Department


class EmployeeForms(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'

class EditForm(forms.ModelForm):
    id = forms.IntegerField(label='Edit object with following ID')
"""
class DepartmentForms(forms.ModelForm):
    class Meta:
        model=Department
        fields='__all__'
"""