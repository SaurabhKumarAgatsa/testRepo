import requests

# Replace 'YOUR_API_KEY' with your actual TATA TELE API key
API_KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIzNDAzODQiLCJpc3MiOiJodHRwczovL2Nsb3VkcGhvbmUudGF0YXRlbGVzZXJ2aWNlcy5jb20vdG9rZW4vZ2VuZXJhdGUiLCJpYXQiOjE2OTY0MDMxNzQsImV4cCI6MTk5NjQwMzE3NCwibmJmIjoxNjk2NDAzMTc0LCJqdGkiOiIyMkNqSUV1RGVFNjluMHA1In0._OJicGJPxDMGNWXNEpNEfLvDrveYqravPUN1boKEjV0'

# API endpoint for retrieving Call Detail Records (CDR) data
api_url = 'https://api-cloudphone.tatateleservices.com/v1/cdr'

# Prepare the request headers
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# List to store all CDR data
all_cdr_data = []

# Pagination logic
while api_url:
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        cdr_data = response.json()
        all_cdr_data.extend(cdr_data['data'])  # Assuming the CDR data is inside the 'data' key
        # Check if there are more pages of data
        if cdr_data.get('next_page'):
            api_url = cdr_data['next_page']
        else:
            break  # No more pages, exit the loop
    else:
        print(f"Failed to retrieve CDR data. Status code: {response.status_code}")
        break

# Now, all_cdr_data contains all call detail records
print(all_cdr_data)
