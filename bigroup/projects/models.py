from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    copy = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    tags = models.TextField()
    city = models.CharField(max_length=255)
    address = models.TextField()
    desc = models.TextField()
    youtube_url = models.TextField()
    main_img = models.ImageField(upload_to='project_images/', blank=True, null=True)
    panorama_img = models.ImageField(upload_to='project_images/', blank=True, null=True)
    title_content = models.CharField(max_length=255)
    desc_content = models.TextField()
    price = models.CharField(max_length=255)
    apartment_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class CallbackRequest(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заявка от {self.full_name} ({self.phone_number})"