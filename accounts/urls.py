from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views





urlpatterns =[

    #path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name = 'logout'),
    path('login/', views.loggin, name = 'login'),  
    path('register/',views.Register_User_View.as_view(), name = 'register'),
    path('password-reset/', views.Password_Reset_View.as_view(),name='password-reset'),
    path('activate/<uidb64>/<token>/', views.User_Activate_Email.as_view(), name='activate'),


    path('perfil/list/',views.Perfil_Investor_View.as_view(), name = 'list'),

    #-------------------------------------- Api Perfil Usuarios ---------------------------------------------------------


    path('quiz/perfil/usuario/list/',views.perfilList),
    path('quiz/perfil/usuario/detail/<str:pk>/',views.perfilDetail),
    path('quiz/perfil/usuario/create/',views.perfilCreate),
    path('quiz/perfil/usuario/update/<str:pk>/',views.perfilUpdate),
    path('quiz/perfil/usuario/delete/<int:pk>/',views.perfilDelete),

    #-------------------------------------- Api Situação Usuarios ---------------------------------------------------------

    path('quiz/situacao/usuario/list/',views.situacaoList),
    path('quiz/situacao/usuario/detail/<int:pk>/',views.situacaoDetail),
    path('quiz/situacao/usuario/create/',views.situacaoCreate),
    path('quiz/situacao/usuario/update/<int:pk>/',views.situacaoUpdate),
    path('quiz/situacao/usuario/delete/<int:pk>/',views.perfilDelete),


    #-------------------------------------- Api Usuarios --------------------------------------------------------------------

    path('quiz/accounts/<int:pk>/perfil/',views.User_Api_Update),
    path('quiz/accounts/<int:pk>/detail/',views.User_Api_Detail),
    
]