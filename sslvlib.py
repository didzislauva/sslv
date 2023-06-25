def switch(x,val):
    return {
        'Pilsēta, rajons': val.get_text().split(":")[1],
        'Pilsēta': val.get_text().split(":")[1],
        'Rajons': val.get_text().split(":")[1],
        'Pilsēta/pagasts': val.get_text().split(":")[1],
        'Ciems':val.get_text().split(":")[1],
        'Iela':val.get_text().split(":")[1][:-8],
        'Istabas':val.get_text().split(":")[1],
        'Platība':val.get_text().split(":")[1][:-3],
        'Stāvs':val.get_text().split(":")[1],
        'Sērija':val.get_text().split(":")[1],
        'Mājas tips':val.get_text().split(":")[1],
        'Ērtības':val.get_text().split(":")[1]
    }.get(x, "")


def searchCoords(x,val):
    nosaukums=val.get_text().split(":")[1][:-8]
    if x=="Iela":
        x=float(val.find("a").get("onclick").split(",")[3].split("=")[3])
        y=float(val.find("a").get("onclick").split(",")[4].replace(" ",""))
        #print(x, y, nosaukums);
        return(x, y)