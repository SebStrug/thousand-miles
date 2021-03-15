from functools import lru_cache
from random import choice

import pandas as pd
from geopy import distance

###
# my lat: 51.5538
# my long: -0.3102
# my_coords = (51.5538, -0.3102)


@lru_cache()
def read_csv() -> pd.DataFrame:
    return pd.read_csv('data/worldcities.csv')


def find_my_city(my_lat: float, my_long: float) -> str:
    """Find the the cities which are closest to 1000 miles to you,
    return a random one
    """

    data = read_csv()
    # geopy uses geodesic by default which is too slow for our needs,
    # great-circle is 20x faster, a little less accurate
    data['distance_miles'] = data.apply(lambda x: distance.great_circle(
        (my_lat, my_long), (x['lat'], x['lng'])).miles, axis=1)

    # Find 3 closest to a certain value in a column
    # Possibly more efficient implementations at:
    # https://stackoverflow.com/questions/30112202/how-do-i-find-the-closest-values-in-a-pandas-series-to-an-input-number
    top_cities = data.iloc[(data['distance_miles'] -
                            1000).abs().argsort()[:3]].copy()

    top_cities['pretty_name'] = top_cities['city'] + \
        ' in ' + top_cities['country']
    return choice(top_cities['pretty_name'].tolist())
