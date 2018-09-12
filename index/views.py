from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, View, DetailView, ListView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse, Http404
from django.template.loader import render_to_string
import json
from django.conf import settings

# Create your views here.


class IndexView(TemplateView):
	template_name = "index.html"


	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context.update({
			'name': 'Henry'
		})
		return context