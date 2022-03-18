from selenium import webdriver
import urllib.request
import json
from datetime import datetime

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://editorial.rottentomatoes.com/guide/best-netflix-movies-to-watch-right-now/")

now = datetime.now()
movielist = []
i = 1
while i<=100:
    for movie in driver.find_elements_by_class_name("row.countdown-item"):
        print(movie.text.split("\n"))
        for img in movie.find_elements_by_tag_name("img"):
            print(img.get_attribute("src"))
            urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".png")
            i = i+1
            movielist.append(
                {"Title": movie.text.split("\n")[0],
                "Starring": movie.text.split("\n")[5],
                "Directed": movie.text.split("\n")[6],
                "waktu_scraping":now.strftime("%Y-%m-%d %H:%M:%S\n"),
                "Image": img.get_attribute("src")
                    }
                )

hasil_scraping = open("hasilscraping.json", "w")
json.dump(movielist, hasil_scraping, indent = 6)
hasil_scraping.close()
driver.quit()