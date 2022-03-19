from flight_search import FLIGHT_SEARCH
from sheety import SHEETY
from datetime import datetime, timedelta
f = FLIGHT_SEARCH()
s = SHEETY()
city = f.get_city_code("Tokyo")
flight = f.flight_details(origin_city=city,destination="PAR",to_time= datetime.now() + timedelta(days=1),
from_time = datetime.now() + timedelta(days=(6 * 30)))

if flight.price < 100000:
    print(flight.price)


