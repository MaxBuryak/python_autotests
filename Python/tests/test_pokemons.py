import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '49354efcc4e46344412edb15decea7e5'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '27427'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200
  