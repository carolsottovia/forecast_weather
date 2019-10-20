Dark Sky
========

This  library for the `Dark Sky
API <https://darksky.net/dev/docs>` provides access to detailed
weather information from around the globe.

Requirements
------------

Before you start using this library, you need to get your API key
<https://darksky.net/dev/register>.

Installation
-------------
You should use pip to install darkskylib and pandas:

* pip install darkskylib
* pip install pandas

And to remove:
* pip uninstall darkskylib
* pip uninstall pandas


API Calls
-------------
~~~~~~~~~
Function ``forecastOfWeek`` handles all request parameters and returns a ``forecastOfWeek`` object.

.. code:: python

	from darksky import forecast
	from datetime import date, timedelta

	def forecastOfWeek(city, geo):
    	days = []
    	weekday = date.today()
    	with forecast("YOUR API KEY", *geo) as sp:
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
~~~~~~~~~

The forecast of week can receive weather forecast in any location on the earth. 
The flexible algorithm of weather calculation provides weather data not only 
for cities but for any geographic coordinates (latitude and longitude) and 
can get a forecast data for the next 7 days.

Parameters:
*  **key** - Your API key from https://darksky.net/dev/.
*  **geo** - The geographic coordinates: latitude and longitude of the location for the forecast
*  **date** - The forecast data for the next 7 days
*  **city** - The geographic coordinates
*  **mintemp** - The minimun temperature in Celsius
*  **maxtemp** - The maximun temperature in Celsius

~~~~~~~~~~~~~
.. code:: python

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
~~~~~~~~~~~~~~~~~~

For Data Engineers
------------------

The csvs folder is created

~~~~~~~~~~~~~~~~~~
.. code:: python

  import util, os

  ROOT_DIR = "%s/forecast" % os.path.dirname(
      os.path.dirname(os.path.abspath(__file__))
  )

  def initDir():
      if not os.path.isdir("%s/%s" % (ROOT_DIR, "csvs")):
          os.mkdir("%s/%s" % (ROOT_DIR, "csvs"))
        

And the csv files are stored in csvs folder per day.

.. code:: python
    
  def createCsv(data, columns=None):
      df = pd.DataFrame(data, columns=columns)
      df.to_csv(
          "csvs/data_%s.csv" % (str(date.today()).replace("-", "_")),
          header=True,
          index=False,
          sep=";",
      )
~~~~~~~~~~~~~~~~~~

Example script
--------------
~~~~~~~~~~~~~~~~~~
.. code:: python

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
~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~
Output:

::

Date;City;MinTemp;MaxTemp
20/Oct/2019;SP;14;21
21/Oct/2019;SP;13;21
22/Oct/2019;SP;15;25
23/Oct/2019;SP;16;23
24/Oct/2019;SP;16;27
25/Oct/2019;SP;18;28
26/Oct/2019;SP;18;28
27/Oct/2019;SP;18;29
20/Oct/2019;RJ;20;25
21/Oct/2019;RJ;18;25
22/Oct/2019;RJ;19;27
23/Oct/2019;RJ;21;26
24/Oct/2019;RJ;21;28
25/Oct/2019;RJ;21;29
26/Oct/2019;RJ;22;29
27/Oct/2019;RJ;22;29
