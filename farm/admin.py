
from django.contrib import admin
from .models import  FarmUser, UserRoles, Permissions, PermissionsRoles, Roles





class FarmUserAdmin(admin.ModelAdmin):
    pass



class RolesAdmin(admin.ModelAdmin):
    pass


class PermissionsAdmin(admin.ModelAdmin):
    pass


class PermissionsRolesAdmin(admin.ModelAdmin):
    pass





class UserRolesAdmin(admin.ModelAdmin):
    pass



admin.site.register(FarmUser, FarmUserAdmin)
admin.site.register(Roles, RolesAdmin)
admin.site.register(Permissions, PermissionsAdmin)
admin.site.register(PermissionsRoles, PermissionsRolesAdmin)
admin.site.register(UserRoles, UserRolesAdmin)





