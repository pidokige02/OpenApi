from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import UserProfile

# 신호(signals) 시스템을 사용하여 새로운 User 객체가 생성될 때
# 자동으로 UserProfile 객체도 생성되도록 한다.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		userprofile = UserProfile.objects.create(user=instance)
	# sender: 신호를 발생시킨 모델, 여기서는 User 모델입니다.
	# instance: 저장된 User 모델의 인스턴스입니다. 즉, 새로 생성되거나 업데이트된 User 객체를 가리킵니다.
	# created: 새로 생성된 객체일 때 True, 기존 객체가 업데이트될 때 False입니다.
	# **kwargs: 추가적인 키워드 인수입니다.