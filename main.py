import requests
import urllib3
from faker import Faker
import json
from datetime import datetime

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Initialize Faker with Brazilian locale
fake = Faker('pt_BR')

# Create a session
session = requests.Session()

def generate_fake_data():
    # Generate fake data
    email = fake.email()
    password = fake.password(special_chars=True, digits=True, upper_case=True, lower_case=True)
    name = fake.name()
    cpf = fake.cpf()
    phone = fake.phone_number()
    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=70).strftime('%d/%m/%Y')
    cep = fake.postcode()
    address = fake.street_name()
    number = fake.building_number()
    neighborhood = fake.neighborhood()
    city = fake.city()
    state = fake.state_abbr()

    # Save credentials to file
    with open('credentials.txt', 'a', encoding='utf-8') as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"\nTimestamp: {timestamp}\n")
        f.write(f"Email: {email}\n")
        f.write(f"Password: {password}\n")
        f.write(f"Name: {name}\n")
        f.write("-" * 50 + "\n")

    return {
        'email_validation': email,
        'newsletter': 'on',
        'tipo_pessoa': 'pf',
        'nome_pessoa_fisica': name,
        'cpf': cpf,
        'telephone_pessoa_fisica': phone,
        'data_nascimento': birth_date,
        'postcode': cep,
        'address_1': address,
        'number': number,
        'address_2': neighborhood,
        'city': city,
        'zone_id': state,
        'salvar_como': 'casa',
        'endereco_principal': 'on',
        'password': password,
        'confirm': password,
        'email': email,
        ' agree': '1',
        'tipo_cadastro': 'normal'
    }

# Headers from the cURL command
headers = {
    "Host": "fechosul.santriweb.com.br",
    "sec-ch-ua": '"Brave";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "origin": "https://fechosul.santriweb.com.br",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "sec-gpc": "1",
    "accept-language": "en-US,en;q=0.6",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": "https://fechosul.santriweb.com.br/conta/cadastro",
    "priority": "u=0, i"
}

# URL from the cURL command
url = "https://fechosul.santriweb.com.br/conta/cadastro"

try:
    # Generate fake data
    data = generate_fake_data()
    
    # Make the registration request
    response = session.post(url, headers=headers, data=data, verify=False, allow_redirects=False)
    
    # Print response status
    print(f"Status Code: {response.status_code}")
    
    # Check if registration was successful
    if response.status_code == 200:
        print("Registration attempt completed. Check credentials.txt for the generated account details.")
    else:
        print("Registration attempt failed. Status code:", response.status_code)
    
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
