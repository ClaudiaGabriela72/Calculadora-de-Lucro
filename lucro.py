# definindo as variaveis
preco_compra = float(input('Digite o preço da compra: '))
preco_venda = float(input('Digite o preço da venda: '))
custos_adicionais = float(input('Digite os custos adicionais (opicional): '))

# Calculando o resultado
lucro = preco_venda - preco_compra - custos_adicionais


print('O lucro é de : R$ {:.2f}'.format(lucro))

# calculando a margem de lucro
margem_lucro = (lucro/preco_venda) * 100

#imprimindo o resultado
print('A margem de lucro é de {:.2f}%'.format(margem_lucro))