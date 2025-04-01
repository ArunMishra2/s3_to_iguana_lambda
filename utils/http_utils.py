import requests

def post_to_iguana(endpoint, hl7_data, api_key=None):
    headers = {
        'Content-Type': 'text/plain'
    }
    if api_key:
        headers['x-api-key'] = api_key

    response = requests.post(endpoint, headers=headers, data=hl7_data)
    return response.status_code, response.text