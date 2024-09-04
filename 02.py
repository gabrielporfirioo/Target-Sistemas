# eu criei uma função chamada fibonacci que recebe a quantidade de numeros(n) como parametro 
# em seguida declarei as variaveis de controle iniciais e criei a variavel lista do tipo list, que ia receber os valores do loop while


def fibonacci(n):
    ultimo = 0
    penultimo = 1
    count = 3
    lista=[]
   
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count +=1 
        lista.append(termo)

    # aqui eu estou exibindo os valores que foram adicionados a list
    for i in lista:
        print(i)
    
    # so para pular linha
    print()
    # aqui eu estou conferindo se o valor do parametro n, pertence ou não a lista de fibonacci
    if n:
        print('Pertence')
    else:
        print('Não Pertence')

# aqui estou chamando a função com o parametro
fibonacci(21)





   

