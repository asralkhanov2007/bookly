from django.db import models
from django.utils.text import slugify
from accounts.models import CustomUser

# Create your models here.

class Business(models.Model):
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='business')
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20,blank=True)
    address = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Service(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.business.name}'
    
class Availability(models.Model):
    DAYS = [
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    ]

    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='availability')
    day_of_week = models.IntegerField(choices=DAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)

    class Meta:
        unique_together = ['business', 'day_of_week']
        ordering = ['day_of_week']

    def __str__(self):

        return f'{self.business.name} - {self.get_day_of_week_display()}'