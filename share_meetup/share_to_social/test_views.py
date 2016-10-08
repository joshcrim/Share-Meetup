from test_plus.test import TestCase
from share_to_social.factories import UserFactory, MeetupEventFactory


class TestViews(TestCase):

	def test_index(self):
		#if user is logged in redirect to home. if user is not logged in display forms to do so.
		#response = self.get('index')
		#print(response.context)
		#self.assertEquals(response.status_code, 200)
		pass

	def test_home(self):
		#TEST if user is not logged in, redirect to login page. if user is logged in but hasnt connected
		# to social accounts, redirect to connect_social. If user is logged in and has connect to meetup,
		# get meetup events and display.
		user_factory = UserFactory()

		self.user1 = self.make_user()
		self.event1 = MeetupEventFactory(user=self.user1)

		with self.login(self.user1):
			response = self.get('home')
		pass
