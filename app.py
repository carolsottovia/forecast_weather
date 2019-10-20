# -*- coding: utf-8 -*-
import util, os

ROOT_DIR = "%s/forecast_weather" % os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

def initDir():
    if not os.path.isdir("%s/%s" % (ROOT_DIR, "csvs")):
        os.mkdir("%s/%s" % (ROOT_DIR, "csvs"))

def main():
    initDir()

    cities = dict([("SP", (-23.5505, -46.6333)), ("RJ", (-22.9068, -43.1729))])
    totalCities = []

    for key, value in cities.items():
        tCity = util.forecastOfWeek(key, cities[key])
        for c in tCity:
            totalCities.append(c)

    util.createCsv(totalCities, ["Date", "City", "MinTemp", "MaxTemp"])

if __name__ == "__main__":
    main()
