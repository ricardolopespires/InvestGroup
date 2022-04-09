import sys, os 
import pandas as pd
import json


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "investgroup.settings")

import django
django.setup()


from analytics.models import Selic



selic = Selic.objects.all()
