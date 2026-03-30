numero_inteiro = input("Em qual numero você está pensando? ")
numero_quebrado = input("Novamente, em qual numero você está pensando? ")

type(numero_inteiro)
type(numero_quebrado)

print(f"O seu primeiro numero é {type(numero_inteiro)} e o segundo numero é {type(numero_quebrado)}.")
# não entendi como que se usa o type, então na aula do professor eu aprendo
# o type é para mostrar o tipo da variável, ou seja, se é string, inteiro, float, etc.
# No caso, como os inputs são sempre strings, ambos numero_inteiro e numero_quebrado são do tipo string.
# Se quisermos converter numero_inteiro para um inteiro, podemos usar int(numero_inteiro), e para numero_quebrado para um float, podemos usar float(numero_quebrado).
