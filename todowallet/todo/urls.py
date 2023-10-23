from django.urls import path


from .views import CatCreateList, CatRetrieveUpdateApiView, CatRetrieveDestroyApiView


urlpatterns = [
    path('cat/', CatCreateList.as_view()),
    path('cat/update/<int:pk>/', CatRetrieveUpdateApiView.as_view()),
    path('cat/delete/<int:pk>/', CatRetrieveDestroyApiView.as_view()),
]