
import requests
import schedule

URL = "https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup"
r = requests.get(url= URL)
def fetch():
    r = requests.get(url= URL)
schedule.every().day.at("00:00").do(fetch)


def fetch_api():
    return r.json()
