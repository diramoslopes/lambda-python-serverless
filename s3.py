import boto3

sessao = boto3.Session(profile_name='dinfracloud')
cliente_s3 = sessao.client('s3')

nome_bucket = 'serverless-curso-python-aws' 

try:
    resposta_bucket = cliente_s3.create_bucket(
        Bucket=nome_bucket,   
        CreateBucketConfiguration={
            'LocationConstraint': 'us-east-2'
        }
    )
    #print(resposta_bucket)
except Exception as error:
    print(f'Este bucket já existe')
    #print(error)

cliente_s3.upload_file(
    r'c:\Users\seu-user-name\Documents\github-clones\lambda-python-serverless\aws_light_theme_logo.svg', 
    nome_bucket, 
    'imagens/aws_logo.svg')

planilha = """
    Nome\tNota
    Diogo\t10
    Maria\t9
    João\t8
    Ana\t7
"""

cliente_s3.put_object(
    Body=planilha,
    Bucket=nome_bucket,     
    Key='planilhas/planilha.xls'
)