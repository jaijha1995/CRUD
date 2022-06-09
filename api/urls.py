from django.urls import path
from api import views


urlpatterns = [
    path("",views.ListApiAPIView.as_view(),name="Api_list"),
    path("create/", views.CreateApiAPIView.as_view(),name="Api_create"),
    path("update", views.UpdateApiAPIView.as_view(), name ="Api_update"),
    path("delete", views.DeleteApiAPIView.as_view(), name ="Api_update"),
    #path("update/<int:pk>/",views.UpdateApiAPIView.as_view(),name="Api_update"),
    #path("delete/<int:pk>/",views.DeleteApiAPIView.as_view(),name="Api_delete")
]