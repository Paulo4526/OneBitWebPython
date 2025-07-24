import asyncio

#1 - Função Sincrona
def sum(a,b):
    return a + b
print(sum(2,3))

#2 - Função assincrona
async def mult(a,b):
    return a * b
res = sum(3,3)
#Evento Loop para funções assincronas
result = asyncio.run(mult(3,3))
print(result)

#3 - Função assincrona que inicializa outra função assincrona
async def getMult(a,b):
    result = await mult(a,b)
    return f'Multiplicação: {a} x {b} = {result}'
#Inicializando a variavel que recebe o valor da função acima
newMult = asyncio.run(getMult(5,6))
print(newMult)
