import requests
import time

BASE_URL = "https://api.quotable.io"
TIMEOUT_SEC = 3

def call_api(method, endpoint, params=None):
    """
    Appelle l'API avec un timeout et un mécanisme de Retry (1 tentative max).
    Retourne la réponse HTTP, le temps de réponse (en ms) et un éventuel message d'erreur.
    """
    url = f"{BASE_URL}{endpoint}"
    retries = 1
    
    for attempt in range(retries + 1):
        start_time = time.time()
        try:
            response = requests.request(method, url, params=params, timeout=TIMEOUT_SEC, verify=False)
            latency_ms = int((time.time() - start_time) * 1000)
            return response, latency_ms, None
            
        except requests.exceptions.Timeout:
            if attempt == retries:
                return None, TIMEOUT_SEC * 1000, "Timeout Error"
            time.sleep(1) # Attendre 1 seconde avant le retry
            
        except Exception as e:
            if attempt == retries:
                return None, 0, f"Connection Error: {str(e)}"
            time.sleep(1)
