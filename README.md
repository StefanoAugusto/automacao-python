# <center>  Automação em Python </center>
Automação em Python que seleciona os dados específicos em uma base de dados web, processando suas informações, disponibilizando o total de consumidores por Estado, indicando:
* Quantos consumidores tem por Estado; 
* Quantos consumidores tem por Cidade.

O dataframe com os dados ficam salvos na pasta ```/saída```.

Base de dados utilizada: ```https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce```

## <center> Como executar a automação </center>
Para rodar a automação, é necessário ter instalado além da linguagem ```Python``` e o ```PIP```, também as bibliotecas ```Pandas```, ```Kaggle``` e ```smtplib```. 
<br> Instalando as bibliotecas:

```pip install pandas```
<br> ```pip install kaggle```
<br> ```pip install smtplib```

Antes de executar o projeto, também devem ser alterados os valores das variáveis no arquivo ```dados.py```.
* Assunto;
* Corpo do e-mail;
* Servidor que enviará o E-mail;
* E-mail remetente;
* Senha;
* Porta do servidor;
* Lista de destinatários.

Após as alterações, é necessário abrir o prompt de comando dentro da pasta principal do projeto e executar o comando:

```py main.py```

## <center> Autor
A solução foi criada por: **Stefano Augusto Mossi**.
	
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://br.linkedin.com/in/stefano-augusto-mossi-6525aa217)