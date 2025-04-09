from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import *
# import html formate
from django.utils.html import format_html
# Register your models here.


@admin.register(About)
class AboutAdmin(ModelAdmin):
    list_display = ['name','job_title', 'display_image']



    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        
    # override adding to just add one record not more 
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
    
    
@admin.register(Vission)
class VissionAdmin(admin.ModelAdmin):
    # override adding to just add one record not more
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
    
    def get_description(self, obj):
        return format_html(obj.description)
    get_description.short_description = 'Description'  # Column header name




@admin.register(Mission)
class MissionAdmin(ModelAdmin):
    list_display = ['get_description']


    def get_description(self, obj):
        return format_html(obj.description)
    get_description.short_description = 'Description'  # Column header name


    
    # override adding to just add one record not more
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(Terms_and_condition)
class Terms_and_conditionAdmin(ModelAdmin):
    list_display = ['get_description']


    def get_description(self, obj):
        return format_html(obj.description)
    get_description.short_description = 'Description'  # Column header name


    
    # override adding to just add one record not more
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
    
    
    
@admin.register(refund_and_policy)
class refund_and_policyAdmin(ModelAdmin):
    list_display = ['get_description']


    def get_description(self, obj):
        return format_html(obj.description)
    get_description.short_description = 'Description'  # Column header name


    
    # override adding to just add one record not more
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)