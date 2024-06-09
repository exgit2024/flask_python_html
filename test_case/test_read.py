import requests, os

def test_read():
    try:
        base_url = "http://localhost:5000" 
        url = base_url + f"/read"
        response=requests.get(url)
        assert response.status_code == 200
        print("Success")
    except AssertionError:
        print("Fail") 
    except Exception as e:
        print("Error")
