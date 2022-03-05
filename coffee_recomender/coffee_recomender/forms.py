from django.forms import Form, CharField,DateField, \
    IntegerField,ChoiceField,RadioSelect,ModelForm, \
    EmailField,DateTimeField,Textarea
from django.core.validators import MinValueValidator,MaxValueValidator
from .models import Coffee
from django.utils import timezone

class InputForm(Form):
    entry_date = DateField() #入力日時
    make = CharField(max_length=30) #製作会社
    coffee = CharField(max_length=30) #コーヒー名
    evaluation = IntegerField(min_value=1,max_value=5)

class RegistrationForm(Form):
    data =[
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    ]

    name = CharField(label='コーヒー名',max_length=30) #コーヒー名
    company = CharField(label='製作会社',max_length=30) #製作会社
    smell = ChoiceField(label='香り',choices=data,widget=RadioSelect())
    acidity = ChoiceField(label='酸味',choices=data,widget=RadioSelect())
    taste = ChoiceField(label='コク',choices=data,widget=RadioSelect())
    bitter = ChoiceField(label='苦味',choices=data,widget=RadioSelect())
    flavor = ChoiceField(label='風味',choices=data,widget=RadioSelect())

class AccessForm(ModelForm):
    class Meta:
        model = Coffee
        fields = ['name','company','smell','acidity','taste','bitter','flavor']

class QueryForm(Form):
    mail = EmailField(max_length=200)
    query = CharField(max_length=500,widget=Textarea(attrs={'rows': 5, 'cols': 40}))
    #query_date = DateTimeField(default=timezone.now)