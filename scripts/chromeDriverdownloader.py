import requests
from requests import HTTPError, ConnectionError
from typing import List
from bs4 import BeautifulSoup
import platform
import os, zipfile

def getLink(websiteLink, version, OSName):
    try:
        html = requests.get(websiteLink)
        html.raise_for_status()
        content = BeautifulSoup(html.text, 'html.parser')
        links: List = [tag["href"] for tag in content.find_all('a', {'class': "XqQF9c"})]
        for link in links:
            if (str(link).find(version) != -1) and (str(link).endswith('.txt') == False):
                downloadLink = str(link).replace('index.html?path=', '') + getOsBasedExtension(OSName)
                print(downloadLink)
                return downloadLink
    except HTTPError:
        raise
    except ConnectionError:
        raise
    except BaseException:
        raise

def getOsBasedExtension(OSName: str):
    if OSName == 'Linux':
        return "chromedriver_linux64.zip"
    elif OSName == 'Windows':
        return "chromedriver_win32.zip"

def downloadDriver(driverLink):
    content = requests.get(driverLink)
    with open(os.path.join(r"../extensions/", os.path.basename(driverLink)), 'wb') as driverFile:
        for chunk in content.iter_content(100000):
            driverFile.write(chunk)
    return os.path.join(r"../extensions/", os.path.basename(driverLink))

def extractFile(zipFileName: str):
    os.chdir(r"../extensions/")
    driverZipObject = zipfile.ZipFile(zipFileName)
    driverZipObject.extractall()
    driverZipObject.close()
    os.unlink(zipFileName)

def downloader(version: str):
    try:
        operatingSystemName: str = platform.system()
        websiteLink = r"https://chromedriver.chromium.org/downloads"
        chromeDriverLink = getLink(websiteLink, version, operatingSystemName)
        extractFile(downloadDriver(chromeDriverLink))
    except BaseException:
        raise

if __name__ == '__main__':
    version: str = input("Enter the version of the chrome driver: ")
    downloader(version)