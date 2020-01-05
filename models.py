from django.db import models
from multiselectfield import MultiSelectField

class Services_Data(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_name = models.CharField(max_length=20, unique=True)
    course_duration = models.CharField(max_length=20)
    course_start_date = models.DateField(max_length=20)
    course_start_time = models.TimeField(max_length=20)
    course_trainer_name = models.CharField(max_length=20)
    course_trainer_exp = models.IntegerField()

class feedback_Data(models.Model):
    name = models.CharField(max_length=20)
    rating = models.CharField(max_length=10)
    feedback = models.TextField(max_length=100)
    date = models.DateTimeField(max_length=30)

class Enquiry_Data(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    mobile = models.BigIntegerField()
    gender = models.CharField(max_length=10)
    start_date = models.DateField(max_length=20)
    COUESES_CHOICES = (
        ('py', 'Python'),
        ('dj', 'Django'),
        ('fl', 'Flask'),
    )
    courses = MultiSelectField(max_length=200, choices=COUESES_CHOICES)
    SHIFTS_CHOICES=(
        ('Morning', 'Morning Shigt'),
        ('Afternon', 'Afternon Shigt'),
        ('Evening', 'Evening Shigt')
    )
    shifts = MultiSelectField(choices=SHIFTS_CHOICES)