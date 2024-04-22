from django.contrib import admin

from .models import Loans

@admin.register(Loans)
class LoanAdmin(admin.ModelAdmin):
    list_display = ['identifier', 'nominal_value', 'interest_rate', 'request_date', 'bank', 'client']
    list_filter = ['request_date']
    search_fields = ['client', 'bank']