from herbie import Herbie
import pandas as pd
import csv
import random
df = pd.read_csv('wildfiredataset.csv')
value = df.loc[10, 'AcresBurned']
randFires = [random.randint(0, len(df.loc[:])) for i in range(250)]
randFires = list(set(randFires))
loc = (35.4676, -97.5164)

points = pd.DataFrame(
    {
        "latitude": [loc[0]],
        "longitude": [loc[1]],
        "stid": ["Location"],
    }
)
hour = 0
model = "2024-05-06 12:00"
H = Herbie(model, model="hrrr", fxx=hour, product="prs")
edata = {}
print(H)
data = H.xarray("(?:GUST:surface|:TMP:2 m|:RH:2 m)", remove_grib=False)\
# Extract wind and humidity data
matched = data[0].herbie.pick_points(points)
edata["temp"] = ((matched.t2m.values[0] - 273.15) * (9/5)) + 32
edata["rh"] = (matched.r2.values[0])

# Extract wind gust data
matched = data[1].herbie.pick_points(points)
edata["gust"] = (matched.gust.values[0] * 1.15078)
print(edata)
