from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator,MaxValueValidator

#必要なモデルを決める
#コーヒーの種類のクラス
class Coffee(models.Model):
    name = models.CharField(max_length=30) #コーヒー名
    company = models.CharField(max_length=30) #製作会社
    smell = models.IntegerField(validators=[ \
                MinValueValidator(1), \
                MaxValueValidator(5)]) #香り
    acidity = models.IntegerField(validators=[ \
                MinValueValidator(1), \
                MaxValueValidator(5)]) #酸味
    taste = models.IntegerField(validators=[ \
                MinValueValidator(1), \
                MaxValueValidator(5)]) #コク
    bitter = models.IntegerField(validators=[ \
                MinValueValidator(1), \
                MaxValueValidator(5)]) #苦味
    flavor = models.IntegerField(validators=[ \
                MinValueValidator(1), \
                MaxValueValidator(5)]) #風味

    def __str__(self):
        return str(self.name) + ":(" + str(self.id) + ")"


#入力欄種類のクラス
class Entry(models.Model):
    entry_date = models.DateField() #入力日時
    make = models.CharField(max_length=30,null=True) #製作会社
    coffee = models.CharField(max_length=30,null=True) #コーヒー名
    evaluation = models.IntegerField(validators=[ \
                MinValueValidator(1), \
                MaxValueValidator(5)])

    def __str__(self):
        return str(self.id)


#問い合わせフォームのクラス
class Query(models.Model):
    mail = models.EmailField(max_length=200)
    query = models.TextField(max_length=500)
    query_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.query_date) + ', (' + str(self.mail) + ')'