from flask import Flask, render_template, redirect, url_for, jsonify
from tester.runner import execute_run
from storage import save_run, list_runs

app = Flask(__name__)

@app.route('/')
def index():
    # Redirige la page d'accueil directement vers le dashboard
    return redirect(url_for('dashboard'))

@app.route('/run')
def trigger_run():
    # 1. Exécuter tous les tests
    run_data = execute_run()
    # 2. Sauvegarder les résultats dans la base SQLite
    save_run(run_data)
    # 3. Rediriger vers le dashboard pour voir le résultat
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    # Récupérer l'historique des tests depuis la base de données
    runs = list_runs()
    return render_template('dashboard.html', runs=runs)

# Bonus : Route de santé de l'application
@app.route('/health')
def health():
    return jsonify({"status": "ok", "api": "Quotable"})
    
@app.route('/debug')
def debug():
    from tester.client import call_api
    resp, lat, err = call_api("GET", "/random")
    return jsonify({"erreur_reseau": err, "latence": lat})
