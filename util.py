# -*- coding: utf-8 -*-
from darksky import forecast
from datetime import date, timedelta
import pandas as pd

def forecastOfWeek(city, geo):
    days = []
    weekday = date.today()
    with forecast("d4f466aaa280fb79c009d11851c638a4", *geo) as sp:
        for day in sp.daily:
            day = [
                date.strftime(weekday, "%d/%b/%Y"),
                city,
                int((day.temperatureMin - 32) / 1.8),
                int((day.temperatureMax - 32) / 1.8),
            ]
            weekday += timedelta(days=1)
            days.append(day)

    return days

def createCsv(data, columns=None):
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(
        "csvs/data_%s.csv" % (str(date.today()).replace("-", "_")),
        header=True,
        index=False,
        sep=";",
    )
