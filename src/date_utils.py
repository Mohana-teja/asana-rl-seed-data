from datetime import datetime, timedelta
import random

NOW = datetime.now()

def random_past_date(days_back=180):
    delta_days = random.randint(0, days_back)
    return NOW - timedelta(days=delta_days)
