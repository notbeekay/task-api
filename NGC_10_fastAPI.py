# import package
from fastapi import FastAPI, Request, Header, HTTPException
import pandas as pd

# Create a FastAPI() object
app = FastAPI()

weather_data = {
    "New York City": {"temperature": "15°C", "condition": "Sunny"},
    "Los Angeles": {"temperature": "22°C", "condition": "Clear"},
    "Chicago": {"temperature": "10°C", "condition": "Cloudy"}
}

API_KEY = "password"

# Endpoint to provide weather data
@app.get("/weather/{location}")
def get_weather(location):
    if location not in weather_data:
        raise HTTPException(status_code=404, detail="Location not found")
    return weather_data[location]



# Endpoint for API KEY authentication
@app.get("/authenticate")
def authenticate(api_key: str = Header(None)):
    # check api_key
    if api_key != API_KEY or api_key == None:
       raise HTTPException(detail = "Invalid API Key", status_code=401)
    return{
       "message" : "API Key is valid"
    }
