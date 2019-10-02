
from django.contrib import admin
from .models import  FarmUser, UserRole, FieldWorker, FarmerGroup, Farmer



class FarmUserAdmin(admin.ModelAdmin):
    pass



class UserRoleAdmin(admin.ModelAdmin):
    pass


class FieldWorkerAdmin(admin.ModelAdmin):
    pass


class FarmerGroupAdmin(admin.ModelAdmin):
    pass


class FarmerAdmin(admin.ModelAdmin):
    pass


admin.site.register(FarmUser, FarmUserAdmin)
admin.site.register(UserRole, UserRoleAdmin)
admin.site.register(FieldWorker, FieldWorkerAdmin)
admin.site.register(FarmerGroup, FarmerGroupAdmin)
admin.site.register(Farmer, FarmerAdmin)

