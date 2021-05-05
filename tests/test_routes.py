def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_no_data_returns_404(client):

    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {
        "message": "Planet with id 1 was not found",
        "success": False
    }

def test_get_one_planet(client, two_saved_planets):

    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Callisto",
        "description": "This planet has water all over the surface"
    }

def test_get_all_planets_with_valid_data(client,two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "Callisto",
        "description": "This planet has water all over the surface"
    },
        {
        "id": 2,
        "name": "Ego",
        "description": "A new planet the has many secrets"
        }
    ]

def test_post_new_planet(client):
    new_planet={
        "name": "Raw",
        "description": "A frozen planet"
    }
    response = client.post("/planets", json=new_planet)
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {
        "success" : True,
        "message" : "Planet Raw has been created"
    }