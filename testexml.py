import xmltodict

with open('nf001.xml', 'rb') as arquivo:
    documento = xmltodict.parse(arquivo)
#print(documento)
dic_notafiscal = documento['nfeProc']['NFe']['infNFe']

nfnumero = dic_notafiscal['ide']['nNF']
natoperacao = dic_notafiscal['ide']['natOp']
comprador = dic_notafiscal['dest']['xNome']
cidade = dic_notafiscal['dest']['enderDest']['xMun']
estado = dic_notafiscal['dest']['enderDest']['UF']
produto = dic_notafiscal['det']['prod']['xProd']
qtde = dic_notafiscal['det']['prod']['qCom']
vlunitproduto = dic_notafiscal['det']['prod']['vUnCom']
vltotalprod = dic_notafiscal['det']['prod']['vProd']
vlfrete = dic_notafiscal['det']['prod']['vFrete']
vltotalnf = dic_notafiscal['total']['ICMSTot']['vNF']


print(f'''Nº NF: {nfnumero}
NAT. OPERAÇÃO: {natoperacao}
COMPRADOR: {comprador}
CIDADE: {cidade}
ESTADO: {estado}
PRODUTO: {produto}
QUANTIDADE: {qtde}
VALOR UNITÁRIO: {vlunitproduto}
VALOR TOTAL PRODUTOS: {vltotalprod}
VALOR FRETE: {vlfrete}
VALOR TOTAL DA NOTA: {vltotalnf}
''')
