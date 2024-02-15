import requests
from datetime import datetime, timedelta

# Define your API key and headers
api_key = 'API_KEY_HERE'
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# Define the date range for the GET request
date = datetime.now()  # get the current date and time
date_start = date.replace(hour=0, minute=0, second=0, microsecond=0)  # start of the day
date_end = date_start + timedelta(days=1)  # end of the day

params = {
    'date_created__gt': date_start.isoformat(),
    'date_created__lt': date_end.isoformat()
}

# Make the GET request
response = requests.get('https://api.close.com/api/v1/activity/call/', headers=headers, params=params)

# Print the response
print(response.json())