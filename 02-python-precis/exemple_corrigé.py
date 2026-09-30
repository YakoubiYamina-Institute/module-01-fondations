# 🟧 SEMAINE 2 : PRÉCISION DU LANGAGE (MOYENNE)
# 🤲 Niyyah : Chercher la justesse et éviter le gaspillage de ressources.

notes = [12, 15, 8, 18, 14]

# 🛡️ SECURITY : Vérifier si la liste n'est pas vide (Éviter division par zéro)
if len(notes) > 0:
    somme = sum(notes)
    compteur = len(notes)
    
    # ⚖️ JUSTICE : Calcul précis de la moyenne
    moyenne = somme / compteur
    
    print(f"📊 Moyenne de {compteur} notes : {moyenne:.2f}/20")
else:
    print("⚠️ Attention : Aucune donnée à analyser. La précision exige des faits.")
