import requests

def calculate_route(start_latitude, start_longitude, end_latitude, end_longitude):
    api_url = "https://api.openrouteservice.org/v2/directions/driving-car"

    headers = {
        "Authorization": "5b3ce3597851110001cf62487d377b2ed72f48b09d41e51457a406b3"
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
        return None


# Example usage
start_latitude = 45.7325  # Replace with the start latitude value
start_longitude = 9.2222  # Replace with the start longitude value
end_latitude = 45.6873  # Replace with the end latitude value
end_longitude = 9.1790  # Replace with the end longitude value


route_data = calculate_route(start_latitude, start_longitude, end_latitude, end_longitude)

if route_data:
    # Extract the route information from the response data
    distance = route_data["features"][0]["properties"]["summary"]["distance"]
    duration = route_data["features"][0]["properties"]["summary"]["duration"]

    print(f"Distance: {distance} meters")
    print(f"Duration: {duration} seconds")
