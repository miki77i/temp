import requests
import json
from flask import Flask


text = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text