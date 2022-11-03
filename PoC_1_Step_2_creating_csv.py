import pandas as pd

## preparing routes.txt and export .txt to .csv
#selecting specific colums
def preparing_routes(path ,routes_txt="", routes_csv=""):
    header_routes = ["route_id", "route_short_name", "route_desc"] 
    routes_to_csv = pd.read_csv(path+"/"+routes_txt, encoding = "utf-8-sig")
    routes_to_csv.to_csv(routes_csv, columns = header_routes, index = None, encoding = "utf-8-sig")
    return(routes_to_csv)


##creating new csv file - cities.csv
# import csv
# cities_csv = "cities.csv"

# header_cities = ['city_id', 'city_name']
# data_cities = [1, 'Wrocław']

# with open(cities_csv, 'w', encoding = "utf-8-sig",  newline='') as f:
#     writer = csv.writer(f)
#     # write the header
#     writer.writerow(header_cities)
#     # write the data
#     writer.writerow(data_cities)


