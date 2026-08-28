import app as velos


def test_sante():
    client = velos.app.test_client()
    reponse = client.get("/sante")
    assert reponse.status_code == 200
    assert reponse.get_json() == {"statut": "ok", "version": "2.0"}


def test_alertes_en_memoire():
    client = velos.app.test_client()
    reponse = client.get("/alertes")
    assert reponse.status_code == 200
    corps = reponse.get_json()
    assert corps["source"] == "memoire"
    assert all(station["velos_disponibles"] <= 2 for station in corps["alertes"])
    assert {station["nom"] for station in corps["alertes"]} == {"Place du Marche", "Universite"}
