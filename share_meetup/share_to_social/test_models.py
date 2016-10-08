from share_to_social.factories import UserFactory, MeetupEventFactory
from share_to_social.models import Meetup_Event
from test_plus.test import TestCase


class TestModels(TestCase):
	def setUp(self):

		self.user1 = UserFactory()
		self.user2 = UserFactory()

		self.event1 = MeetupEventFactory(user=self.user1)
		self.event2 = MeetupEventFactory(user=self.user2)

	def test_meetup_event(self):

		print(self.event1.user.first_name)
		print(Meetup_Event.objects.get(user=self.event1.user))
		self.assertTrue(self.event1.user.first_name)

		print(self.event2.user.first_name)
		print(Meetup_Event.objects.get(user=self.event2.user))
		self.assertTrue(self.event2.user.first_name)
