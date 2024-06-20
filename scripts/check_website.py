import requests

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"The website {url} is online.")
            return True
        else:
            print(f"The website {url} returned status code {response.status_code}.")
            return False
    except requests.ConnectionError:
        print(f"The website {url} is offline.")
        return False

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Check if a website is online.')
    parser.add_argument('url', type=str, help='The URL of the website to check')
    args = parser.parse_args()
    url = args.url
    if not check_website(url):
        exit(1)
