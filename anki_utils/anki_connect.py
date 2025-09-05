import requests

ANKI_CONNECT_URL = "http://localhost:8765"


# wrapper to send request to AnkiConnect
def invoke(action, **params):
    try:
        response = requests.post(
            ANKI_CONNECT_URL,
            json={"action": action, "version": 6, "params": params},
            timeout=5,
        )
    except requests.exceptions.ConnectionError:
        print(
            "ERROR: Couldn't connect to Anki. Please ensure Anki is running with AnkiConnect installed."
        )
        return None
    except requests.exceptions.Timeout:
        print("ERROR: Request to AnkiConnect timed out.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"ERROR: HTTP error: {e}")
        return None
    except Exception as e:
        print(f"ERROR: unexepected error om request {e}")
        return None

    # If no errors from AnkiConnect, parse response
    try:
        result = response.json()
        print(result)
    except ValueError:
        print("ERROR: couldn't parse response object from AnkiConnect.")
        return None

    if result.get("error"):
        print(f"ERROR: AnkiConnect error: {result['error']}")
        return None

    return result.get("result")
