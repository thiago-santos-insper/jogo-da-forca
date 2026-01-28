# ABREVIAÇÕES

# ns = no space
# vf = verificação
# lst = lista
# frag = fragmento
# po = palavra oculta
# qtde = quantidade
# dic = dicionário

# /ABREVIAÇÕES/



# IMPORTAÇÕES

import os
from unidecode import unidecode

# /IMPORTAÇÕES/


# FUNÇÕES

def vf_letra_desejada(letra_desejada):
    while True:
        if len(letra_desejada) == 0:
            os.system("cls")
            print_interface(palavra_oculta, categoria_palavra, qtde_vidas, lst_tentativas_colorida)
            print("\033[33m" + "Inválido. Digite uma letra!" + "\033[0m", "", "", sep="\n")
            letra_desejada = input("Digite a letra desejada: ")
        elif len(letra_desejada) > 1:
            os.system("cls")
            print_interface(palavra_oculta, categoria_palavra, qtde_vidas, lst_tentativas_colorida)
            print("\033[33m" + "Inválido. Digite apenas uma letra!" + "\033[0m", "", "", sep="\n")
            letra_desejada = input("Digite a letra desejada: ")
        elif letra_desejada.isalpha() == False:
            os.system("cls")
            print_interface(palavra_oculta, categoria_palavra, qtde_vidas, lst_tentativas_colorida)
            print("\033[33m" + "Inválido. Digite uma letra do alfabeto!" + "\033[0m", "", "", sep="\n")
            letra_desejada = input("Digite a letra desejada: ")
        else:
            return letra_desejada

def print_interface(palavra_oculta, categoria_palavra, qtde_vidas, lst_tentativas_colorida):
    tentativas_str = ", ".join(lst_tentativas_colorida) if lst_tentativas_colorida else "Nenhuma"
    print(
        "",
        "",
        "---------------------------------------------",
        "",
        f"JOGO DA FORCA - {categoria_palavra}:",
        "",
        palavra_oculta,
        "",
        f"Vidas restantes: {qtde_vidas}",
        "",
        f"Tentativas: {tentativas_str}",
        "",
        "---------------------------------------------",
        "",
        sep="\n"
    )

def underlines(frag_palavra_desejada):
    frag_palavra_oculta_ns = len(frag_palavra_desejada) * "_"
    return frag_palavra_oculta_ns

def spaces(frag_palavra_oculta_ns):
    frag_palavra_oculta = " ".join(frag_palavra_oculta_ns)
    return frag_palavra_oculta

def join_po(lst_palavra_oculta):
    palavra_oculta = "  ".join(lst_palavra_oculta)
    return palavra_oculta

def inserir_texto(texto_original, inserir, posicao):
    texto_final = texto_original[:posicao] + inserir + texto_original[posicao+1:]
    return texto_final

def substituicao_palavra (palavra_desejada, palavra_oculta, letra_desejada):
    palavra_desejada = palavra_desejada.lower()
    lst_indices = []
    for i, letra in enumerate(palavra_desejada):
            if letra_desejada == letra:
                lst_indices.append(i)
    palavra_oculta_ns = "".join(palavra_oculta.split())
    for indice in lst_indices:
        nova_palavra_oculta_ns = inserir_texto(palavra_oculta_ns, letra_desejada.upper(), indice)
        palavra_oculta_ns = nova_palavra_oculta_ns
    nova_palavra_oculta = " ".join(nova_palavra_oculta_ns)
    return nova_palavra_oculta

def substituicao_lista(lst_palavra_desejada, palavra_oculta, letra_desejada):
    dic_indices = {}
    lst_palavra_oculta = palavra_oculta.split("  ")
    nova_lst_palavra_oculta_ns = []
    nova_lst_palavra_oculta = []
    for i, palavra in enumerate(lst_palavra_desejada):
        lst_indices = []
        for i2, letra in enumerate(palavra.lower()):
            if letra_desejada == letra:
                lst_indices.append(i2)
        dic_indices.update({i: lst_indices})
    for i, frag_palavra_oculta in enumerate(lst_palavra_oculta):
        frag_palavra_oculta_ns = "".join(frag_palavra_oculta.split())
        if dic_indices[i]:
            for indice in dic_indices[i]:
                novo_frag_palavra_oculta_ns = inserir_texto(frag_palavra_oculta_ns, letra_desejada.upper(), indice)
                frag_palavra_oculta_ns = novo_frag_palavra_oculta_ns  
            nova_lst_palavra_oculta_ns.append(novo_frag_palavra_oculta_ns)
        else:
            nova_lst_palavra_oculta_ns.append(frag_palavra_oculta_ns)  
        novo_frag_palavra_oculta = " ".join(nova_lst_palavra_oculta_ns[i])
        nova_lst_palavra_oculta.append(novo_frag_palavra_oculta)
    nova_palavra_oculta = join_po(nova_lst_palavra_oculta)
    return nova_palavra_oculta

def vf_conclusao():
    conclusao = palavra_oculta.find("_")
    return conclusao

# /FUNÇÕES/



# ANSI

negrito = "\033[1m"
sublinhado = "\033[4m"

red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"

reset = "\033[0m"

# /ANSI/



# FASE DO INPUT

os.system("cls")

print("\n\nJOGO DA FORCA\n")

## INPUT DA PALAVRA DESEJADA

palavra_desejada = input("Digite a palavra desejada: ")

palavra_desejada_ns = palavra_desejada.replace(" ", "").lower()
vf_palavra_desejada_alfabeto = palavra_desejada_ns.isalpha()

while len(palavra_desejada) == 0 or vf_palavra_desejada_alfabeto == False:
    if len(palavra_desejada) == 0:
        os.system("cls")
        print("\n\nJOGO DA FORCA\n")
        print(yellow + "Inválido. Digite uma palavra!" + reset)
    elif vf_palavra_desejada_alfabeto == False:
        os.system("cls")
        print("\n\nJOGO DA FORCA\n")
        print(yellow + "Palavra inválida!. Insira somente letras do alfabeto." + reset)
    palavra_desejada = input("\nDigite a palavra desejada: ")
    palavra_desejada_ns = palavra_desejada.replace(" ", "").lower()
    vf_palavra_desejada_alfabeto = palavra_desejada_ns.isalpha()

os.system("cls")

print("\n\nJOGO DA FORCA\n")
print(f"Digite a palavra desejada: {palavra_desejada}")

palavra_desejada = palavra_desejada.capitalize().strip()

## INPUT DA CATEGORIA DA PALAVRA

categoria_palavra = input("Digite a categoria da palavra: ")

while len(categoria_palavra) == 0:
    os.system("cls")
    print("\n\nJOGO DA FORCA\n")
    print(f"Digite a palavra desejada: {palavra_desejada}\n")
    print(yellow + "Inválido. Insira uma categoria!" + reset)
    categoria_palavra = input("\nDigite a categoria da palavra: ")

categoria_palavra = categoria_palavra.capitalize().strip()

os.system("cls")

# /FASE DO INPUT/



# PALAVRA x LISTA DE PALAVRAS

lst_palavra_desejada = []

if palavra_desejada.find(" ") != -1:
    lst_palavra_desejada = palavra_desejada.lower().split()

# /PALAVRA x LISTA DE PALAVRAS/



# PALAVRA OCULTA

## NO SPACE

lst_palavra_oculta_ns = []

if lst_palavra_desejada:
    for frag_palavra_desejada in lst_palavra_desejada:
        frag_palavra_oculta_ns = underlines(frag_palavra_desejada)
        lst_palavra_oculta_ns.append(frag_palavra_oculta_ns)
else:
    palavra_oculta_ns = underlines(palavra_desejada)

## SPACE

lst_palavra_oculta = []

if lst_palavra_desejada:
    for frag_palavra_oculta_ns in lst_palavra_oculta_ns:
        frag_palavra_oculta = spaces(frag_palavra_oculta_ns)
        lst_palavra_oculta.append(frag_palavra_oculta)
else:
    palavra_oculta = spaces(palavra_oculta_ns)

## JOIN

if lst_palavra_desejada:
    palavra_oculta = join_po(lst_palavra_oculta)

# /PALAVRA OCULTA/



# INTERFACE

qtde_vidas = 5
lst_tentativas = []
qtde_letras_totais = len(palavra_desejada_ns)

if lst_palavra_desejada:
    qtde_palavras = len(lst_palavra_desejada)
else:
    qtde_palavras = 1

# /INTERFACE/



# REGRA DE SUBSTITUIÇÃO

## VERIFICAÇÃO DE CONCLUSÃO

conclusao = vf_conclusao()

## WHILE

lst_tentativas_colorida = [] 

tentativas_str = "Nenhuma"
print(
    "",
    "",
    "---------------------------------------------",
    "",
    f"JOGO DA FORCA - {categoria_palavra}:",
    "",
    palavra_oculta,
    "",
    f"Vidas restantes: {qtde_vidas}",
    "",
    f"Tentativas: {tentativas_str}",
    "",
    f"Quantidade de letras: {qtde_letras_totais}",
    "",
    f"Quantidade de palavras: {qtde_palavras}",
    "",
    "---------------------------------------------",
    "",
    "",
    sep="\n"
    )

letra_desejada = input("Digite a letra desejada: ")
letra_desejada = vf_letra_desejada(letra_desejada)
letra_desejada = letra_desejada.lower()
os.system("cls")

while True:
    if letra_desejada in palavra_desejada_ns and letra_desejada.upper() not in lst_tentativas:
        if lst_palavra_desejada:
            palavra_oculta = substituicao_lista(lst_palavra_desejada, palavra_oculta, letra_desejada)
        else:
            palavra_oculta = substituicao_palavra(palavra_desejada, palavra_oculta, letra_desejada)
        lst_tentativas.append(letra_desejada.upper())
        lst_tentativas_colorida.append(green + letra_desejada.upper() + reset)
                
        conclusao = vf_conclusao()
        if conclusao == -1:
            break

        print_interface(palavra_oculta, categoria_palavra, qtde_vidas, lst_tentativas_colorida)
        print(f"A letra {green + letra_desejada.upper() + reset} foi adicionada!", "", "", sep="\n")
        letra_desejada = input("Digite a letra desejada: ")
        letra_desejada = vf_letra_desejada(letra_desejada)
        letra_desejada = letra_desejada.lower()
        os.system("cls")

    elif letra_desejada.upper() in lst_tentativas:
        print_interface(palavra_oculta, categoria_palavra, qtde_vidas, lst_tentativas_colorida)
        print(yellow + f"Inválido. Você já tentou a letra \"{blue + letra_desejada.upper() + reset}\"!" + reset, "", "", sep="\n")
        letra_desejada = input("Digite a letra desejada: ")
        letra_desejada = vf_letra_desejada(letra_desejada)
        letra_desejada = letra_desejada.lower()
        os.system("cls")
        
    elif letra_desejada in unidecode(palavra_desejada_ns):
        print_interface(palavra_oculta, categoria_palavra, qtde_vidas, lst_tentativas_colorida)
        print(yellow + "Ops! Parece que você não adicionou o caractere especial nessa letra. Tente novamente." + reset, "", "", sep="\n")
        letra_desejada = input("Digite a letra desejada: ")
        letra_desejada = vf_letra_desejada(letra_desejada)
        letra_desejada = letra_desejada.lower()
        os.system("cls")

    elif unidecode(letra_desejada) in unidecode(palavra_desejada_ns) and unidecode(letra_desejada).upper() not in palavra_oculta:
        print_interface(palavra_oculta, categoria_palavra, qtde_vidas, lst_tentativas_colorida)
        print(yellow + "Ops! Parece que você adicionou o caractere especial errado nessa letra. Tente novamente." + reset, "", "", sep="\n")
        letra_desejada = input("Digite a letra desejada: ")
        letra_desejada = vf_letra_desejada(letra_desejada)
        letra_desejada = letra_desejada.lower()        
        os.system("cls")

    else:
        qtde_vidas -= 1
        lst_tentativas.append(letra_desejada.upper()) 
        lst_tentativas_colorida.append(red + letra_desejada.upper() + reset)
        
        if qtde_vidas == 0:
            break
        
        print_interface(palavra_oculta, categoria_palavra, qtde_vidas, lst_tentativas_colorida)
        print(yellow + f"Incorreto. A palavra não possui a letra {red + letra_desejada.upper() + reset}." + reset, "", "", sep="\n")
        letra_desejada = input("Digite a letra desejada: ")
        letra_desejada = vf_letra_desejada(letra_desejada)
        letra_desejada = letra_desejada.lower()                
        os.system("cls")

# /REGRA DE SUBSTITUIÇÃO/



# FINAIS

if conclusao == -1:
    os.system("cls")
    print_interface(palavra_oculta, categoria_palavra, qtde_vidas, lst_tentativas_colorida)
    print(magenta + "Parabéns, você acertou a palavra!" + reset, "", "", sep= "\n")
else:
    os.system("cls")
    print_interface(palavra_oculta, categoria_palavra, qtde_vidas, lst_tentativas_colorida)
    print(red + "Que pena, suas vidas acabaram!" + reset, "", "", yellow + f"A palavra correta era \"{magenta + palavra_desejada.upper() + reset}\"." + reset, "", "", sep= "\n")

# /FINAIS/
