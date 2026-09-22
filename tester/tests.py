from datetime import datetime, timezone
from tester.client import call_api

def execute_run():
    # Lancer tous les tests
    tests_results = run_all_tests()

    # Calculer le nombre de succès et d'échecs
    passed = sum(1 for t in tests_results if t["status"] == "PASS")
    failed = sum(1 for t in tests_results if t["status"] == "FAIL")
    total = passed + failed

    # Calcul du taux d'erreur
    error_rate = round(failed / total, 3) if total > 0 else 1.0

    # Calcul des latences (Moyenne et Percentile 95)
    latencies = sorted([t["latency_ms"] for t in tests_results])
    avg_lat = int(sum(latencies) / len(latencies)) if latencies else 0
    
    if latencies:
        p95_index = int(len(latencies) * 0.95)
        # S'assurer de ne pas dépasser la taille de la liste
        p95_index = min(p95_index, len(latencies) - 1)
        p95_lat = latencies[p95_index]
    else:
        p95_lat = 0

    # Construire la structure de données finale
    run_data = {
        "api": "Quotable",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "passed": passed,
            "failed": failed,
            "error_rate": error_rate,
            "latency_ms_avg": avg_lat,
            "latency_ms_p95": p95_lat
        },
        "tests": tests_results
    }

    return run_data
