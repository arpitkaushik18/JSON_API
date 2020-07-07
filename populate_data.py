import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','JSON_API.settings')

import django
django.setup()

import random

from jsonapi.models import User, ActivityPeriod

from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):
        fake_name = fakegen.name()
        fake_tz=fakegen.timezone()
        fake_user_id = fakegen.random_int()
        user = User.objects.get_or_create(real_name=fake_name,tz=fake_tz,id=fake_user_id)
        fake_start_time = fakegen.date_time()
        fake_end_time   = fakegen.date_time()
        activityperiod = ActivityPeriod.objects.get_or_create(start_time=fake_start_time,end_time=fake_end_time,user_id=fake_user_id)

if __name__ == '__main__':
    print("Populating data.. Please wait.")
    populate(20)
    print("Populating Complete")


