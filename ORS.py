import requests

def calculate_route(start_latitude, start_longitude, end_latitude, end_longitude):
    api_url = "https://api.openrouteservice.org/v2/directions/driving-car"

    headers = {
        "Authorization": "5b3ce3597851110001cf6248979a09d111a04067acc3745267148029"
    }

    params = {
        "start": f"{start_longitude},{start_latitude}",
        "end": f"{end_longitude},{end_latitude}"
    }

    response = requests.get(api_url, headers=headers, params=params)

    if response.status_code == 200:
        route_data = response.json()
        return route_data
    else:
        print(f"Failed to calculate the route. Error: {response.status_code}")
        return -1


