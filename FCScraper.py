import requests
from bs4 import BeautifulSoup
import time

# Collects links to each of the free articles on Focused Compounding
# Outputs the link and excerpt to Out_file_path

def linkgetter():
    Outfile_path = ".\linkgetterOutput.txt"
    
    for i in range(85):
        soup = BeautifulSoup(requests.get("https://focusedcompounding.com/free-content/page/"+str(i)).text, "html.parser")

        data = soup.find_all("div", class_="post-content")
        try:    
            for line in data:
                content = line.find("div", class_="post-content-inner").text
                link = line.find("a").get("href")
                with open (Outfile_path, "a") as outfile:
                    outfile.write(link)
                    outfile.write("\n")
                    outfile.write(content)
                    outfile.write("\n")
        except:
            print("error on page: " + i)

def postscraper():
    with open(".\linkgetterOutput.txt", "r") as f:
        try:
            for line in f.readlines():
                if line.startswith("https://focusedcompounding.com/"):
                    URL = line.strip()
                    
                    soup = BeautifulSoup(requests.get(URL).text, "html.parser")
                    div = soup.find("div", class_="post-content")

                    with open ("postscraperOutput.html", "a", encoding='utf8') as outfile:
                        outfile.write('<p style="page-break-before: always;">&nbsp;</p>')
                        outfile.write(div.prettify())
                    time.sleep(0.2)
        except Exception as e: print(e + "FROM: " + URL)

if __name__ == "__main__":
    # linkgetter()
    # postscraper()
    print("no function uncommented")