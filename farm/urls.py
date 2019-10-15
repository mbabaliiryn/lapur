
from farm.views import FarmUserViewSet, UserRolesViewSet, PermissionsViewSet, PermissionsRolesViewSet, RolesViewSet


from django.urls import include, path

from rest_framework import routers


router = routers.DefaultRouter()



router.register('farm_user', FarmUserViewSet)
router.register('user_roles', UserRolesViewSet)
router.register('Permissions', PermissionsViewSet)
router.register('permissions_roles', PermissionsRolesViewSet)
router.register('roles', RolesViewSet)



urlpatterns = [
    path('', include(router.urls)),
    # path('Farm_User', FarmerViewSet.as_view({'get':'list'})),
    
]
