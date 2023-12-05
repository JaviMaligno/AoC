from decouple import config
import requests


AOC_SESSION = config('AOC_SESSION')


s = requests.Session()

def get_input(day):
    resp = s.get(f'https://adventofcode.com/2023/day/{day}/input', cookies={'session':AOC_SESSION}, verify=False)
    text = resp.text
    return text

