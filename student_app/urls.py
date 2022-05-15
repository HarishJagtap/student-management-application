from django.urls import path, include
from rest_framework.routers import DefaultRouter

from student_app.views import (
    StudentViewSet,
    StudentSearchWebsite,
    StudentCreateWebsite,
)

router = DefaultRouter()
router.register("student", StudentViewSet, basename="student")

urlpatterns = [
    # API urls
    path('', include(router.urls)),
    # Website urls
    path('website/search/', StudentSearchWebsite, name="website-search"),
    path('website/create/', StudentCreateWebsite, name="website-create"),
]
