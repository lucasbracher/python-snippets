import re
'''
    Reads as input a number between -99999 and 99999, and write it in full in Portuguese.

    Recebe como entrada um número entre -99999 e 99999 e o escreve por extenso em português.
'''
def extenso(s):
    u = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
         "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete",
         "dezoito", "dezenove"]
    d = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta",
         "setenta", "oitenta", "noventa"]
    c = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos",
         "setecentos", "oitocentos", "novecentos" ]

    n = int(s)
    menos = False
    if s[0] == "-":
        menos = True
        n = -n
    if n == 0:
        return "zero"
    if n  == 100:
        return "menos cem" if menos else "cem"
    if n >= 1000:
        pnm = [n // 1000, n % 1000]
    else:
        pnm = [n]
    psm = []

    i = 0
    for parte in pnm:
        ps = []
        ps.append(c[parte // 100])
        if parte % 100 < 20:
            if len(pnm) == 2 and i == 0 and parte == 1:
                ps.append("")
            else:
                ps.append(u[parte % 100])
        else:
            ps.append(d[(parte % 100) // 10])
            ps.append(u[(parte % 100) % 10])
        res = " e ".join(ps)
        res = re.sub("(^ e | e $)", "", res)
        psm.append(res)
        i += 1

    if len(psm) == 2 and psm[0] == "um":
        psm[0] == ""
    res = " mil e ".join(psm)
    res = re.sub("( e ?$|^ )", "", res)
    return "menos "+res if menos else res

