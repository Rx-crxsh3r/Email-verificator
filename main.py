import requests

def validate_email(email_address):
    api_key = ""
    url = 'https://api.hunter.io/v2/email-verifier'
    params = {
        'email': email_address,
        'api_key': api_key
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data.get('data'):
            status = data['data']['result']
            if status == "deliverable":
                print(f"Email {email_address} is valid and exists.")
            elif status == "undeliverable":
                print(f"Email {email_address} is invalid and does not exist.")
            else:
                print(f"Email {email_address} has an unknown status: {status}.")
        else:
            print(f"Email {email_address} could not be verified.")
    else:
        print(f"Request failed with status code: {response.status_code}")

email_address = input('Type Email: ')
validate_email(email_address)
