
import PoC_1_Step_1_download_data as s1
import PoC_1_Step_2_creating_csv as s2
import PoC_1_Step_3_creating_db as s3
import PoC_1_Step_4_import_data_to_db as s4

URL = "https://www.wroclaw.pl/open-data/87b09b32-f076-4475-8ec9-6020ed1f9ac0/OtwartyWroclaw_rozklad_jazdy_GTFS.zip"
fileName = "./OtwartyWroclaw_rozklad_jazdy_GTFS.zip"
path= "./OtwartyWroclaw_rozklad_jazdy_GTFS"

routes_txt = "routes.txt"
routes_csv = "routes.csv"
cities_csv = "cities.csv"

database_name = "PoC_1_wroclaw_mpk.db"

#Recall of functions
s1.download_data(URL, fileName, path)
s2.preparing_routes(path, routes_txt, routes_csv)
s3.creating_database(database_name)
s4.load_write_data(database_name, routes_csv,cities_csv)
