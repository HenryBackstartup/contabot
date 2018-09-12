from django.test import TestCase
from django.test import RequestFactory
from .views import IndexView
# Create your tests here.



class IndexViewTest(TestCase):
	def test_get(self):
		"""HelloView.get() sets 'name' in response context."""
		# Setup name.
		name = 'Henry'
		# Setup request and view.
		request = RequestFactory().get('/fake-path')
		view = IndexView.as_view(template_name='index.html')

		# Run.
		response = view(request, name=name)
		# Check.
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.template_name[0], 'index.html')
		self.assertEqual(response.context_data['name'], name)	