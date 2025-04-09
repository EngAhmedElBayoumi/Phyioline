from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import CustomUser , SuplierRequest
# import group model
from django.contrib.auth.models import Group
#import gettext
from django.utils.translation import gettext as _
# Register your models here.

# unregister group model
admin.site.unregister(Group)

@admin.register(CustomUser)
class CustomUserAdmin(ModelAdmin):
    list_display = ["username", "email", "first_name", "last_name", "is_staff"]
    search_fields = ["username", "email", "first_name", "last_name","phone"]
    list_filter = ["is_staff", "is_superuser", "is_active","type"]
    fieldsets = (
        (None, {
            "fields": (_("email"), _("password"), _("type")),
        }),
        (_("Personal info"), {
            "fields": (_("first_name"), _("last_name"), _("username"), _("phone")),
        }),
        (_("Permissions"), {
            "fields": (
                _("is_active"),
                _("is_staff"),
                _("is_superuser"),
                _("groups"),
                _("user_permissions"),
            ),
        }),
        (_("Important dates"), {
            "fields": (_("last_login"), _("date_joined")),
        }),
    )
    
    filter_horizontal = [_("groups"), _("user_permissions")]
    
    
    
@admin.register(Group)
class GroupAdmin(ModelAdmin):
    filter_horizontal=['permissions']


@admin.register(SuplierRequest)
class SuplierRequestAdmin(ModelAdmin):
    list_display = ["user", "status", "created_at", "updated_at"]
    
    list_filter = ["status", "created_at", "updated_at"]
    search_fields = ["user__username", "user__email"]
    
    



