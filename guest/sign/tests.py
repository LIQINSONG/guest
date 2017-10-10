from django.test import TestCase
from sign.models import Event, Guest


# Create your tests here.
class ModelTest(TestCase):

	def setUp(self):
		Event.objects.create(id=1, name="openplus 3 event", status=True,
							 limit=2000, address="shenzhen", start_time="2016-08-31 02:18:22")
		Guest.objects.create(id=1, event_id=1, realname="allen", phone="18800000000", emali="alen@mail.com", sign=False)

	def test_event_models(self):
		result = Event.objects.get(name = "openplus 3 event")
		self.assertEquals(result.address, "beijing")
		self.assertTrue(result.status)

	def test_guest_models(self):
		result = Guest.objects.get(phone = "18800000000")
		self.assertEquals(result.realname, "allen")
		self.assertFalse(result.sign)