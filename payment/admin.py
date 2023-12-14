from django.contrib import admin

from payment.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date_payment', 'payment_amount', 'payment_method',)
    list_filter = ('date_payment',)
    search_fields = ('user',)
