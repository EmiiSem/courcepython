from django.contrib.auth.models import User
from datetime import datetime, timedelta
from celery.decorators import periodic_task
from celery.task.schedules import crontab

@periodic_task(run_every=crontab(minute=0, hour=0))
def check_inactive_users():
    # Определяем дату, которую будем сравнивать (1 месяц назад)
    one_month_ago = datetime.now() - timedelta(days=30)

    # Ищем пользователей, которые не заходили более месяца
    inactive_users = User.objects.filter(last_login__lt=one_month_ago)

    # Блокируем найденных пользователей
    for user in inactive_users:
        user.is_active = False
        user.save()