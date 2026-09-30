# 🟧 SEMAINE 3 : ORDRE ET STRUCTURE (ANNUAIRE)
# 🤲 Niyyah : Organiser l'information avec clarté et respect (Ihsan).

# Création d'un annuaire structuré (Dictionnaire)
annuaire = {
    "Yamina": "0123456789",
    "Ahmed": "0987654321",
    "Sophie": "0612345678"
}

def rechercher_contact(nom):
    """
    Recherche un contact avec bienveillance et précision.
    """
    # 🛡️ RESPECT : Vérifier si le nom existe avant d'accéder
    if nom in annuaire:
        numero = annuaire[nom]
        print(f"✅ Contact trouvé : {nom} - {numero}")
    else:
        print(f"❌ Contact '{nom}' introuvable. Vérifiez l'orthographe avec soin.")

# Test de la fonction
rechercher_contact("Yamina")
rechercher_contact("Inconnu")
