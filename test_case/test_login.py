import requests, os

def test_login():
    try:
        base_url = "http://localhost:5000" 
        url = base_url + f"/login"
        payload = {
            "email": 'sample@gmail.com',
            "password": 'Sample123*'
        }
        response=requests.post(url, json=payload)
        assert response.status_code == 200
        print("Success")
    except AssertionError:
        print("Fail") 
    except Exception as e:
        print("Error")
