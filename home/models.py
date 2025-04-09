from django.db import models
from ckeditor.fields import RichTextField
# import gettext_lazy as _
from django.utils.translation import gettext_lazy as _


# Create your models here.

class About(models.Model):
    name=models.CharField(max_length=100,verbose_name=_("Name"))
    name_ar=models.CharField(max_length=100,verbose_name=_("Name Arabic"))
    image=models.FileField(upload_to="about/",verbose_name=_("Image"))
    job_title=models.CharField(max_length=100,verbose_name=_("Job Title"))
    job_title_ar=models.CharField(max_length=100,verbose_name=_("Job Title Arabic"))
    description=RichTextField(verbose_name=_("Description"))
    description_ar=RichTextField(verbose_name=_("Description Arabic"))
    
    def __str__(self):
        return self.name
    
    
    # verpose name
    class Meta:
        verbose_name = _("About")
        verbose_name_plural = _("About")
    
    
class Vission(models.Model):
    description=RichTextField(verbose_name=_("Description"))
    description_ar=RichTextField(verbose_name=_("Description Arabic"))
    
    def __str__(self):
        return self.description
    
    # verpose name
    class Meta:
        verbose_name = _("Vission")
        verbose_name_plural = _("Vission")
    
class Mission(models.Model):
    description=RichTextField(verbose_name=_("Description"))
    description_ar=RichTextField(verbose_name=_("Description Arabic"))
    
    
    def __str__(self):
        return self.description
    
    # verpose name
    class Meta:
        verbose_name = _("Mission")
        verbose_name_plural = _("Mission")
    
    
class Terms_and_condition(models.Model):
    description=RichTextField(verbose_name=_("Description"))
    description_ar=RichTextField(verbose_name=_("Description Arabic"))

    
    def __str__(self):
        return self.description
    
    # verpose name
    class Meta:
        verbose_name = _("Terms and condition")
        verbose_name_plural = _("Terms and condition")
    
class refund_and_policy(models.Model):
    description=RichTextField(verbose_name=_("Description"))
    description_ar=RichTextField(verbose_name=_("Description Arabic"))
    
    
    def __str__(self):
        return self.description
    
    # verpose name
    class Meta:
        verbose_name = _("Refund and policy")
        verbose_name_plural = _("Refund and policy")
    
    
