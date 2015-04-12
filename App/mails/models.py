from django.db import models


class ContactUs(models.Model):
    SUBJECTS = (
        ("GCS", "General Customer Service"),
        ("Suggest", "Suggestions"),
        ("PS", "Product Support"))
    name = models.CharField("NAME", max_length=150)
    subject = models.CharField("SUBJECT", max_length=150, choices=SUBJECTS, null=True, blank=True)
    email = models.EmailField("EMAIL ADDRESS", null=True, blank=True)
    message = models.TextField("MESSAGE", null=True, blank=True)
