import pandas as pd
import smtplib, os
from dados import email, senha, smtpServer, destino, porta, assunto, corpoEmail
from email.message import EmailMessage

def fazContagem(df, uf, diretorioSaida):
    for estado in uf:
        dfEstado = df[df['customer_state'] == estado]
        arquivoSaida = diretorioSaida + estado.upper() + '.csv'
        contagemCidade = dfEstado['customer_city'].value_counts().reset_index()
        dfSaida = pd.DataFrame({
            'Estado': [estado] * len(contagemCidade),
            'Cidade': contagemCidade['customer_city'],
            'Total de Consumidores': contagemCidade['count'],
        })

        contagemEstado = dfSaida['Total de Consumidores'].sum()
        totalEstado = pd.DataFrame({
            'Estado': estado,
            'Cidade': 'total de consumidores no estado',
            'Total de Consumidores': [contagemEstado],
        })

        dfSaida = pd.concat([dfSaida, totalEstado])
        dfSaida.to_csv(arquivoSaida, index=False)

def enviarEmail(uf):
    mensagem = EmailMessage()
    mensagem['Subject'] = assunto
    mensagem['From'] = email
    mensagem['To'] = destino
    mensagem.set_content(corpoEmail)
    anexos = ["saida/" + f"{estado.upper()}.csv" for estado in uf]
    try:
        for anexo in anexos:
            with open(anexo, 'rb') as f:
                leArquivo = f.read()
                nomeArquivo = os.path.basename(anexo)
            mensagem.add_attachment(leArquivo, maintype='text', subtype='csv', filename=nomeArquivo)

        server = smtplib.SMTP(smtpServer, porta)
        server.starttls()
        server.login(email, senha)
        server.send_message(mensagem)
        server.quit()
        print("E-Mail Enviado!")
    except Exception as erro:
        print("Ocorreu um erro ao enviar o e-mail: ", str(erro))



