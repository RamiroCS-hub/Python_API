import json

def test_start_endpoint (client):
  response = client.get('/start')
  assert response.status_code == 200
  assert b'Te encuentras en un bosque oscuro. Solo hay un sendero que se bifurca en tres direcciones' in response.data

def test_choose_endpoint (client):
  response = client.post('/choose?id=5')
  assert response.status_code == 200
  data = response.get_json()
  assert len(data['options']) == 3

def test_wrong_id_endpoint (client):
  response = client.post('/choose?id=200')
  assert response.status_code == 404