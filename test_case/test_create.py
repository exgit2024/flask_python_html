import requests, os

def test_register():
    try:
        base_url = "http://localhost:5000"
        url = base_url + f"/create"
        payload = {
                "title": "Spaghetti Bolognese",
                "description": "A classic Italian pasta dish",
                "ingredients": "Spaghetti, ground beef, tomatoes, garlic, onions, olive oil, basil, oregano, salt, pepper",
                "instructions": "1. Cook the spaghetti. 2. Prepare the sauce. 3. Mix together and serve hot."
            }
        response=requests.post(url, json=payload)
        assert response.status_code == 200
        print("Success")
    except AssertionError:
        print("Fail") 
    except Exception as e:
        print("Error")
