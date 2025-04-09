from django.contrib import admin
from .models import *
from unfold.admin import ModelAdmin , TabularInline
from django.utils.html import format_html
from PIL import Image
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm

# Register your models here.


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name','name_ar')
    fields= ('name','name_ar')
    exclude = ('suplier',)
    
    # permission
    def get_queryset(self, request):
        """Restrict suppliers to only see their own products."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:  # Superusers see all products
            return qs
        return qs.filter(suplier=request.user)
    
    # save 
    def save_model(self, request, obj, form, change):
        """Set the supplier to the logged-in admin user if not already set."""
        if not obj.suplier:  # Ensure supplier is only set when it's empty
            obj.suplier = request.user
        obj.save()
    
    
    
    
@admin.register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'name_ar')
    fields = ('name', 'name_ar')
    
    

@admin.register(ProductImage)
class ImageAdmin(ModelAdmin):  # Use admin.ModelAdmin instead of ModelAdmin
    list_display = ('display_image',)

    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" /><br>{}'.format(obj.image.url, obj.image.name.split('/')[-1]))
    
    display_image.short_description = 'Image'
    

    
@admin.register(Product)
class ProductAdmin(ModelAdmin,ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    export_form_class = SelectableFieldsExportForm
    
    
    list_display = ('title', 'display_main_image', 'price', 'discount', 'label', 'category', 'created_at', 'updated_at', 'rate', 'SKU')
    search_fields = ('title', 'category__name', 'tags__name')
    list_filter = ('category', 'tags', 'label')
    filter_horizontal = ('tags', 'images')  # Add images here
    list_editable = ('discount', 'label')
    
    def display_main_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />'.format(obj.main_image.url))
    
    display_main_image.short_description = 'Main Image'
    
    
    exclude = ('title_en', 'description_en', 'label_en',"slug","suplier")

    def save_model(self, request, obj, form, change):
        """Set the supplier to the logged-in admin user if not already set."""
        if not obj.suplier:  # Ensure supplier is only set when it's empty
            obj.suplier = request.user
        obj.save()
    
    # permission
    def get_queryset(self, request):
        """Restrict suppliers to only see their own products."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:  # Superusers see all products
            return qs
        return qs.filter(suplier=request.user)
    


    
    
@admin.register(Review)
class ReviewAdmin(ModelAdmin):
    list_display = ('name', 'email', 'review', 'rate', 'product')
    search_fields = ('name', 'email', 'product__title')
    list_filter = ('rate', 'product')
    
    exclude = ('review_en',)  

    # permission
    def get_queryset(self, request):
        """Restrict suppliers to only see their own products."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:  # Superusers see all products
            return qs
        return qs.filter(product__suplier=request.user)
    
    
    
@admin.register(Card)
class CardAdmin(ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_at', 'updated_at', 'coupon', 'total_price', 'total_price_after_discount')
    search_fields = ('user__username', 'product__title')
    list_filter = ('coupon', 'product')
    
    # permission
    def get_queryset(self, request):
        """Restrict suppliers to only see their own products."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:  # Superusers see all products
            return qs
        return qs.filter(product__suplier=request.user)
    
        

@admin.register(Wishlist)
class WishlistAdmin(ModelAdmin):
    list_display = ('user', 'product', 'created_at')
    search_fields = ('user__username', 'product__title')
    list_filter = ('product',)
    
    # permission
    def get_queryset(self, request):
        """Restrict suppliers to only see their own products."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:  # Superusers see all products
            return qs
        return qs.filter(product__suplier=request.user)
    
    
    
class OrderItemInline(TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("product_image", "product", "quantity", "total_price")
    
    def product_image(self, obj):
        """Display product image in the admin panel."""
        if obj.product.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:5px;"/>', obj.product.image.url)
        return "No Image"
    
    product_image.short_description = "Product Image"

class OrderAdmin(ModelAdmin):
    list_display = ("user", "formatted_total", "status", "created_at", "transaction_id")
    list_filter = ("status", "created_at")
    search_fields = ("user__username", "transaction_id")
    readonly_fields = ("user", "total_price", "transaction_id", "created_at", "updated_at", "formatted_items")
    inlines = [OrderItemInline]

    def formatted_total(self, obj):
        """Format the total price properly before passing it to format_html."""
        return format_html('<b style="color: green;">${}</b>', "{:.2f}".format(obj.total_price))

    formatted_total.short_description = "Total Price"

    def formatted_items(self, obj):
        """Show order items inside the admin panel with proper formatting."""
        items_html = "<table style='border-collapse: collapse; width: 100%;'>"
        items_html += "<tr style='background:#f8f8f8;'><th style='padding: 8px; border: 1px solid #ddd;'>Image</th><th style='padding: 8px; border: 1px solid #ddd;'>Product</th><th style='padding: 8px; border: 1px solid #ddd;'>Quantity</th><th style='padding: 8px; border: 1px solid #ddd;'>Total</th></tr>"
        
        for item in obj.orderitem_set.all():
            image_html = f'<img src="{item.product.image.url}" width="50" height="50" style="border-radius:5px;">' if item.product.image else "No Image"
            formatted_price = "{:.2f}".format(item.total_price)  # Properly format the price
            
            items_html += f"<tr><td style='padding: 8px; border: 1px solid #ddd; text-align: center;'>{image_html}</td>"
            items_html += f"<td style='padding: 8px; border: 1px solid #ddd;'>{item.product.title}</td>"
            items_html += f"<td style='padding: 8px; border: 1px solid #ddd;'>{item.quantity}</td>"
            items_html += f"<td style='padding: 8px; border: 1px solid #ddd;'>${formatted_price}</td></tr>"

        items_html += "</table>"
        return format_html(items_html)


    formatted_items.short_description = "Order Items"



admin.site.register(Order, OrderAdmin)
    

