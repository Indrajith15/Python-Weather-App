# 🌦️ Python Weather App

A Python command-line Weather App that fetches real-time weather data using the OpenWeatherMap API.

## Features

- Get real-time weather by city
- Temperature
- Feels Like Temperature
- Humidity
- Weather Condition
- Weather Description
- Wind Speed
- Country
- Handles invalid city names
- Secure API key using `.env`

## Technologies Used

- Python
- Requests
- python-dotenv
- OpenWeatherMap API

## Installation

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
API_KEY=YOUR_API_KEY
```

Run:

```bash
python weather.py
```

## Example Output

```text
========== Weather Report ==========
City        : Kochi, IN
Temperature : 27.4 °C
Feels Like  : 29.0 °C
Humidity    : 81 %
Weather     : Clouds
Description : broken clouds
Wind Speed  : 3.4 m/s
====================================
```
