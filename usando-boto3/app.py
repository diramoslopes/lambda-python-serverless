import boto3

# print(boto3)
# utilizando profile dinfracloud para listar os buckets
# boto3 é a biblioteca oficial da AWS para Python
sessao = boto3.Session(profile_name='dinfracloud')
cliente_s3 = sessao.client('s3')
lista_buckets = cliente_s3.list_buckets()
print(lista_buckets)

#session, client e resource
# session: é a sessão que você cria para se conectar à AWS, se voce nao criar uma sessão, o boto3 irá usar a sessão padrão
# client: é a interface de baixo nível para interagir com os serviços da AWS
# resource: é uma interface de alto nível para interagir com os serviços da AWS