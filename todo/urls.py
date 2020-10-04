from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import *

router = routers.DefaultRouter()
router.register('users', HomeViewSet)
router.register('todo', ToDoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', AddToDoView.as_view(), name="add-todo"),
    path('todolist/<int:url>/', ToDoAPIView.as_view(), name="todo-api"),
    path('todolist/add/<int:url>/', AddTodoToListView.as_view(), name="add-todo-to-list"),
    path('todolist/<int:url>/set_code/', ToDoListSetCodeView.as_view(), name="set-code"),
    path('', include(router.urls))
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]