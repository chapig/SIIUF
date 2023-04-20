from fastapi import FastAPI

from SII import lookup_uf_date, lookup_uf_month_year

app = FastAPI()


@app.get("/date/{date}")
def read_item(date: str):
    """

    Busca el valor de la UF en una fecha específica.
    El formato de la fecha debe ser dd-mm-yyyy.

    :param date:
    :return:
    """

    try:
        data = lookup_uf_date(date=date)
        return data
    except Exception as error:
        return {"Error": str(error)}


@app.get("/{day}/{month}/{year}")
def read_item(day: int, month: int, year: int):
    """

    Busca el valor de la UF en una fecha específica.
    El formato de la fecha debe ser dia, mes y año.

    :param day:
    :param month:
    :param year:
    :return:
    """

    try:
        data = lookup_uf_month_year(day=day, month=month, year=year)
        return data
    except Exception as error:
        return {"Error": str(error)}


@app.get("/{year}")
def read_item(year: int):
    """
    :param year:
    :return:
    """
    try:
        data = lookup_uf_month_year(year=year)
        return data
    except Exception as error:
        return {"Error": str(error)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
