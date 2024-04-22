from django.contrib import admin

from .models import  Payments

@admin.register(Payments)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['loan', 'payment_date', 'payment_value']
    list_filter = ['payment_date']
    search_fields = ['loan__client']