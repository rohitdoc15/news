import sys
sys.path.append('/home/rohit/news/website')
from fuzzywuzzy import fuzz

import os
import django
from django.utils import timezone
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()
from collections import Counter as CollectionsCounter
from pages.models import Video, TrendingTopic


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
from datetime import datetime
from pages.models import petroluem

# data = [
#     {'date': datetime(2022, 1, 1), 'price': 94},
#     {'date': datetime(2022, 2, 1), 'price': 104},
#     {'date': datetime(2022, 3, 1), 'price': 103},
#     {'date': datetime(2022, 4, 1), 'price': 103},
#     {'date': datetime(2022, 5, 1), 'price': 103},
#     {'date': datetime(2022, 6, 1), 'price': 103},
#     {'date': datetime(2022, 7, 1), 'price': 103},
#     {'date': datetime(2023, 1, 1), 'price': 103},
#     {'date': datetime(2023, 2, 1), 'price': 103},
#     {'date': datetime(2023, 3, 1), 'price': 103},
#     {'date': datetime(2023, 4, 1), 'price': 103},
#     {'date': datetime(2023, 5, 1), 'price': 103},
#     {'date': datetime(2023, 6, 1), 'price': 103},
# ]

# # Clear existing data
# petroluem.objects.all().delete()

# # Create new instances and save them
# for item in data:
#     petroluem_instance = petroluem(price=item['price'], date=item['date'])
#     petroluem_instance.save()


#replace a topic with another topic
from django.db.models import F

old_topic = "Gujarat "
new_topic = "Cyclone Biperjoy"

# Select the videos with the old topic and update their topic field
Video.objects.filter(topic=old_topic).update(topic=new_topic)


    
