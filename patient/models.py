from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=10)
    gender = models.CharField(max_length=10, null=True)
    mobile = models.CharField(max_length=15, null=True)  # Assuming mobile number can include characters
    address = models.TextField(null=True)
    detail = models.TextField(null=True)
    medicine_detail = models.TextField(null=True)
    note = models.TextField(null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    next_visit = models.IntegerField(default=0)
    added_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
