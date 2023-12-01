from decouple import config
import requests
import certifi
import ssl

# Create a new SSL context
ssl_context = ssl.create_default_context()

# Load the certificates from certifi
ssl_context.load_verify_locations(certifi.where())


AOC_SESSION = config('AOC_SESSION')


s = requests.Session()

def get_input(day):
    resp = s.get(f'https://adventofcode.com/2023/day/{day}/input', cookies={'session':AOC_SESSION}, verify=False)
    text = resp.text
    return text

