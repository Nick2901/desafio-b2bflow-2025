# desafio-b2bflow-2025
Desafio B2BFlow 2025
Requisitos

Conta no Supabase com tabela contatos.

Conta no Z-API (plano gratuito disponível).

Python 3.8+ instalado.

Estrutura da tabela no Supabase

Nome da tabela: contatos

Coluna	Tipo	Exemplo
id	int	1
nome	text	Maria
numero	text	5511999999999
Configuração

Clone este repositório:

git clone https://github.com/Nick2901/desafio-b2bflow-2025.git
cd src


Instale as dependências:

pip install supabase python-dotenv requests


Crie um arquivo .env com os seguintes dados:

SUPABASE_URL=https://xxxx.supabase.co
SUPABASE_KEY=sua_chave_do_supabase
ZAPI_INSTANCE_ID=id_da_sua_instancia
ZAPI_TOKEN=token_da_instancia
ZAPI_TOKEN_CLIENT=client_token_do_zapi

Como rodar
python main.py

Observações

O código envia mensagens para até 3 contatos, ignorando contatos extras para evitar spam.

Certifique-se que os números estejam no formato DDI+DDD+número, sem traços ou espaços (ex.: 5511999999999).

Conecte sua instância do Z-API para que as mensagens sejam realmente enviadas. Se o código rodar com a instância desconectada, as mensagens ficarão apenas na fila.
