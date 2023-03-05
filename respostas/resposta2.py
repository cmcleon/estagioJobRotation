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

