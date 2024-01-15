from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('birds/', views.birds_index, name="index"),
    path('create/', views.BirdCreate.as_view(), name='bird_create'),
    path('birds/<int:bird_id>/', views.birds_detail, name="detail"),
    path('birds/<int:pk>/update', views.BirdUpdate.as_view(), name="bird_update"),
    path('birds/<int:pk>/delete', views.BirdDelete.as_view(), name="bird_delete"),
    path('birds/<int:bird_id>/add_feeding/', views.add_feeding, name="add_feeding" ),
    
    path('birds/<int:bird_id>/assoc_nestingmaterial/<int:nestingmaterial_id>/', views.assoc_nestingmaterial, name='assoc_nestingmaterial'),
    path('birds/<int:bird_id>/unassoc_nestingmaterial/<int:nestingmaterial_id>/', views.unassoc_nestingmaterial, name='unassoc_nestingmaterial'),
    
    path('nesting-materials/', views.NestingMaterialList.as_view(), name="nestingmaterials_index"),
    path('nesting-materials/<int:pk>/', views.NestingMaterialDetail.as_view(), name='nestingmaterials_detail'),
    path('nesting-materials/create', views.NestingMaterialCreate.as_view(), name='nestingmaterials_create'),
    path('nesting-materials/<int:pk>/update/', views.NestingMaterialUpdate.as_view(), name='nestingmaterials_update'),
    path('nesting-materials/<int:pk>/delete', views.NestingMaterialDelete.as_view(), name="nestingmaterials_delete")
]