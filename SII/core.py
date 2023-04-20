import locale

import requests
from bs4 import BeautifulSoup

# Set the locale to Spanish to parse the dates in Spanish format
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')


def get_html_content(url):
    """
    Retrieve the HTML content of a web page given its URL.

    Args:
    url (str): The URL of the web page to retrieve.

    Returns:
    bytes: The raw HTML content of the web page as a bytes object.
    If an error occurs while retrieving the web page, None is returned.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    elif response.status_code == 404:
        raise Exception('The UF webpage for the specified year could not be found.')


def extract_uf_table(html, month_id):
    """
    Extract the table of the UF (Unidad de Fomento) values for a given month from the HTML content of a web page.

    Args:
    html (bytes): The raw HTML content of the web page as a bytes object.
    month_id (str): The ID of the HTML element that contains the UF table for the desired month.

    Returns:
    list of dict: A list of dictionaries representing each row of the UF table,
    where each dictionary has two keys: 'Day' for the date and 'UF' for the UF value.
    If the UF table cannot be found in the HTML content, None is returned.
    """
    soup = BeautifulSoup(html, 'html.parser')
    div_month = soup.find('div', {'id': month_id})
    if div_month:
        table = div_month.find('table')
        rows = table.find_all('tr')
        data = []
        for row in rows[1:]:  # Skip header
            headers = row.find_all('th')
            cells = row.find_all('td')
            for i in range(len(headers)):
                date = headers[i].text.strip()
                value = cells[i].text.strip()
                if date and value:
                    data.append({date: value})
        return data
    return None
