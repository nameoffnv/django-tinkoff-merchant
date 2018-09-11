from django.contrib import admin

from .models import Payment, Receipt, ReceiptItem
from .services import MerchantAPI


def make_cancel(modeladmin: admin.ModelAdmin, request, qs):
    for p in qs:
        MerchantAPI().cancel(p)
        p.save()

make_cancel.short_description = 'Отменить платеж'


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_id', 'get_amount_rub', 'success', 'status', 'payment_id']
    list_filter = ['status', 'success']
    search_fields = ['order_id', 'payment_id']
    actions = [make_cancel]

    def get_amount_rub(self, obj):
        return obj.amount / 100

    get_amount_rub.short_description = 'Сумма (руб)'

    def has_add_permission(self, request):
        return False

    def get_readonly_fields(self, request, obj=None):
        return [f.name for f in obj._meta.fields]


class PermissionsMixin:
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ReceiptItemInline(PermissionsMixin, admin.TabularInline):
    model = ReceiptItem


@admin.register(Receipt)
class ReceiptAdmin(PermissionsMixin, admin.ModelAdmin):
    list_display = ['id', 'payment', 'email', 'phone']
    inlines = [ReceiptItemInline]
