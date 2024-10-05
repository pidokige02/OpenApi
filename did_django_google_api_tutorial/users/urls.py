from django.urls import path
from . import views


app_name = "users"
urlpatterns = [
	# as_view()는 클래스 기반 뷰(Class-Based View, CBV)를 **함수 기반 뷰(Function-Based View, FBV)**로 변환하는 역할
	path('', views.AccountView.as_view(), name="account"),
	path('profile', views.profile_view, name="profile"),
	path('sign-up', views.SignUpView.as_view(), name="sign-up"),
	path('sign-in', views.SignInView.as_view(), name="sign-in"),
	path('sign-out', views.sign_out, name="sign-out"),
	]