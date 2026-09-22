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
    results.append({"name": "Champ 'content' présent", "status": status, "latency_ms": lat})

    # 4. Test du type : 'author' est une chaîne de caractères
    status = "PASS" if isinstance(data.get("author"), str) else "FAIL"
    results.append({"name": "Champ 'author' est un texte", "status": status, "latency_ms": lat})

    # 5. Test du type : 'length' est un entier
    status = "PASS" if isinstance(data.get("length"), int) else "FAIL"
    results.append({"name": "Champ 'length' est un entier", "status": status, "latency_ms": lat})

    # 6. Robustesse : Erreur 404 sur un endpoint invalide
    resp_404, lat_404, err_404 = call_api("GET", "/endpoint_invalide")
    status_404 = "PASS" if not err_404 and resp_404.status_code == 404 else "FAIL"
    results.append({"name": "Erreur 404 gérée", "status": status_404, "latency_ms": lat_404})

    return results
