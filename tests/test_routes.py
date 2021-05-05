def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client):

    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == None

def test_temp_saved_two_books(client, two_saved_planets):

    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200

def test_client_post(client):

    response = client.post("/planets", json = new_planet)
    response_body = response.get_json()

    assert response.status_code == 201
