from django.db import models
from django.contrib.auth.models import User
#model is special kind of object or class about our required data

# ----------------------------- Expenses Models -----------------------------

class Expense(models.Model):
    #Expense model
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Housing', 'Housing'),
        ('Transportation', 'Transportation'),
        ('Utilities', 'Utilities'),
        ('Healthcare', 'Healthcare'),
        ('Entertainment', 'Entertainment'),
        ('Education', 'Education'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    date = models.DateField()
    paid_by = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class Budget(models.Model):
    #Budget model(month specific)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    year = models.IntegerField()
    month = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('user', 'year', 'month')

    def __str__(self):
        return f"{self.user.username} - {self.month}/{self.year} Budget"


# ----------------------------- TO DO LIST model -----------------------------

from django.db import models
from django.contrib.auth.models import User

PRIORITY_CHOICES = (
    ('high', 'High'),
    ('medium', 'Medium'),
    ('low', 'Low'),
)

STATUS_CHOICES = (
    ('todo', 'To Do'),
    ('progress', 'In Progress'),
)

class Task(models.Model):
    #task model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='todo')
    member = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
# ----------------------------- Notes Model -----------------------------

class Note(models.Model):
    COLOR_CHOICES = [
        ('default', 'Default'),
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('yellow', 'Yellow'),
        ('green', 'Green'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    pinned = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='default')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pinned', '-updated_at']

    def __str__(self):
        return self.title
    

# ----------------------------- Calendar model -----------------------------

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class CalendarEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField(default=timezone.now())
    reminder = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=20, default="#6c63ff")

    def __str__(self):
        return self.title
    
# ----------------------------- Inventory Model -----------------------------

from django.db import models
from django.contrib.auth.models import User

class InventoryItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name