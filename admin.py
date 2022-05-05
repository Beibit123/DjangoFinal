from django.contrib import admin
from .models import *


admin.site.register(Category),
admin.site.register(Salad),
admin.site.register(Soup),
admin.site.register(Dessert),
admin.site.register(Snack),
admin.site.register(Order)
