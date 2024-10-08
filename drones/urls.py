from django.urls import include, path
from . import views
from rest_framework.routers import SimpleRouter

# Criação do roteador e registro do ViewSet
router = SimpleRouter()
router.register(r"drone-categories", views.DroneCategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),  # As rotas para DroneCategory serão geridas pelo ViewSet
    path("drones/", views.DroneList.as_view(), name=views.DroneList.name),
    path("drones/<int:pk>/", views.DroneDetail.as_view(), name=views.DroneDetail.name),
    path("pilots/", views.PilotList.as_view(), name=views.PilotList.name),
    path("pilots/<int:pk>/", views.PilotDetail.as_view(), name=views.PilotDetail.name),
    path("competitions/", views.CompetitionList.as_view(), name=views.CompetitionList.name),
    path("competitions/<int:pk>/", views.CompetitionDetail.as_view(), name=views.CompetitionDetail.name),
]
