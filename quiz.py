print('Seja bem-vindo ao quiz!')
resposta = input('Quer começar?(S/N)')
if resposta == 'S':
    print('Começando...')
elif resposta == 'N':
    quit()
score = 0

print('Qual menor país do mundo? \n (A) Vaticando\n (B) Mônaco\n (C) Nauru\n (D) Tuvalu')
resposta1 = input('Resposta: ')

if resposta1 == 'A':
    print('Correto!')
    score += 1
else:
    print('Incorreto!')
print('Quantos estados tem o Brasil? \n (A) 24\n (B) 25 estados e 1 distrito\n (C) 26 estados e 1 distrito\n (D) Nenhuma das anteriores')
resposta2 = input('Resposta: ')

if resposta2 == 'C':
    print('Correto!')
    score += 1
else:
    print('Incorreto!')

print('Sua pontuação foi de {}/2'.format(score))
