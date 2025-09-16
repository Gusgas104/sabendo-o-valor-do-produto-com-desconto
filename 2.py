produto = float(input('Qual é o valor do produto? R$'))
v = produto - (produto * 5 / 100)
p = produto + (produto * 10 / 100)
print('O produto no valor de R${}, á vista tem desconto de 5% e fica no preço de R${:.2f}, /ne o produto parcelado tem um aumento de 10% ficando no valor de R${:.2f}'.format(produto, v, p))