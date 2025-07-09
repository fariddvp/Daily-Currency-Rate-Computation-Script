import requests

def fetch_currency_rates(api_key, base_url):
    """
    Fetches the latest currency rates from the Fixer API.

    Args:
        api_key (str): Your Fixer API key.
        base_url (str): The base URL for the Fixer API (e.g., https://data.fixer.io/api/latest).

    Returns:
        dict: A dictionary containing API response, with 'success' flag.
    """
    try:
        # Base URL should NOT include API key directly
        url = f"{base_url.rstrip('/')}/latest"
        params = {
            "access_key": api_key
        }

        response = requests.get(url, params=params, timeout=5)

        # If the response is valid JSON and success = False (e.g., invalid key), return it anyway
        data = response.json()
        return data

    except requests.exceptions.Timeout:
        return {
            "success": False,
            "error": "Request timed out while fetching currency rates."
        }

    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": f"Request error: {str(e)}"
        }

    except Exception as e:
        return {
            "success": False,
            "error": f"Unexpected error: {str(e)}"
        }
