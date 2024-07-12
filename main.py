import requests
from bs4 import BeautifulSoup
from pathlib import Path
from PIL import Image
import shutil

HEADERS = {
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Host": "tcbscans.com",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.",
}
link = "https://tcbscans-manga.com/manga/one-piece/ajax/chapters/"
text = requests.post(link).text
soup = BeautifulSoup(text,"html.parser")
links = soup.find_all(class_="wp-manga-chapter")
links = [link.a["href"] for link in links]
ultimo_capitolo,*_=links
print(ultimo_capitolo)
text = requests.get(ultimo_capitolo).text
soup = BeautifulSoup(text,"html.parser")
links = soup.find(class_="chapter-video-frame")
links = links.find_all("img")
links = [link["src"] for link in links]
path = Path("ultimo")
path.mkdir(exist_ok=True)
number_pages=len(links)
for i, link in enumerate(links, 1):
    with open(f"ultimo\\{i}.jpg", "wb") as f:
        print(f"downloading page {i}/{number_pages}")
        f.write(requests.get(link).content)
print("chapter  downloaded")



def conv_rgba_to_rgb(file: str) -> Image.Image:
    rgba = Image.open(file)
    rgb = Image.new("RGB", rgba.size, (255, 255, 255))
    rgb.paste(rgba)
    return rgb


files = [
            f"ultimo\\{i}.jpg" for i in range(1, number_pages + 1)
        ]
images = [conv_rgba_to_rgb(file) for file in files]
images[0].save(
            "ultimo.pdf", "PDF", append_images=images[1:], save_all=True
        )
shutil.rmtree("ultimo")
