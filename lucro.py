preco_compra = float(input('Digite o preço da compra: '))
preco_venda = float(input('Digite o preço da venda: '))
custos_adicionais = float(input('Digite os custos adicionais (opicional): '))
lucro = preco_compra - preco_venda - custos_adicionais

print('O lucro é de : R$ {:.2f}'.format(lucro))