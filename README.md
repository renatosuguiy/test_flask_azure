<h1> test_flask_azure </h1>

<h2>Objetivo</h2>
Este projeto tem como objetivo criar um exemplo de como criar um Azure Function que acessa outros modulos do Azure. Todos os módulos devem estar na mesma conta. 

Para o Azure Fuctions reconhecer os requests, é necessaria a pasta "HadleApproach" e seus arquivos interno e o JSON "host.json". O  "HandleApproach" indica quais são os tipos de requests que a function vai responder e qual função do código ele vai ativar ao receber o request.

<br>

<h2>Endpoints</h2>
<hr>

<br>

<h3>/test/<'name'> </h3>
<hr>
Retorna na tela o nome que for colocado no lugar de "<name>".

<br>

<h3>/db/test_db</h3>
<hr>
Verificar se a conexão com o banco de dados está funcionando. São necessárias as variáveis de ambiente "DB_USERNAME", "DB_PASSWORD" e "DB_HOSTNAME" correspondente as configurações do banco de dados para este Endpoint funcionar. 

<br>

<h3>/db/get_one_line</h3>
<hr>
Pega uma linha da tabela "ppc_links" do banco "test_azure_db" previamente criados no Azure e retorna como JSON. São necessárias as variáveis de ambiente "DB_USERNAME", "DB_PASSWORD" e "DB_HOSTNAME" correspondente as configurações do banco de dados para este Endpoint funcionar. 

<br>

<h3>/key/create_key</h3>
<hr>
Cria uma chave no Azure KeyVault previamente criado. São necessárias as variáveis de ambiente "AZURE_CLIENT_ID", "AZURE_CLIENT_SECRET", e "AZURE_TENANT_ID". Os valores dessas chaves são criadas quando se é criado um novo usuário para o KeyVault conforme link: 
<a href='https://docs.microsoft.com/pt-BR/python/api/overview/azure/keyvault-keys-readme?view=azure-python#create-a-service-principal-optional'>Link</a>

<br>

<h3>/key/get_key</h3>
<hr>
Retorna a chave criada pelo Endpoint anterior. São necessárias as variáveis de ambiente "AZURE_CLIENT_ID", "AZURE_CLIENT_SECRET", e "AZURE_TENANT_ID". Os valores dessas chaves são criadas quando se é criado um novo usuário para o KeyVault conforme link: 
<a href='https://docs.microsoft.com/pt-BR/python/api/overview/azure/keyvault-keys-readme?view=azure-python#create-a-service-principal-optional'>Link</a>

<br>

<h3>/test/create_container</h3>
<hr>
Cria um container no Azure Blob Storage. Necessária a variável de ambiente "AZURE_STORAGE_CONNECTION_STRING".

<br>

<h3>/test/list_files</h3>
<hr>
Lista os arquivos que estão armazenados no container criado no endpoint anterior. Necessária a variável de ambiente "AZURE_STORAGE_CONNECTION_STRING".

<br>

<h3>/test/send_mail_flask</h3>
<hr>
Envia um email usando a biblioteca flask-mail. É necessária a variável de ambiente "MAIL_USERNAME". A senha do email é requisitada de uma secret com nome 'mail-password' que foi previamente criada no KeyVault. O SMTP server usado é do <a href='https://mailtrap.io/'>MailTrap</a>, uma ferramente para testar o envio de emails. Não é recomendado usar provedores de email grátis (gmail, outlook, yahoo...), podem não funcionar. 

<br>

<h3>/test/graph</h3>
<hr>
Envia a imagem "fig1.png" armazenada no container criado anteriormente. Será utilizada a biblioteca flask-mail para o envio do email. 

<img src='Diagrama em branco - Página 1.png'>

<br>

<h3>/test/send_mail</h3>
<hr>
Envia o email usando a api <a href='https://docs.sendgrid.com/'>SendGrid</a>. Necessária a variável de ambiente "SENDGRID_API_KEY" para funcionar. 

<br>
