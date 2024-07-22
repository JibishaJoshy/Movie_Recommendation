from django.urls import path
from Backend import views


urlpatterns=[
    path('index_page/', views.index_page,name="index_page"),
    path('Add_category',views.Add_category,name="Add_category"),
    path('savedata_Category',views.savedata_Category,name="savedata_Category"),
    path('display_Movie/',views.display_Movie,name="display_Movie"),
    path('edit_Movie/<int:Movieid>/',views.edit_Movie,name="edit_Movie"),
    path('update_Movie/<int:Movieid>/',views.update_Movie,name="update_Movie"),
    path('delete_Movie/<int:Movieid>/',views.delete_Movie,name="delete_Movie"),

    # *****************************
    path('login_page/',views.login_page,name="login_page"),
    path('login_admin/',views.login_admin,name="login_admin"),
    path('Adminlogout/',views.Adminlogout,name="Adminlogout"),
]