#RESPOSTA 3
#Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

with open('dados.json') as json_file:
    dados = json.load(json_file)

    minV = dados[0]
    maxV = dados[0]
    somaMedia = 0.0
    numDiasSUperiorFaturamento = 0

    #print(len(dados))
    for i in dados:
        if(i['valor'] != 0):
            somaMedia = somaMedia + i['valor']
            if(i['valor'] > maxV['valor']):
                maxV = i
            elif (i['valor'] < minV['valor']):
                minV = i
    
    media = (somaMedia/len(dados))
    
    for j in dados:
        if(j['valor'] != 0):
            if(j['valor'] > media):
                numDiasSUperiorFaturamento += 1 
    
    
    print('Menor valor de faturamento: ',minV['valor'])
    print('Maior valor de faturamento: ',maxV['valor'])
    print('Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: ',numDiasSUperiorFaturamento)
