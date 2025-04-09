from django.db import models
from ckeditor.fields import RichTextField
from account.models import CustomUser
from django.utils import timezone
from django.utils.text import slugify
# import gettext_lazy as _
from django.utils.translation import gettext_lazy as _


# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name=_("Name"))
    suplier=models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True,verbose_name=_("Suplier"))

    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

# Tag Model
class Tag(models.Model):
    name = models.CharField(max_length=100,verbose_name=_("Name"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

# Image Model
class ProductImage(models.Model):
    image = models.ImageField(upload_to='images/',verbose_name=_("Image"))

    def __str__(self):
        # return the image name and split it by / and get the last part
        return self.image.name.split('/')[-1]
    
    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

# Product Model
class Product(models.Model):
    suplier=models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True,verbose_name=_("Suplier"))
    title = models.CharField(max_length=100,verbose_name=_("Title"))
    main_image = models.ImageField(upload_to='products/',verbose_name=_("Main Image"))
    images = models.ManyToManyField('ProductImage', blank=True,verbose_name=_("Images"))  # Allow empty image lists
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name=_("Price"))
    description = RichTextField(verbose_name=_("Description"))
    discount = models.DecimalField(max_digits=10, decimal_places=0, default=0,verbose_name=_("Discount"))  # Default to 0
    label = models.CharField(max_length=100, blank=True, null=True,verbose_name=_("Label"))
    category = models.ForeignKey('Category', on_delete=models.CASCADE,verbose_name=_("Category"))
    tags = models.ManyToManyField('Tag', blank=True,verbose_name=_("Tags"))  # Allow products without tags
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True,verbose_name=_("Updated At"))
    rate = models.DecimalField(max_digits=3, decimal_places=0, default=0,verbose_name=_("Rate"))  # Store the average rating
    SKU = models.CharField(max_length=100, unique=True,verbose_name=_("SKU"))  # Ensure SKU is unique
    slug = models.SlugField(unique=True, blank=True, null=True,verbose_name=_("Slug"))

    def __str__(self):
        return self.title

    def update_rating(self):
        """ Update the product rating based on all reviews. """
        reviews = self.reviews.all()
        total_reviews = reviews.count()
        total_rating = sum(review.rate for review in reviews)

        self.rate = total_rating / total_reviews if total_reviews > 0 else 0
        self.save()

    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate initial slug from title
            base_slug = slugify(self.title)
            slug = base_slug
            # Check if slug exists and generate unique slug
            counter = 1
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            
            
        # suplier = request.user
        
        
        super().save(*args, **kwargs)
        
        
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

# Review Model
class Review(models.Model):
    name = models.CharField(max_length=100,verbose_name=_("Name"))
    email = models.EmailField(verbose_name=_("Email"))
    review = models.TextField(verbose_name=_("Review"))
    rate = models.DecimalField(max_digits=3, decimal_places=2,verbose_name=_("Rate"))  # Supports values like 5.0, 4.5
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="reviews",verbose_name=_("Product"))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Ensure rate is between 0 and 5
        self.rate = min(5, max(0, self.rate))

        super().save(*args, **kwargs)  # Save the review first

        # Update the product rating
        self.product.update_rating()
        

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")


# wishlist
class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,verbose_name=_("User"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name=_("Product"))
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=_("Created At"))

    def __str__(self):
        return f'{self.user.username} - {self.product.title}'
    
    class Meta:
        verbose_name = _("Wishlist")
        verbose_name_plural = _("Wishlists")
    
    
# copoun
class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True,verbose_name=_("Code"))
    discount = models.DecimalField(max_digits=10, decimal_places=2,help_text="%",verbose_name=_("Discount"))
    valid_from = models.DateTimeField(verbose_name=_("Valid From"))
    valid_to = models.DateTimeField(verbose_name=_("Valid To"))
    active = models.BooleanField(default=True,verbose_name=_("Active"))

    def __str__(self):
        return self.code
    
    class Meta:
        verbose_name = _("Coupon")
        verbose_name_plural = _("Coupons")

# card 
class Card(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,verbose_name=_("User"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name=_("Product"))
    quantity = models.PositiveIntegerField(default=1,verbose_name=_("Quantity"))
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True,verbose_name=_("Updated At"))
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True,verbose_name=_("Coupon"))
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name=_("Total Price"))
    total_price_after_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name=_("Total Price After Discount"))
    
    def __str__(self):
        return f'{self.user.username} - {self.product.title}'
    
    
    def save(self, *args, **kwargs):
        # Calculate total price
        self.total_price = self.product.price * self.quantity

        # Calculate total price after discount
        if self.coupon and self.coupon.active and self.coupon.valid_from <= timezone.now() <= self.coupon.valid_to:
            self.total_price_after_discount = self.total_price - (self.total_price * (self.coupon.discount / 100))
        else:
            self.total_price_after_discount = self.total_price

        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = _("Card")
        verbose_name_plural = _("Cards")


# card 
class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", _("Pending")),
        ("paid", _("Paid")),
        ("failed", _("Failed")),
        ("cancelled", _("Cancelled")),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,verbose_name=_("User"))
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name=_("Total Price"))
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True,verbose_name=_("Updated At"))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending",verbose_name=_("Status"))
    transaction_id = models.CharField(max_length=255, null=True, blank=True,verbose_name=_("Transaction ID"))

    def __str__(self):
        return f"Order {self.id} - {self.user.username} - {self.status}"

    def calculate_total(self):
        """Recalculate total price based on order items"""
        self.total_price = sum(item.total_price for item in self.orderitem_set.all())
        self.save()
        
    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,verbose_name=_("Order"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name=_("Product"))
    quantity = models.PositiveIntegerField(default=1,verbose_name=_("Quantity"))
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True,verbose_name=_("Updated At"))
    status = models.CharField(max_length=100, default='pending',verbose_name=_("Status"))
    address = models.CharField(max_length=100, blank=True, null=True,verbose_name=_("Address"))
    phone = models.CharField(max_length=100, blank=True, null=True,verbose_name=_("Phone"))
    city = models.CharField(max_length=100, blank=True, null=True,verbose_name=_("City"))
    country = models.CharField(max_length=100, blank=True, null=True,verbose_name=_("Country"))
    zip_code = models.CharField(max_length=100, blank=True, null=True,verbose_name=_("Zip Code"))
    notes = models.TextField(blank=True, null=True,verbose_name=_("Notes"))
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name=_("Total Price"))
    total_price_after_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name=_("Total Price After Discount"))

    def __str__(self):
        return f'{self.order.user.username} - {self.product.title}'

    def save(self, *args, **kwargs):
        # Calculate total price
        self.total_price = self.product.price * self.quantity

        # Apply discount if the order has a valid coupon
        if self.order.user.card_set.filter(product=self.product).exists():
            card_item = self.order.user.card_set.get(product=self.product)
            if card_item.coupon and card_item.coupon.active and card_item.coupon.valid_from <= timezone.now() <= card_item.coupon.valid_to:
                self.total_price_after_discount = self.total_price - (self.total_price * (card_item.coupon.discount / 100))
            else:
                self.total_price_after_discount = self.total_price
        else:
            self.total_price_after_discount = self.total_price

        super().save(*args, **kwargs)
        

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")