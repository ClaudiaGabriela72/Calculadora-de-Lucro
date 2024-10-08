import openpyx1

# definindo as variaveis
preco_compra = float(input('Digite o preço da compra: '))
preco_venda = float(input('Digite o preço da venda: '))
custos_adicionais = float(input('Digite os custos adicionais (opicional): '))
custo_frete = float(input("Digite o custo do frete: "))
# Calculando o resultado
lucro = preco_venda - preco_compra - custos_adicionais - custo_frete


print('O lucro é de : R$ {:.2f}'.format(lucro))

# calculando a margem de lucro
margem_lucro = (lucro/preco_venda) * 100

#imprimindo o resultado
print('A margem de lucro é de {:.2f}%'.format(margem_lucro))





# Salvando resultados em uma planilha do Excel

nome_do_produto

resumo = [nome_do_produto, preco_compra, preco_venda, custos_adicionais, custo_frete, lucro, margem_lucro]


try:
    wb = openpyx1.load_workbook('planilha.xlsx')
    sheet = wb.active
except:
    wb = openpyx1.Workbook()
    sheet = wb.active
    sheet.title = "Resultado da Calculadora de lucro"

    #Adicionando cabeçalho
    sheet['A1'] = "Nome do Produto"
    sheet['B1'] = "Preco_compra"
    sheet['C1'] = "Preco_venda"
    sheet['D1'] = "Custos_adicionais"
    sheet['E1'] = "Custo_frete"
    sheet['F1'] = "Lucro líquido"
    sheet['G1'] = "Margem_lucro (%)"

# Adicionando valores a planilha
row = sheet.max_row + 1
sheet['A{}'.format(row)] = nome_do_produto
sheet['B{}'.format(row)] = preco_compra
sheet['C{}'.format(row)] = preco_venda
sheet['D{}'.format(row)] = custos_adicionais
sheet['E{}'.format(row)] = custo_frete
sheet['F{}'.format(row)] = lucro
sheet['G{}'.format(row)] = margem_lucro

# salvando a planilha