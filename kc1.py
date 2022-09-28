import pandas as pd
import requests
response = requests.get("http://api.zippopotam.us/us/90210")
jsondata = response.json()
df = pd.DataFrame.from_dict(jsondata)
places = jsondata['places']
df2 = pd.DataFrame.from_dict(places)
new_df = pd.DataFrame.join(df, df2)
print(new_df['latitude'])
print(new_df['longitude'])
print(new_df.query('state == "California"'))
print(new_df[["country", "country abbreviation"]])
# think this is correct for the 4 rows, do not have 4 rows of data though!
print(new_df.iloc[0:3])