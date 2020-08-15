from django.urls import path
from . import views
urlpatterns= [
    path('', views.home, name='home'),
    path('settings/', views.SettingsView.as_view(), name='settings'),
    path('skills/', views.SkillListview.as_view(), name='skill-list'),
    path('skills/create', views.SkillCreateView.as_view(), name='skill-create'),
    path('skills/update/<int:pk>', views.SkillUpdateView.as_view(), name='skill-update'),
    path('skills/delete/<int:pk>', views.SkillDeleteView.as_view(), name='skill-delete'),
    path('interests/', views.InterestListview.as_view(), name='interest-list'),
    path('interests/create', views.InterestCreateView.as_view(), name='interest-create'),
    path('interests/update/<int:pk>', views.InterestUpdateView.as_view(), name='interest-update'),
    path('interests/delete/<int:pk>', views.InterestDeleteView.as_view(), name='interest-delete'),
    path('educations/', views.EducationListview.as_view(), name='education-list'),
    path('educations/create', views.EducationCreateView.as_view(), name='education-create'),
    path('educations/update/<int:pk>', views.EducationUpdateView.as_view(), name='education-update'),
    path('educations/delete/<int:pk>', views.EducationDeleteView.as_view(), name='education-delete'),
    path('badges/', views.BadgeListview.as_view(), name='badge-list'),
    path('badges/create', views.BadgeCreateView.as_view(), name='badge-create'),
    path('badges/update/<int:pk>', views.BadgeUpdateView.as_view(), name='badge-update'),
    path('badges/delete/<int:pk>', views.BadgeDeleteView.as_view(), name='badge-delete'),
    path('<slug:username>/', views.WebsiteView.as_view(), name='website'),
]