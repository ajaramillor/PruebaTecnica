import logging


import pandas as pd
import requests


def airport_info(airport_code,url):
    url = url

    querystring = {"iata": airport_code}

    headers = {
        "X-RapidAPI-Key": "6f294ed6f0mshd9fbb45d9c15ffbp112336jsn9ed08e8c22a6",
        "X-RapidAPI-Host": "airport-info.p.rapidapi.com",
    }
    try:
        response = requests.get(url, headers=headers, params=querystring)

    except Exception as e:
        logging.exception(f"Se ha presentado una excepcion al consultar la API: {e}")
        return

    print(response.json())

    return response

def arreglar_fecha(row):
    if row["WHEELSOFF"] < row["CRSDEPTIME"]:
        row["WHEELSOFF"] = row["WHEELSOFF"] + pd.to_timedelta(
            1, unit="day", errors="ignore"
        )
        row["WHEELSON"] = row["WHEELSON"] + pd.to_timedelta(
            1, unit="day", errors="ignore"
        )
        row["CRSARRTIME"] = row["CRSARRTIME"] + pd.to_timedelta(
            1, unit="day", errors="ignore"
        )
        row["ARRTIME"] = row["ARRTIME"] + pd.to_timedelta(
            1, unit="day", errors="ignore"
        )
        return row
    elif row["WHEELSON"] < row["WHEELSOFF"]:
        row["WHEELSON"] = row["WHEELSON"] + pd.to_timedelta(
            1, unit="day", errors="ignore"
        )
        row["CRSARRTIME"] = row["CRSARRTIME"] + pd.to_timedelta(
            1, unit="day", errors="ignore"
        )
        row["ARRTIME"] = row["ARRTIME"] + pd.to_timedelta(
            1, unit="day", errors="ignore"
        )
        return row
    elif row["ARRTIME"] < row["WHEELSON"]:
        row["CRSARRTIME"] = row["CRSARRTIME"] + pd.to_timedelta(
            1, unit="day", errors="ignore"
        )
        row["ARRTIME"] = row["ARRTIME"] + pd.to_timedelta(
            1, unit="day", errors="ignore"
        )
        return row
    elif row["ARRTIME"] < row["WHEELSOFF"]:
        row["ARRTIME"] = row["ARRTIME"] + pd.to_timedelta(
            1, unit="day", errors="ignore"
        )
        return row
    elif row["CRSARRTIME"] < row["WHEELSOFF"]:
        row["CRSARRTIME"] = row["CRSARRTIME"] + pd.to_timedelta(
            1, unit="day", errors="ignore"
        )
        return row
    elif row["ARRTIME"] < row["DEPTIME"]:
        row["ARRTIME"] = row["ARRTIME"] + pd.to_timedelta(
            1, unit="day", errors="ignore"
        )

    return row