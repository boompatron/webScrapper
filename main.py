import requests
from bs4 import BeautifulSoup


def main():
    indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
    indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')
    pagination = indeed_soup.find("div", {"class": "pagination"})
    pages = pagination.find_all('a')
    for p in pages[:-1]:
        print(p.find("span"))


if __name__ == "__main__":
    main()
