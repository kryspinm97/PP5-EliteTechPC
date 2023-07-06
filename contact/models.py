from django.db import models

# Create your models here.


class ContactUs(models.Model):

    """ Model type for contact form / messages """

    class Meta:
        verbose_name_plural = 'Contact Us'

    CATEGORY_CHOICES = [
        ('Technical', 'Technical'),
        ('General Inquiry', 'General Inquiry'),
        ('Feedback', 'Feedback'),
        ('Other', 'Other'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='General Inquiry', null=False, blank=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
