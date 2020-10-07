import requests
from bs4 import BeautifulSoup
import sys
import PIL.Image
import urllib.request
from PIL import Image
from PIL.ExifTags import TAGS
import glob


class Target:

    def __init__(self):
        # Prototyping attributes of Target
        self.targetWebsite = ''
        self.URL = ''

    def chooseWebsite(self):
        URL = input("Enter the target website:\t")
        if URL not in ("https://", "http://"):
            URL = "https://" + URL
        try:
            URL_content = requests.get(URL)
            soup = BeautifulSoup(URL_content.content, 'html.parser')
        except requests.exceptions.ConnectionError as x:
            print("Error:\t", x)
            sys.exit(1)
        except AttributeError as x:
            print("Could not find website:\t", x)
            sys.exit(1)

        self.URL = URL
        self.targetWebsite = soup

    def extractImages(self):
        images = []
        for element in self.targetWebsite.findAll("img"):
            images.append(element.get('src'))
        for element in self.targetWebsite.findAll("img"):
            images.append(element.get('src'))

        image_urls = []
        for img in images:
            URL_domain_length = len(self.URL)
            if img[:3] != "htt":
                img = f"{self.URL}{img}"
                image_urls.append(img)

        for a in image_urls:
            print(a)

        # Download all images
        if len(image_urls) > 0:
            print(f"[+] Found {len(image_urls)} photos.\n")
        else:
            print(f"[-] Found {len(image_urls)} photos.\n")
            sys.exit(1)

        for img in image_urls:
            try:
                print("Attempting to download: ", img)
                urllib.request.urlretrieve(f"{img}", f"{img[5:]}")
            except urllib.error.HTTPError as x:
                print(img, " returned an error.\n", x)
                pass

    def getMetaData(self):
        file_list = glob.glob("*.jpg")
        for i in file_list:
            image = Image.open(i)
            exifdata = image.getexif()

            for tag_id in exifdata:
                # get the tag name, instead of human unreadable tag id
                tag = TAGS.get(tag_id, tag_id)
                data = exifdata.get(tag_id)
                # decode bytes
                if isinstance(data, bytes):
                    data = data.decode()
                print(f"{tag:25}: {data}")


def main():

    # This looks so clean when you put all the functions into a class
    target = Target()
    target.chooseWebsite()
    target.extractImages()
    target.getMetaData()


if __name__ == "__main__":
    main()