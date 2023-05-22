import pandas as pd

import funciones as funciones

# Prueba unitaria para la función airport_info


def test_airport_info():
    airport_code = "JFK"
    url = "https://airport-info.p.rapidapi.com/airport"

    # Realizar las pruebas con una clave de API válida
    headers = {
        "X-RapidAPI-Key": "6f294ed6f0mshd9fbb45d9c15ffbp112336jsn9ed08e8c22a6",
        "X-RapidAPI-Host": "airport-info.p.rapidapi.com",
    }

    response = funciones.airport_info(airport_code, url)

    # Verificar que la respuesta sea exitosa y contenga la información esperada
    assert response.status_code == 200
    assert "name" in response.json()
    assert "location" in response.json()

    # Verificar que la respuesta para un aeropuerto no existente sea error
    invalid_airport_code = "XYZ"
    response = funciones.airport_info(invalid_airport_code, url)
    assert response.status_code == 200
    assert "error" in response.json()

# Prueba unitaria para la función arreglar_fecha


def test_arreglar_fecha():
    # Crear dataframe de prueba
    row = {
        "WHEELSOFF": pd.Timestamp("2023-05-21 08:30:00"),
        "CRSDEPTIME": pd.Timestamp("2023-05-21 10:00:00"),
        "WHEELSON": pd.Timestamp("2023-05-21 11:00:00"),
        "CRSARRTIME": pd.Timestamp("2023-05-21 12:30:00"),
        "ARRTIME": pd.Timestamp("2023-05-21 12:15:00"),
        "DEPTIME": pd.Timestamp("2023-05-21 09:30:00"),
    }
    expected_row = {
        "WHEELSOFF": pd.Timestamp("2023-05-22 08:30:00"),
        "CRSDEPTIME": pd.Timestamp("2023-05-21 10:00:00"),
        "WHEELSON": pd.Timestamp("2023-05-22 11:00:00"),
        "CRSARRTIME": pd.Timestamp("2023-05-22 12:30:00"),
        "ARRTIME": pd.Timestamp("2023-05-22 12:15:00"),
        "DEPTIME": pd.Timestamp("2023-05-21 09:30:00"),
    }

    modified_row = funciones.arreglar_fecha(row)

    assert modified_row == expected_row

    # Segundo caso

    row_2 = {
        "WHEELSOFF": pd.Timestamp("2023-05-21 10:30:00"),
        "CRSDEPTIME": pd.Timestamp("2023-05-21 10:00:00"),
        "WHEELSON": pd.Timestamp("2023-05-21 11:00:00"),
        "CRSARRTIME": pd.Timestamp("2023-05-21 12:30:00"),
        "ARRTIME": pd.Timestamp("2023-05-21 09:45:00"),
        "DEPTIME": pd.Timestamp("2023-05-21 09:30:00"),
    }
    expected_row_2 = {
        "WHEELSOFF": pd.Timestamp("2023-05-21 10:30:00"),
        "CRSDEPTIME": pd.Timestamp("2023-05-21 10:00:00"),
        "WHEELSON": pd.Timestamp("2023-05-22 11:00:00"),
        "CRSARRTIME": pd.Timestamp("2023-05-22 12:30:00"),
        "ARRTIME": pd.Timestamp("2023-05-22 09:45:00"),
        "DEPTIME": pd.Timestamp("2023-05-21 09:30:00"),
    }

    modified_row_2 = funciones.arreglar_fecha(row_2)

    assert modified_row_2 == expected_row_2

    
