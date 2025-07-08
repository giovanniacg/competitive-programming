"""
Nós somos galinhas globais
Estamos em todo o planeta
Estamos em todo o planeta
No Brasil a gente diz: galinha
Na Argentina a gente diz: gallina
No Brasil a gente diz: galinha
Na Argentina a gente diz: gallina
Na Alemanha somos huhn
Nos Estados Unidos somos hen ou chicken
Estamos em todo planeta
Estamos em todo planeta
Na França somos poule
Israel, tarnegolét
Egito somos farkha
Itália, gallina
Polônia, kura
Finlândia, kana
E no Japão é niwatori
Na Russia, kuritsa, kuritsa
Em Angola, em Angola
Tem a galinha da Angola que é cinza e branca e vive cantando assim:
Tô fraca, tô fraca, tô fraca
Tô fraca, tô fraca, tô fraca
"""

r = {
    "Brasil": "galinha",
    "Argentina": "gallina",
    "Alemanha": "huhn",
    "Estados Unidos": "hen ou chicken",
    "França": "poule",
    "Israel": "tarnegolet",
    "Egito": "farkha",
    "Itália": "gallina",
    "Polônia": "kura",
    "Finlândia": "kana",
    "Japão": "niwatori",
    "Russia": "kuritsa",
    "Angola": "to fraca"
}

country = input()

print(r[country])