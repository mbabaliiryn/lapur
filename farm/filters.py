from django.db.models import Q

from rest_framework import filters


class FarmerQuerySet(models.QuerySet):
    def farmers(self):
        return self.filter(is_farmer=True)