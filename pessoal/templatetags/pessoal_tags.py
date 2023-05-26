from dateutil.relativedelta import *
from datetime import datetime, timedelta
from django import template
import math



register = template.Library()


@register.simple_tag
def calculation(mensal, anterior):    
    if  anterior is None or  anterior is 0:
        return 0  
    sellprice = mensal - (mensal *  anterior/100)
    return math.floor(sellprice)
