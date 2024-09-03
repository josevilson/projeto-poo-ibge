def ajustar_selecao(paises):
    paises_ajustado = []
    for p in paises:
        p = p.split('-')[0].strip()
        print(p)
        paises_ajustado.append(p)

    return paises_ajustado
