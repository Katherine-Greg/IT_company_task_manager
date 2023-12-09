from django.urls import path

from task_manager.views import (index,
                                TaskListView,
                                TaskDetailView,
                                TaskCreateView,
                                TaskUpdateView,
                                TaskDeleteView,
                                task_assign_delete_worker_view,
                                WorkerListView,
                                WorkerDetailView,
                                WorkerUpdateView,
                                PositionListView,
                                PositionDetailView,
                                PositionCreateView,
                                PositionUpdateView,
                                PositionDeleteView,)


urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/assign-worker/",
         task_assign_delete_worker_view,
         name="task-assign-delete-worker"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("workers/<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("positions/<int:pk>/", PositionDetailView.as_view(), name="position-detail"),
    path("positions/create/", PositionCreateView.as_view(), name="position-create"),
    path("positions/<int:pk>/update/", PositionUpdateView.as_view(), name="position-update"),
    path("positions/<int:pk>/delete/", PositionDeleteView.as_view(), name="position-delete"),

]

app_name = "task_manager"
