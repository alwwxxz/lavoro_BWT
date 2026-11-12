def bwt_transform(testo):
    testo += "$"
    lung = len(testo)
    rotazioni = []
    for i in range(lung):
        rotazione = testo[i:] + testo[:i]  # crea le rotazioni
        rotazioni.append(rotazione)

    rotazioni.sort()  # mette in ordine alfabetico

    bwt = ""
    for rot in rotazioni:
        bwt += rot[-1]  # prende l'ultima colonna

    return bwt