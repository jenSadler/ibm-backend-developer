import httpx
import pandas as pd

data = httpx.get("https://official-joke-api.appspot.com/jokes/ten")

df= pd.DataFrame(data.json())

print(df[["setup","punchline"]])

