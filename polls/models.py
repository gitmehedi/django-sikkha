from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    title = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['votes']



class Person(models.Model):
    name = models.CharField(max_length=128)
    # age = models.IntegerField(default=2)


    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person,through="Membership")

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_person = models.CharField(max_length=64)

    def __str__(self):
        return self.invite_person
