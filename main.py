import requests
from sslvlib import *
from bs4 import BeautifulSoup
from time import sleep

class SSlv:
    def __new__(cls, *args, **kwargs):
        print("1. Create a new instance of sslv")
        return super().__new__(cls)

    def __init__(self, url):
        response = requests.get(url)  # Replace with your webpage URL
        soup = BeautifulSoup(response.text, "html.parser")
        form = soup.find("form", {"id": "filter_frm"})
        tables = form.find_all("table")
        rows = []
        for row in tables[2].find_all("tr"):
            rows.append(row)
        rows.pop(0)
        rows.pop(len(rows) - 1)

        self.rows=rows


    def listPlaces(self):
        vietas = []
        for each in self.rows:
            vieta = {}
            tds = each.find_all('td')

            url = "https://www.ss.lv" + tds[1].find("a").get("href")
            vieta["idx"] = url.split("/")[-1].split(".")[0]

            print(url)

            if vieta["idx"]=="bolpg":
                break

            response2 = requests.get(url)
            soup2 = BeautifulSoup(response2.text, "html.parser")
            div = soup2.find("div", {"id": "msg_div_msg"})
            trs2 = div.find("table").find_all("table")[0].find_all("tr")
            trs3 = div.find("table").find_all("table")[1].find_all("tr")

            # TODO kā apvienot divus tr mainīgos vienā, lai nebūtu jāveic divi cikli, katrs savam mainīgajam?

            for each in trs2:
                vieta[each.get_text().split(":")[0]] = switch(each.get_text().split(":")[0], each)
                if each.get_text().split(":")[0] == "Iela":
                    vieta["coords"] = searchCoords(each.get_text().split(":")[0], each)

            for each in trs3:
                vieta[each.get_text().split(":")[0]] = switch(each.get_text().split(":")[0], each)
                if each.get_text().split(":")[0] == "Iela":
                    vieta["coords"] = searchCoords(each.get_text().split(":")[0], each)

            vieta["datums"] = soup2.find_all("td", {"class": "msg_footer"})[2].get_text()[8:]


            cenas = div.find_all("table")[-1].find_all("td")[-1].get_text().replace(" ", "").replace(")", "").split(
                "€(")
            vieta["cena"] = cenas[0]
            vieta["cena par kvm"] = cenas[1][:-4]

            vietas.append(vieta)


            self.vietas=vietas

            sleep(0.2)




if __name__ == '__main__':
    pagelist=[
        "https://www.ss.lv/lv/real-estate/flats/cesis-and-reg/sell/",
        "https://www.ss.lv/lv/real-estate/flats/ventspils-and-reg/sell/"
    ]

    for page in pagelist:
        sslv= SSlv(page)
        sslv.listPlaces()
        print(sslv.vietas)
        sleep(0.1)

