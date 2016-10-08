from factory import DjangoModelFactory, lazy_attribute
from faker import Faker

from .models import Meetup_Event
from django.contrib.auth.models import User

faker = Faker()


class UserFactory(DjangoModelFactory):

	username = lazy_attribute(lambda x: faker.user_name())
	first_name = lazy_attribute(lambda x: faker.first_name())
	email = lazy_attribute(lambda x: faker.email())
	password = lazy_attribute(lambda x: faker.password(
		length=10,
		special_chars=True,
		digits=True,
		upper_case=True,
		lower_case=True
	))

	class Meta:
		model = User


class MeetupEventFactory(DjangoModelFactory):

	user = UserFactory()
	event_id = lazy_attribute(lambda x: faker.pyint())
	group_name = lazy_attribute(lambda x: faker.company())
	event_name = lazy_attribute(lambda x: faker.catch_phrase())
	web_link = lazy_attribute(lambda x: faker.url())
	event_time = lazy_attribute(lambda x: faker.time(pattern='%H:%M:%S'))
	photo_link = lazy_attribute(lambda x: faker.image_url(width=None, height=None))

	class Meta:
		model = Meetup_Event
