import boto3

sessao = boto3.Session(profile_name='dinfracloud')
cliente_s3 = sessao.client('s3')

nome_bucket = 'my-tf-test-bucket-dimais' 

# obtem um objeto do s3 e salva ele no seu disco local c, ou em uma pasta da rede
cliente_s3.download_file(   
    Bucket=nome_bucket, 
    Key='evandro2.png', 
    Filename='evandro-aniversario.png'
)

#obtem um objeto do s3 e salva ele em uma variavel, nao necessariamente no disco local
# o objeto pode ser um arquivo de texto, planilha, imagem, etc.
# voce pode manipular o conteudo do objeto depois de baixado e subir de volta para o s3
planilha_s3 = cliente_s3.get_object(
    Bucket='serverless-curso-python-aws',
    Key='planilhas/planilha.xls',
)

planilha_body = planilha_s3['Body']
planilha = planilha_body.read().decode('utf-8')
print(planilha)