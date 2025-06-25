import json

log = "-- Log do sistema --\n"
log += "Abrindo arquivo JSON\n"

arquivo = open('dados.json', 'r')  # r = read = ler , quando não especificamos o caminho , ele procurar o arquivo na raiz do projeto
info = arquivo.read()
# print(info)

log += "Lendo arquivo JSON\n"
dados = json.loads(info)  # json.loads() converte uma string JSON em um objeto Python

log += "Alterando endereco do objeto JSON\n"
dados['endereco'] = 'Rua Nova, 123'  # Modificando o valor do campo 'endereco'

novo_arquivo = open('dados_novo.json', 'w')  # w = write = escrever
novos_dados = json.dumps(dados)  # json.dumps() converte um objeto Python em uma string JSON
novo_arquivo.write(novos_dados) 

novo_arquivo.close # json.dumps() converte um objeto Python em uma string JSON

#------
log += "Adcionando novo objeto JSON ao final do arquivo\n"

novo_arquivo = open('dados_novo.json', 'a')  # a = append = adicionar, utilizado para incrementar dados ao final do arquivo
novo_arquivo.write('\n{"cidade": "São Paulo"}')  # Adicionando um novo objeto JSON ao final do arquivo
novo_arquivo.close()

#------
log += "Criando novo arquivo de log\n"
arquivo_log = open('arquivos\log.txt', 'w')  # w = write = escrever
arquivo_log.write(log) 
arquivo_log.close()  # Fechando o arquivo de log