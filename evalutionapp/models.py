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
    app_icon = models.ImageField(upload_to= 'app_images/')
    app_image = models.ImageField(upload_to='app_images/')
    app_points = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete= models.SET_NULL, null= True)
    subcategory = models.ForeignKey(SubCategory, on_delete= models.SET_NULL, null= True)
    created_at = models.DateTimeField(auto_now_add= True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.app_name

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)