from django.urls import path, include
from rest_framework import routers

from Form import views
from Form.restview import FormInfoViewSets
from Form.views import form

router = routers.DefaultRouter()
router.register('FormInfo', FormInfoViewSets)

urlpatterns = [
    path('user_form/', form, name="user_form"),
    path('apis/', include(router.urls)),
    path('display_forms/', views.display_forms, name='display_forms'),
]
