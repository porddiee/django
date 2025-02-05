from django.contrib import admin
from .models import User, BorrowRecord
# Register your models here.

admin.site.register(User)
admin.site.register(BorrowRecord)