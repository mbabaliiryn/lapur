from farm.views import FarmUserViewSet, UserRoleViewSet, FieldWorkerViewSet, FarmerGroupViewSet, FarmerViewSet

from django.urls import include, path

from rest_framework import routers


router = routers.DefaultRouter()



router.register('farm_user', FarmUserViewSet)
router.register('user_role', UserRoleViewSet)
router.register('field_worker', FieldWorkerViewSet)
router.register('farmer_group', FarmerGroupViewSet)
router.register('farmer', FarmerViewSet)




urlpatterns = [
    path('', include(router.urls)),
    # path('Farm_User', FarmerViewSet.as_view({'get':'list'})),
    
]