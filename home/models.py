from django.db import models

# Create your models here.
class ICategory(models.Model):
    #idc = models.IntegerField()#primary_key=True
    slug = models.TextField(unique = True)
    title = models.CharField(max_length = 200)
    description = models.TextField(blank = True)
    imageUrl = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'media')
    #programs = models.ForeignKey(IProgram,on_delete = models.CASCADE)
    
    
    def __str__(self):
        return self.title
    
    
class IProgram(models.Model):
    #idp = models.IntegerField()
    title = models.CharField(max_length = 200)
    slug = models.TextField(unique = True)
    description = models.TextField(blank = True)
    summary = models.TextField(blank = True)
    #imageUrl = models.CharField(max_length = 200)
    imagUrl = models.ImageField(upload_to = 'media')
    startDate = models.CharField(max_length = 200)
    endDate = models.CharField(max_length = 200)
    time = models.CharField(max_length = 200)
    location = models.CharField(max_length = 200)
    type = models.CharField(max_length = 200)
    noOfSeats = models.IntegerField()
    status = models.CharField(max_length = 200)
    categoryId = models.IntegerField()
    category = models.ForeignKey(ICategory,on_delete = models.CASCADE)
    
    
    def __str__(self):
        return self.title
    
 