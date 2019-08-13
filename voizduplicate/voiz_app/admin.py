from django.contrib import admin
from .models import Customer5, PrepaidPlan, PostpaidPlan, Dongle5, Credit, BankAxis, BankSBI, Complaint, Faq

admin.site.register(Customer5)
admin.site.register(PrepaidPlan)
admin.site.register(PostpaidPlan)
admin.site.register(Dongle5)


admin.site.register(Credit)
admin.site.register(BankAxis)
admin.site.register(BankSBI)
admin.site.register(Complaint)
admin.site.register(Faq)