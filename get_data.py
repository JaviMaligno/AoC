from decouple import config
import requests


AOC_SESSION = config('AOC_SESSION')


s = requests.Session()
s.auth = ('JaviMaligno', '76321jav')
def get_input(day):
    resp = s.get(f'https://adventofcode.com/2022/day/{day}/input', cookies={'session':AOC_SESSION})
    text = resp.text
    return text