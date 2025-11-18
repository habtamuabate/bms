from django.contrib import admin
from .models import Company, Project, Bid, BidItem

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'email', 'phone', 'created_at']
    search_fields = ['company_name', 'email']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_code', 'project_name', 'client_name', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['project_code', 'project_name', 'client_name']

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ['bid_number', 'bid_name', 'project', 'bid_amount', 'status', 'submission_deadline']
    list_filter = ['status', 'bid_type', 'submission_deadline']
    search_fields = ['bid_number', 'bid_name', 'project__project_name']

@admin.register(BidItem)
class BidItemAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'bid', 'quantity', 'unit_price', 'total_price']
    list_filter = ['bid']
    search_fields = ['item_name', 'bid__bid_name']