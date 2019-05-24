#Bruno Henrique - RA:  1700431

def por_andares(arvore):
    resposta = []
    fila= Fila()
    if arvore == {}:
        return []
    resposta.append(arvore['raiz'])
    fila.insere(arvore)
    while fila.tamanho() > 0:
        arvore_atual= fila.retira()
        esquerda= arvore_atual['esquerda']
        if esquerda != {}:
            resposta.append(esquerda['raiz'])
            fila.insere(esquerda)
        direita= arvore_atual['direita']
        if direita != {}:
            resposta.append(direita['raiz'])
            fila.insere(direita)
            
    print(arvore)
