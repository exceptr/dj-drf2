from django.contrib import admin

from logistic.models import Product, Stock, StockProduct


class StockProductInline(admin.TabularInline):
    model = StockProduct
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    inlines = [StockProductInline]


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['address',]
    inlines = [StockProductInline]
