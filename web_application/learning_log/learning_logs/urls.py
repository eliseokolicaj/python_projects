"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
		#Home page
		path('', views.index, name='index'),
		#Topics page
		path('topics/', views.topics, name='topics'),
		#Single topic page
		path('topics/<int:topic_id>/', views.topic, name='topic'),
		#Path for adding a new topic
		path('new_topic/', views.new_topic, name='new_topic'),
		#Path for adding new entry
		path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
		#Path to edit an entry
		path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
