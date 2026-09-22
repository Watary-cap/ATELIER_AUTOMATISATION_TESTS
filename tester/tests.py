from tester.client import call_api

def run_all_tests():
    results = []
    
    # 1. Test du statut HTTP 200 sur /random
    resp, lat, err = call_api("GET", "/random")
    status = "PASS" if not err and resp.status_code == 200 else "FAIL"
    results.append({"name": "GET /random retourne 200", "status": status, "latency_ms": lat})

    # 2. Test du Content-Type (doit être JSON)
    is_json = not err and "application/json" in resp.headers.get("Content-Type", "")
    status = "PASS" if is_json else "FAIL"
    results.append({"name": "Content-Type est JSON", "status": status, "latency_ms": lat})

    data = resp.json() if is_json else {}

    # 3. Test de la présence du champ obligatoire 'content'
    status = "PASS" if "content" in data else "FAIL"
    results.append({"name": "Champ 'content' présent", "status": status, "latencyOui, tu peux tout à fait commiter ton fichier `client.py`. Voici les commandes exactes à taper dans ton terminal et la suite logique de ton flux de travail :

1. **Ajouter le fichier (le préparer pour le commit) :**
   ```bash
   git add client.py
