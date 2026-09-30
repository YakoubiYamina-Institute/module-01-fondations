# 🟧 SEMAINE 4 : AUDIT ET AMANAH (TRANSPARENCE)
# 🤲 Niyyah : Assumer la responsabilité de chaque ligne (Amanah).

# ⚠️ IMPORTANT : Aucun mot de passe ou clé API ne doit jamais apparaître ici.
# Les secrets doivent être dans des variables d'environnement (.env).

def calculer_zakat(epargne, nisab=5000):
    """
    Calcule le Zakat (2.5%) si l'épargne dépasse le Nisab.
    Transparence totale sur le calcul.
    """
    if epargne >= nisab:
        zakat_du = epargne * 0.025
        return f"✅ Zakat dû : {zakat_du:.2f} CHF (2.5% de {epargne} CHF)"
    else:
        return "ℹ️ Épargne inférieure au Nisab. Aucun Zakat dû pour le moment."

# Exemple d'utilisation transparente
mon_epargne = 6000
print(calculer_zakat(mon_epargne))   
