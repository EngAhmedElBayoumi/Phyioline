from django.db import models
from django.contrib.auth.models import User , AbstractUser
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
# Create your models here.

# override User model to login with email

# type choice
TYPE_CHOICES = (
    ('admin', _('admin')),
    ('suplier', _('suplier')),
    ('client', _('client')),
)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True,verbose_name=_("Email"))
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    # type admin or suplier or client
    type = models.CharField(max_length=10, default='client', choices=TYPE_CHOICES,verbose_name=_("Type"))
    phone=models.CharField(max_length=15,blank=True,null=True,verbose_name=_("Phone"))
    def __str__(self):
        return self.email
    
    # verpose name
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

# status choice
STATUS_CHOICES = (
    ('pending', _('pending')),
    ('approved', _('approved')),
    ('rejected', _('rejected')),
)

# suplier request to be suplier
class SuplierRequest(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,verbose_name=_("User"))
    status = models.CharField(max_length=10, default='pending', choices=STATUS_CHOICES,verbose_name=_("Status"))
    resoan = models.TextField(blank=True, null=True,verbose_name=_("Resoan"))
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True,verbose_name=_("Updated At"))
    # files 
    account_statement = models.FileField(upload_to='suplier_request/account_statement', blank=True, null=True,verbose_name=_("Account Statement"))
    commercial_register = models.FileField(upload_to='suplier_request/commercial_register', blank=True, null=True,verbose_name=_("Commercial Register"))
    tax_card = models.FileField(upload_to='suplier_request/tax_card', blank=True, null=True,verbose_name=_("Tax Card"))
    id_card = models.FileField(upload_to='suplier_request/id_card', blank=True, null=True,verbose_name=_("ID Card"))
    
    def __str__(self):
        return self.user.email


    def save(self, *args, **kwargs):
        """
        When status is changed to 'approved', assign permissions to the user.
        """
        if self.pk:  # Ensure object exists before checking previous status
            try:
                old_instance = SuplierRequest.objects.get(pk=self.pk)
                if old_instance.status != 'approved' and self.status == 'approved':  
                    self.assign_permissions()
            except ObjectDoesNotExist:
                pass  # If the object doesn't exist, proceed normally

        super().save(*args, **kwargs)

    def assign_permissions(self):
        from product.models import Product, Card, Order, Wishlist, Category, OrderItem, Review

        """Grant the user full CRUD permissions for specific models when approved."""
        models = [Product, Card, Order, Wishlist, Category, OrderItem, Review]
        for model in models:
            content_type = ContentType.objects.get_for_model(model)
            permissions = Permission.objects.filter(content_type=content_type)
            self.user.user_permissions.add(*permissions)

        # Ensure user is staff after approval
        self.user.is_staff = True
        self.user.save()
        

    class Meta:
        verbose_name = _("Suplier Request")
        verbose_name_plural = _("Suplier Requests")
    