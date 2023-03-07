#RESPOSTA 2
#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
#IMPORTANTE:Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código

n = int(input("Que termo deseja encontrar: "))
n1=0
n2=1
sequencia=[0]

if n<0:
    print("Para Sequência de Fibonacci, apenas números inteiros! Por favor, inicie com outro número.")
else:
    for count in range(0,n):
            termo = n1 + n2
            n2 = n1
            n1 = termo
            count += 1

            sequencia.append(termo) 
            

    print("Sequência de Fibonacci:",sequencia)

    if n in sequencia:
        print ("O número informado PERTECNE a sequencia de Fibonacci.")
    else:
        print("O número informado NÃO PERTENCE a sequencia de Fibonacci.")

