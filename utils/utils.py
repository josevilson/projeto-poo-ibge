def ajustar_selecao(selecao_usuario: list) -> str:
    """
        Recebe uma lista de inputs do usuário e transforma em string.

    Attributes:
        selecao_usuario (list): Inputs da camada de interface.

    Returns:
        selecao_ajustado: Retorna uma string para inserir 
        no Url da requisição da API.
    """
    selecao_ajustado = []
    for p in selecao_usuario:
        p = p.split('-')[0].strip()
        print(p)
        selecao_ajustado.append(p)

    return selecao_ajustado
