from modeltranslation.translator import register, TranslationOptions
from .models import Category, Tag, Product, Review

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'label')

@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('review',)
