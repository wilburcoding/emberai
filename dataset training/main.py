from herbie import Herbie
import pandas as pd
import csv
import random
df = pd.read_csv('wildfiredataset.csv')
randFires = [random.randint(800, len(df.loc[:])) for i in range(250)]
randFires = sorted(list(set(randFires)))
for i in range(len(randFires)):
  item = randFires[i]
  value = df.loc[item, 'AcresBurned']
  loc = (df.loc[item, 'Latitude'], df.loc[item, 'Longitude'])
  print("Loading " + str(i) + "/250")
  start = (df.loc[item,'Started'])
  if (loc == (0,0)):
    print("No location found for fire #" + str(item))
    continue
  else:
    print("Location: " + str(loc))


  points = pd.DataFrame(
      {
          "latitude": [loc[0]],
          "longitude": [loc[1]],
          "stid": ["Location"],
      }
  )
  hour = 0
  try:
    model = start.split("T")[0] + " " + start.split("T")[1].split(":")[0] + ":00"
    print(model)
    H = Herbie(model, model="hrrr", fxx=hour, product="prs")
    edata = {}
    data = H.xarray("(?:TMP:2 m|:RH:2 m)", remove_grib=True)
    # Extract wind and humidity data
    matched = data.herbie.pick_points(points)
    edata["temp"] = ((matched.t2m.values[0] - 273.15) * (9/5)) + 32
    edata["rh"] = (matched.r2.values[0])
    print("ea")
    data = H.xarray(":WIND:10 m", remove_grib=True)
    print(data)
    # Extract wind data
    matched = data.herbie.pick_points(points)
    edata["wind"] = (matched.si10.values[0] * 2.23694)
    print(edata)
    with open("dataset.csv", "a", newline="") as file:
      writer = csv.writer(file)
      writer.writerow([model, loc[0],loc[1], value,edata["temp"], edata["rh"], edata['wind']])

  except Exception as e:
    print("Error: " + str(e))
    continue
  