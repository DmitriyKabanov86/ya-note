from django.urls import path

from notes import views

app_name = 'notes'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),  # Должна быть доступна анонимному пользователю.
    path('add/', views.NoteCreate.as_view(), name='add'),  # Доступна аут. пользователю. Аноим редирект на логин.
    path('edit/<slug:slug>/', views.NoteUpdate.as_view(), name='edit'),  # Доступна автору. Аноим редирект на логин.
    path('note/<slug:slug>/', views.NoteDetail.as_view(), name='detail'),  # Доступна автору. Аноим редирект на логин.
    path('delete/<slug:slug>/', views.NoteDelete.as_view(), name='delete'),  # Доступна автору. Аноим редирект на логин.
    path('notes/', views.NotesList.as_view(), name='list'),  # Доступна аут. пользователю. Аноим редирект на логин.
    path('done/', views.NoteSuccess.as_view(), name='success'),  # Доступна аут. пользователю. Аноим редирект на логин.
]
