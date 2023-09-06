import requests

api_keys='cd45dd59'

base_url = f"http://www.omdbapi.com/?apikey={api_keys}"


def search_movies_by_title(title):
    try:
        # Construct the API request URL
        url = f"{base_url}&s={title}"
        
        # Send an HTTP GET request to the API
        response = requests.get(url)
        
        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            print(response.json())
            # Check if the response contains movies
            if 'Search' in data:
                movies = data['Search']
                return movies
            else:
                return []
        else:
            print("Error:", response.status_code)
            return []
    except Exception as e:
        print("An error occurred:", str(e))
        return []



search_term = input("enter the movie name to search")
movies = search_movies_by_title(search_term)

if movies:
    print(f"Found {len(movies)} movies:")
    for movie in movies:
        print(f"Title: {movie['Title']}, Year: {movie['Year']}")
else:
    print("No movies found.")




