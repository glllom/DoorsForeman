from django.forms import ModelForm, TextInput, ClearableFileInput, SelectMultiple, Select, Textarea

from main.models import *


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = "להסיר תמונה"
    initial_text = "קובץ נוכחי"
    input_text = "שינוי"
    placeholder = "sdfsdfdsf"


class DoorTypeForm(ModelForm):
    error_css_class = "error"

    class Meta:
        model = DoorType
        fields = ['name', 'image', 'height_calculation', 'width_calculation']
        widgets = {'name': TextInput(attrs={'class': 'form-control', 'size': '30'}),
                   'height_calculation': TextInput(attrs={'size': '5', 'class': 'form-control'}),
                   'width_calculation': TextInput(attrs={'size': '5', 'class': 'form-control'}),
                   'image': CustomClearableFileInput(attrs={'class': 'form-control'},),
                   }
        error_messages = {
            'name': {'required': "שדה חובה", 'unique': "דלת עם שם כזה כבר קיימת במערכת"},
            'height_calculation': {'max_value': "מספר חייב להיות שלילי או אפס", 'invalid': "הזן מספר"},
            'width_calculation': {'max_value': "מספר חייב להיות שלילי או אפס", 'invalid': "הזן מספר"},
            'image': {'invalid_image': "קובץ תמונה שגוי"}
        }


class LockForm(ModelForm):
    class Meta:
        model = Lock
        fields = ['name', 'compatible_doors']
        widgets = {'name': TextInput(attrs={'class': 'form-control', 'size': '20'}),
                   'compatible_doors': SelectMultiple(attrs={'class': 'form-select doors-selector'})}
        error_messages = {
            'name': {'required': "שדה חובה", 'unique': "מנעול עם שם כזה כבר קיימת במערכת"},
        }


class HingesForm(ModelForm):
    class Meta:
        model = Hinge
        fields = ['name', 'compatible_doors']
        widgets = {'name': TextInput(attrs={'class': 'form-control', 'size': '20'}),
                   'compatible_doors': SelectMultiple(attrs={'class': 'form-select'})}
        error_messages = {
            'name': {'required': "שדה חובה", 'unique': "צירים עם שם כזה כבר קיימים במערכת"},
        }


class EngravingForm(ModelForm):
    class Meta:
        model = EngravingType
        fields = ['name', 'compatible_doors', 'image']
        widgets = {'name': TextInput(attrs={'class': 'form-control', 'size': '20'}),
                   'compatible_doors': SelectMultiple(attrs={'class': 'form-select'}),
                   'image': CustomClearableFileInput(attrs={'class': 'form-control'})}
        error_messages = {
            'name': {'required': "שדה חובה", 'unique': "חריטה עם שם כזה כבר קיימת במערכת"},
            'image': {'invalid_image': "קובץ תמונה שגוי"}
        }


class StructureForm(ModelForm):
    class Meta:
        model = Structure
        fields = ['description', 'compatible_doors', 'compatible_engraving']
        widgets = {'description': Textarea(attrs={'class': 'form-control', 'style': 'height: 100px;'}),
                   'compatible_doors': SelectMultiple(attrs={'class': 'form-select'}),
                   'compatible_engraving': SelectMultiple(attrs={'class': 'form-select'}),
                   'image': ClearableFileInput(attrs={'class': 'form-control'})}
        error_messages = {
            'description': {'required': "שדה חובה", 'unique': "חריטה עם שם כזה כבר קיימת במערכת"},
            'image': {'invalid_image': "קובץ תמונה שגוי"}
        }


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ('date',)
        widgets = {'id': TextInput(attrs={'class': 'form-control'}),
                   'customer': TextInput(attrs={'class': 'form-control', 'size': '15'}),
                   'phone': TextInput(attrs={'class': 'form-control', 'size': '15'}),
                   'address': TextInput(attrs={'class': 'form-control', 'size': '15'}),
                   'door_type': Select(attrs={'class': 'form-select',}),
                   'lock': Select(attrs={'class': 'form-select'}),
                   'hinges': Select(attrs={'class': 'form-select'}),
                   'engraving': Select(attrs={'class': 'form-select'}),
                   'structure': Select(attrs={'class': 'form-select'}),
                   'casing': Select(attrs={'class': 'form-select'}),
                   'comment': Textarea(attrs={'class': 'form-control', 'style': 'height: 125px;'}),
                   }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['lock'].queryset = Lock.objects.none()
        self.fields['hinges'].queryset = Hinge.objects.none()
        self.fields['engraving'].queryset = EngravingType.objects.none()


class DoorsGroupInstanceForm(ModelForm):
    class Meta:
        model = DoorsGroupInstance
        fields = '__all__'
        exclude = ['order']
        widgets = {'door_type': Select(attrs={'class': 'form-select'}),
                   'lock': Select(attrs={'class': 'form-select'}),
                   'hinges': Select(attrs={'class': 'form-select'}),
                   'engraving': Select(attrs={'class': 'form-select'}),
                   }


class DoorInstanceForm(ModelForm):
    class Meta:
        model = DoorInstance
        fields = '__all__'
        exclude = ['group', 'number']
        widgets = {'quantity': TextInput(attrs={'class': 'form-control px-1 rounded-0'}),
                   'width': TextInput(attrs={'class': 'form-control px-1 rounded-0'}),
                   'height': TextInput(attrs={'class': 'form-control px-1 rounded-0'}),
                   'frame': TextInput(attrs={'class': 'form-control px-1 rounded-0'}),
                   'comment': TextInput(attrs={'class': 'form-control px-2 rounded-0'}),
                   'direction': Select(attrs={'class': 'form-select ps-1 rounded-0'}),
                   }
