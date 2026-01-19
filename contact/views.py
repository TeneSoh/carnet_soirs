from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.template.context_processors import request
from django.http import Http404
from contact.models import Contact
# Create your views here.
