import requests

# Authorization token that must have been created previously
token = "BQBJbDaW48XbIozYqYPcngxgjWoid5uothv9YYkuW715I1KwXHGFkUmwyR1EDNpLCJzvDjM3_s-pDu_QTXxZzct-zrB_EzD_5NShGF1veSSb3ziYoKMtwhV5G2vuQaspYQvLwqVxVk1e3Ork27Ogw_5lqB3AVw1HguUhfCulXI6nAPa1Us6zvVA9xBQq5a13cqq9oo2RJlCJu6WR_-a6FPxDRoYUK1Cg8hccVhbSoWOaKrGDhB-VnXmLINdHIgh0pc05HguKs4ViozutJ7UBL_xaCGXBjkz2DTkG"

def fetch_web_api(endpoint, method="GET", body=None):
    url = f"https://api.spotify.com/{endpoint}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    if method == "GET":
        response = requests.get(url, headers=headers)
    elif method == "POST":
        response = requests.post(url, headers=headers, json=body)
    else:
        raise ValueError("Unsupported HTTP method")
    
    response.raise_for_status()  # Raise an error for HTTP issues
    return response.json()

def get_available_genre():
    # Endpoint reference: https://developer.spotify.com/documentation/web-api/reference/get-users-top-artists-and-tracks
    endpoint = "/recommendations/available-genre-seeds"
    response = fetch_web_api(endpoint)
    return response.get("items", [])

def get_top_tracks():
    endpoint = "v1/me/top/tracks?time_range=long_term&limit=5"
    response = fetch_web_api(endpoint)
    return response.get("items", [])
# Fetch and print the top tracks
top_tracks = get_top_tracks()
# available_genres = get_available_genre()

for track in top_tracks:
    name = track["name"]
    artists = ", ".join(artist["name"] for artist in track["artists"])
    print(f"{name} by {artists}")
# print(available_genres)