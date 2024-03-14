from django.urls import path,include
from groups.views import CourseAPIList, LoginView,CreateUserView


urlpatterns = [
		path('course/',CourseAPIList.as_view()),
		# path('add/course/',ChooseCourse.as_view(),name='add_course'),
		path('login/', LoginView.as_view()),
		path('reg/',CreateUserView.as_view()),
]
