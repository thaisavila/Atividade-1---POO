import math

def distancia(p1,p2):
  return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
#calcula a distância entre dois pontos

def coordenada(indice, nome_ponto):
  while True:
      x = float(input(f'Digite a coordenada x {indice}: '))
      y = float(input(f'Digite a coordenada y {indice}: '))
      return (x,y)

def triangulo(a,b,c):
  lados = sorted([round(a,6) , round(b,6) , round(c,6)])

  if lados[0] + lados[1] <= lados[2]:
    print('Não é um triângulo')
    return

  if lados[0] == lados[2]:
    print('Triângulo equilátero, pois possui os três lados de mesma medida.')
  elif lados[0] == lados[1] or lados[1] == lados[2]:
    print('triângulo isósceles')
  else:
    print('Triângulo escaleno')

def quadrilatero(pontos):
    lados = [
        distancia(pontos[0], pontos[1]), # Lado 1-2
        distancia(pontos[1], pontos[2]), # Lado 2-3
        distancia(pontos[2], pontos[3]), # Lado 3-4
        distancia(pontos[3], pontos[0])  # Lado 4-1
    ]
    diagonais = [
        distancia(pontos[0], pontos[2]), # Diagonal 1-3
        distancia(pontos[1], pontos[3])  # Diagonal 2-4
    ]
    l = [round(l,6) for l in lados]
    d = [round(d,6) for d in diagonais]

    lados_iguais = (l[0] == l[1] and l[1] == l[2] and l[2] == l[3])
    diagonais_iguais = (d[0] == d[1])
    lados_opstos_iguais = (l[0] == l[2] and l[1] == l[3])

    if lados_iguais and diagonais_iguais:
        print('Quadrado')
    elif diagonais_iguais and lados_opstos_iguais:
        print('a figura é um retângulo')
    else:
      print('a figura é outro tipo de quadrilátero')

def principal():
    while True:
        escolha = input("Você deseja inserir 3 ou 4 coordenadas?: ")
        if escolha in ('3', '4'):
            num_pontos = int(escolha)
            break
        else:
            print("Erro! Digite '3' ou '4'.")

    if num_pontos == 3:
        p1 = coordenada(1, 'Ponto A')
        p2 = coordenada(2, 'Ponto B')
        p3 = coordenada(3, 'Ponto C')

        lado_a = distancia(p1, p2)
        lado_b = distancia(p2, p3)
        lado_c = distancia(p3, p1)

        triangulo(lado_a, lado_b, lado_c)

    elif num_pontos == 4:
        # Coleta 4 pontos (P1, P2, P3, P4)
        p1 = coordenada(1, 'Ponto A')
        p2 = coordenada(2, 'Ponto B')
        p3 = coordenada(3, 'Ponto C')
        p4 = coordenada(4, 'Ponto D')

        pontos = [p1, p2, p3, p4]

        # Classifica o quadrilátero
        quadrilatero(pontos)

if __name__ == "__main__":
    principal()