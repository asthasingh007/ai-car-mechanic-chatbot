from django.db import models


class ChatMessage(models.Model):
    message = models.TextField()
    sender = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


class Diagnosis(models.Model):
    problem = models.TextField()
    diagnosis = models.TextField()
    recommendation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    car_model = models.CharField(max_length=100)
    issue = models.TextField()
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    status = models.CharField(max_length=20, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)


class MediaUpload(models.Model):
    file = models.FileField(upload_to="uploads/")
    media_type = models.CharField(max_length=20)
    uploaded_at = models.DateTimeField(auto_now_add=True)