from django.core.management.base import BaseCommand
from django.core.files import File
from product.models import Category, Tag, Product, Review, ProductImage
from faker import Faker
from django.conf import settings
import random
import os
from decimal import Decimal

class Command(BaseCommand):
    help = 'Seed data for products and reviews'

    def handle(self, *args, **kwargs):
        # Initialize Faker for both English and Arabic
        fake_en = Faker()
        fake_ar = Faker('ar_AA')  # Arabic locale

        # Create Categories
        categories = []
        category_data = [
            {'en': 'Electronics', 'ar': 'إلكترونيات'},
            {'en': 'Clothing', 'ar': 'ملابس'},
            {'en': 'Books', 'ar': 'كتب'},
            {'en': 'Home & Kitchen', 'ar': 'المنزل والمطبخ'},
            {'en': 'Sports', 'ar': 'رياضة'}
        ]

        # Sample product names for each category
        product_names = {
            'Electronics': [
                'Smart Watch', 'Wireless Earbuds', 'Laptop', 'Smartphone', 
                'Tablet', 'Power Bank', 'Bluetooth Speaker', 'Gaming Console',
                'Digital Camera', 'Smart TV'
            ],
            'Clothing': [
                'T-Shirt', 'Jeans', 'Dress', 'Jacket', 'Sweater', 
                'Hoodie', 'Shorts', 'Skirt', 'Pants', 'Coat'
            ],
            'Books': [
                'Novel', 'Cookbook', 'History Book', 'Science Book', 
                'Poetry Collection', 'Biography', 'Self-Help Book',
                'Children\'s Book', 'Technical Manual', 'Art Book'
            ],
            'Home & Kitchen': [
                'Coffee Maker', 'Blender', 'Toaster', 'Air Fryer',
                'Food Processor', 'Microwave', 'Kettle', 'Mixer',
                'Rice Cooker', 'Vacuum Cleaner'
            ],
            'Sports': [
                'Yoga Mat', 'Dumbbells', 'Tennis Racket', 'Basketball',
                'Soccer Ball', 'Running Shoes', 'Fitness Tracker',
                'Jump Rope', 'Exercise Bike', 'Weight Bench'
            ]
        }

        image_data = [
            {'image': '/static/assets/images/products/img_1.jpg'},
            {'image': '/static/assets/images/products/img_2.jpg'},
            {'image': '/static/assets/images/products/img_3.jpg'},
            {'image': '/static/assets/images/products/img_4.jpg'},
            {'image': '/static/assets/images/products/img_5.jpg'},
            {'image': '/static/assets/images/products/img_6.jpg'},
            {'image': '/static/assets/images/products/img_7.jpg'},
            {'image': '/static/assets/images/products/img_8.jpg'},
            {'image': '/static/assets/images/products/img_9.jpg'},
            {'image': '/static/assets/images/products/img_10.jpg'},
        ]

        self.stdout.write('Creating categories...')
        for cat in category_data:
            category = Category.objects.create(
                name=cat['en'],
                name_ar=cat['ar']
            )
            categories.append(category)

        # Create Tags
        tags = []
        tag_data = [
            {'en': 'New', 'ar': 'جديد'},
            {'en': 'Popular', 'ar': 'شائع'},
            {'en': 'Sale', 'ar': 'تخفيض'},
            {'en': 'Best Seller', 'ar': 'الأكثر مبيعاً'},
            {'en': 'Featured', 'ar': 'مميز'}
        ]

        self.stdout.write('Creating tags...')
        for tag in tag_data:
            tag_obj = Tag.objects.create(
                name=tag['en'],
                name_ar=tag['ar']
            )
            tags.append(tag_obj)

        # Create Sample Product Images
        product_images = []
        for image in image_data[:5]:  # Create 5 sample product images
            img = ProductImage.objects.create(
                image=image['image']
            )
            product_images.append(img)

        # Create Products
        self.stdout.write('Creating products...')
        for _ in range(50):
            # Generate random values
            price = round(random.uniform(10, 1000), 2)
            discount = round(random.uniform(0, price/2), 2)
            rate = round(random.uniform(1, 5), 2)

            # Select random category and corresponding product name
            category = random.choice(categories)
            product_name = random.choice(product_names[category.name])

            # Create product with both English and Arabic content
            product = Product.objects.create(
                title=f"{product_name} {fake_en.word().capitalize()}",
                title_ar=f"{fake_ar.word()} {fake_ar.word()}",
                main_image=random.choice(image_data)['image'],
                price=Decimal(str(price)),
                description=fake_en.text(max_nb_chars=200),
                description_ar=fake_ar.text(max_nb_chars=200),
                discount=Decimal(str(discount)),
                label=random.choice(['New', 'Hot', 'Sale']),
                label_ar=random.choice(['جديد', 'رائج', 'تخفيض']),
                category=category,
                rate=rate,
                SKU=fake_en.unique.ean(length=8)
            )

            # Add random tags
            product.tags.set(random.sample(tags, random.randint(1, 3)))
            
            # Add random product images
            product.images.set(random.sample(product_images, random.randint(1, 3)))

            # Create reviews for this product
            if random.random() < 0.5:  # 50% chance of having reviews
                num_reviews = random.randint(1, 12)
                for _ in range(num_reviews):
                    Review.objects.create(
                        name=fake_en.name(),
                        email=fake_en.email(),
                        review=fake_en.text(max_nb_chars=200),
                        review_ar=fake_ar.text(max_nb_chars=200),
                        rate=round(random.uniform(1, 5), 2),
                        product=product
                    )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database!'))
