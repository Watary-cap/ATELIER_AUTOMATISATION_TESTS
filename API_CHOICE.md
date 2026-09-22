# API Choice

- Étudiant : Valente Matéo
- API choisie : Quotable
- URL base : [https://api.quotable.io](https://api.quotable.io)
- Documentation officielle / README : [https://github.com/lukePeavey/quotable] (https://github.com/lukePeavey/quotable)
- Auth : None / API Key / OAuth
- Endpoints testés :
  - GET /random (Récupère une citation aléatoire)
  - GET /quotes (Récupère une liste paginée de citations)
- Hypothèses de contrat (champs attendus, types, codes) :
  Code HTTP attendu : 200 (succès) ou 404 (mauvais endpoint/paramètre)
  Format de réponse : Content-Type: application/json.
  Champs obligatoires pour /random : _id (string), content (string), author (string), length (integer).
- Limites / rate limiting connu : content-type: Pas de limite stricte documentée (API ouverte), mais nécessite une utilisation raisonnable (fair-use) pour éviter un blocage de l'IP. L'approche de l'atelier (1 run/5min) est largement dans les clous.
- Risques (instabilité, downtime, CORS, etc.) : C'est une API communautaire hébergée gratuitement, le risque principal est le downtime (serveur inaccessible temporairement) ou des temps de réponse (latence) parfois très longs. Pas de problème de CORS car les requêtes seront faites côté serveur (via Python/requests) et non depuis un navigateur.
