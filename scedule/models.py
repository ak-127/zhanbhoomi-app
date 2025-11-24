# Create your models here.
from django.db import models

class TeenagerApplication(models.Model):
    PHOTO_ID_CHOICES = [
        ('aadhar', 'Aadhar Card'),
        ('pan', 'PAN Card'),
        ('passport', 'Passport'),
        ('voter', 'Voter ID'),
    ]

    LANGUAGE_CHOICES = [
        ('hindi', 'Hindi'),
        ('english', 'English'),
        ('marathi', 'Marathi'),
        ('other', 'Other'),
    ]

    PROFICIENCY_CHOICES = [
        ('basic', 'Basic'),
        ('intermediate', 'Intermediate'),
        ('fluent', 'Fluent'),
        ('none','None')
    ]

    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    # Basic Info
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo_id_type = models.CharField(max_length=20, choices=PHOTO_ID_CHOICES)
    id_number = models.IntegerField(max_length=50)
    date_of_birth = models.DateField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50, default='India')
    state = models.CharField(max_length=100)

    # Education Info
    studying_in_class = models.CharField(max_length=50)
    school_college_name = models.CharField(max_length=200)

    # Contact Info
    email = models.EmailField()
    mobile_number = models.IntegerField(max_length=15)
    photo = models.ImageField(upload_to='uploads/photos/', null=True, blank=True)

    # Parent Info
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    parent_mobile_number = models.CharField(max_length=15)
    parent_old_student = models.CharField(max_length=3, choices=YES_NO_CHOICES)

    # Language and Proficiency
    hindi_proficiency = models.CharField(max_length=20, choices=PROFICIENCY_CHOICES)
    english_proficiency = models.CharField(max_length=20, choices=PROFICIENCY_CHOICES)
    preferred_language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)

    # Emergency Contact
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_number = models.CharField(max_length=15)
    emergency_contact_relation = models.CharField(max_length=100)

    # Health & Other Questions
    learnt_other_meditation = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    physical_health_problem = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    mental_health_problem = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    taking_medication = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    friend_or_family_joining = models.CharField(max_length=3, choices=YES_NO_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
