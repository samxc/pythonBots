import requests
from bs4 import BeautifulSoup
import pyttsx3
import os
import time
from tqdm import tqdm

class GetUrl:
    def __init__(self, url):
        self.url = url
        self.desktop_path = self.get_desktop_path()
        
    def get_desktop_path(self):
        # Check if the desktop path with OneDrive exists
        desktop_path_with_onedrive = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
        if os.path.exists(desktop_path_with_onedrive):
            return desktop_path_with_onedrive

        # If the desktop path with OneDrive doesn't exist, try the desktop path without OneDrive
        desktop_path_without_onedrive = os.path.join(os.path.expanduser("~"), "Desktop")
        if os.path.exists(desktop_path_without_onedrive):
            return desktop_path_without_onedrive

        # If neither path exists, return None or raise an exception, depending on your preference
        return None
        
    def start_scraping(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all('p')
        with open(os.path.join(self.desktop_path, 'scraped.txt'), 'w', encoding='utf-8') as f:
            for ps in results:
                f.write(ps.text)
            f.close()
        for i in tqdm(range(5)):
            time.sleep(1)
        print('Successfully scraped all the text from paragraph tags!')

    def start_reading(self):
        engine = pyttsx3.init()
        print("Would you like to read the scraped file? (y/n)")
        command = str(input())
        if command == "y" or command == "yes":
            with open(os.path.join(self.desktop_path, 'scraped.txt'), 'r', encoding='utf-8') as file:
                text_to_read = file.read()
            engine.setProperty('rate', 150)
            engine.say(text_to_read)
            engine.runAndWait()
        elif command == "n" or command == "no":
            print('Exiting the bot now!')
            os.system('exit')
        else:
            print("Please give a valid command!")

def ask_url():
    print("Enter a website you would like to scrape: ")
    url = str(input())
    return url

if __name__ == "__main__":
    print(" ----------------------------------")
    print("| Welcome To Scrape-Reader Bot     |")
    print("| My job is to make your job easier|")
    print("| Let's start                      |")
    print(" ---------------------------------- ")

    val = ask_url()
    scraper = GetUrl(val)
    scraper.start_scraping()
    scraper.start_reading()
