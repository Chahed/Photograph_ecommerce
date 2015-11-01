from django.db import models
from django.contrib.auth.models import User

class home_image(models.Model):
    titre = models.CharField(max_length=30,unique=True)
    texte = models.TextField(null=True)
    image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')



    def __str__(self):
        return self.titre

class film(models.Model):
    titre = models.CharField(max_length=30,unique=True)
    texte = models.TextField(null=True)
    image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    url = models.URLField(default=0)



    def __str__(self):
        return self.titre



class projet(models.Model):

    titre = models.CharField(max_length=30,unique=True)
    image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')

    def __str__(self):
        return self.titre

class realisation(models.Model):

    titre = models.CharField(max_length=30,unique=True)
    texte = models.TextField(null=True)
    image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    projet= models.CharField(max_length=30,unique=False)




    def __str__(self):
        return self.projet

class cv(models.Model):

    file = models.FileField(upload_to ='files/',blank=True)



class commissioned_work(models.Model):

    titre = models.CharField(max_length=30,unique=True)
    image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')

    def __str__(self):
        return self.titre

class shop(models.Model):
    titre = models.CharField(max_length=30,unique=True)
    texte = models.TextField(null=True)
    image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    year = models.IntegerField(null=True)
    prix= models.IntegerField()



    def __str__(self):
        return self.titre


class client(models.Model):
    FIRST_NAME =  models.CharField(max_length=30)
    LAST_NAME = models.CharField(max_length=30)
    ADDRESS_LINE_1 = models.CharField(max_length=30)
    ADDRESS_LINE_2 =models.CharField(max_length=30)
    TOWN_CITY = models.CharField(max_length=30)
    REGION_STATE=models.CharField(max_length=30)
    COUNTRY= models.CharField(max_length=30)
    POST_CODE = models.IntegerField()
    EMAIL_ADRESS= models.EmailField()
    PHONE_NUMBER= models.IntegerField()

    def __str__(self):
        return self.FIRST_NAME
