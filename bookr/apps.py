import imp
from django.contrib.admin import apps 
class ReviewsAdminConfig(apps.AdminConfig):
    default_site = 'bookr.admin.BookrAdminSite'