import requests
from bs4 import BeautifulSoup

# BBC News website
URL = "https://www.bbc.com/news"

try:
    # Send HTTP request
    response = requests.get(URL)
    response.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    print("=" * 60)
    print("           LATEST BBC NEWS HEADLINES")
    print("=" * 60)

    # Find heading tags
    headlines = soup.find_all(["h2", "h3"])

    count = 1

    for headline in headlines:
        text = headline.get_text(strip=True)

        if text:
            print(f"{count}. {text}")
            count += 1

        if count > 10:
            break

except requests.exceptions.RequestException as e:
    print("Error while connecting to the website.")
    print(e)

except Exception as e:
    print("Unexpected Error:", e)