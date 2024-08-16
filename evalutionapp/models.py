from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250, unique= True)
    created_at = models.DateTimeField(auto_now_add= True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    subcategory = models.CharField(max_length= 250, unique= True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.subcategory

class App(models.Model):
    app_name = models.CharField(max_length=250)
    app_link = models.TextField()
    app_image = models.ImageField(upload_to='media/app_images/')
    category = models.ForeignKey(Category, on_delete= models.SET_NULL, null= True)
    subcategory = models.ForeignKey(SubCategory, on_delete= models.SET_NULL, null= True)
    created_at = models.DateTimeField(auto_now_add= True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.app_name

class AppPoint(models.Model):
    points = models.IntegerField()
    app_name = models.ForeignKey(App, on_delete= models.CASCADE,unique= True)
    created_at = models.DateTimeField(auto_now_add= True)
    update_at = models.DateTimeField(auto_now= True)

    def __str_(self):
        return self.points
