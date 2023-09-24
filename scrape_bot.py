import requests
from bs4 import BeautifulSoup
import pyttsx3
import os
import time
from tqdm import tqdm

class GetUrl:
    def __init__(self, url):
        self.url = url
        
    def start_scraping(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all('p')
        with open('C:\\{provide your desktop path here}\\scraped.txt', 'w', encoding='utf-8') as f:
            for ps in results:
                f.write(ps.text)
            f.close()
        for i in tqdm(range(5)):
            time.sleep(1)
        print('Successfully, scraped all the text from paragraph tags!.')

    def start_reading(self):
        engine = pyttsx3.init()
        print("Would you like to read the scraped file?(y/n)")
        command = str(input())
        if command == "y" or command == "yes":
            with open('C:\\{provide your desktop path here}\\scraped.txt', 'r', encoding='utf-8') as file:
                text_to_read = file.read()
            engine.setProperty('rate', 150)
            engine.say(text_to_read)
            engine.runAndWait()
        elif command == "n" or command == "no":
            print('exiting the bot now!')
            os.system('exit')
        else:
            print("please give a valid command!.")


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
    
