import re
import requests
from bs4 import BeautifulSoup


def get_latest_daily_build_url():
    try:
        response = requests.get("https://builder.blender.org/download/daily/")
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <a> tags with href matching the specific pattern
        releases = soup.find_all('a', href=re.compile(
            r"https://cdn\.builder\.blender\.org/download/daily/blender-\d+\.\d+\.\d+-\w+\+\w+\.\w+-linux\.x86_64-release\.tar\.xz"))

        # Filter out URLs containing '.sha256'
        download_urls = [a['href'] for a in releases if '.sha256' not in a['href']]

        # Return only the latest version (assuming list is sorted in descending order by version)
        return download_urls[0] if download_urls else None

    except requests.RequestException as e:
        print(f"Network error: {e}")
    except Exception as e:
        print(f"Error fetching or parsing data: {e}")
    return None


if __name__ == "__main__":
    download_url = get_latest_daily_build_url()
    if download_url:
        print(download_url)
    else:
        print("Failed to find the latest daily Blender build download URL.")
