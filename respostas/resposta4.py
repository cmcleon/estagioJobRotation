#RESPOSTA 3
#Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#SP - R$67.836,43;RJ - R$36.678,66, MG - R$29.229,88, ES - R$27.165,48, Outros - R$19.849,53
#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
print('FATURAMENTO DISTRIBUIDORA ')
estados=['SP','RJ','MG','ES','Outros']
fat=list()

for i in estados:
    v=float(input(f'Digite o valor do faturamento mensal de {i} = R$ '))
    if v<0:
        print('Digite um valor válido.')
    fat.append(v)

fat_total=sum(fat)

print('\nFaturamento total= R$', fat_total,'\n')
'\n'

cont=0
for x in fat:
    cont += 1
    percent=((x / fat_total) *100)

    print(f'O percentual de faturamento de {estados[cont-1]} foi R$ {percent:.2f}%')