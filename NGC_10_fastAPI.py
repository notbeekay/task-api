# import package
from fastapi import FastAPI, HTTPException, Header
import pandas as pd

# API Key for authentication
API_KEY = "password"  # Replace with your actual API key

# Create and populate DataFrame
data = {
    "Location": ["New York City", "Los Angeles", "Chicago"],
    "Temperature": ["15°C", "22°C", "10°C"],
    "Condition": ["Sunny", "Clear", "Cloudy"]
}
df = pd.DataFrame(data)

# Create a FastAPI() object
app = FastAPI()

# Endpoint to provide weather data
@app.get("/weather/{location}")
def get_weather(location: str, api_key: str = Header(None)):
    # Check if API key is valid
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    # Check if location is in the DataFrame
    if location not in df['Location'].values:
        raise HTTPException(status_code=404, detail="Location not found")
    
    # Filter DataFrame based on location
    result = df.query(f"Location == '{location}'")
    
    # Convert result to dictionary and return
    return result.to_dict(orient="records")[0]  # Return the first record

# Endpoint for API Key authentication
@app.get("/authenticate")
async def authenticate(api_key: str = Header(None)):
    # Check if API key is valid
    if api_key != API_KEY or api_key is None:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    return {"message": "API Key is valid"}
