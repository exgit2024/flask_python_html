import requests, os

def test_delete():
    try:
        base_url = "http://localhost:5000"
        url = base_url + f"/delete"
        payload = {
            "title": 'sample@gmail.com',
        }
        response=requests.post(url, json=payload)
        assert response.status_code == 200
        print("Success")
    except AssertionError:
        print("Fail") 
    except Exception as e:
        print("Error")
