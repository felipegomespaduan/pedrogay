import random
pontos_seus = 0
pontos_deles = 0
while True:

  cor_secreta = random.choice(['R', 'G', 'B'])
  palpite = input("adivinha a cor (R, G, ou B): ").upper()
  if palpite not in ['R', 'G', 'B']:
    print("entrada inválida. Escolha R, G ou B.")
  elif palpite == cor_secreta:
    print("acertou")
    pontos_seus = pontos_seus + 1
  else:
    print("erro")
    pontos_deles = pontos_deles + 1
    print(' a cor era', cor_secreta)
    print(f'vc {pontos_seus} x pc {pontos_deles}')