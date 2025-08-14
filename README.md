# desafio-b2bflow-2025
Requisitos:
    Conta no Supabase com tabela contatos.
    Conta no Z-API (plano gratuito disponível).
    Python 3.8+ instalado.

Estrutura da tabela no Supabase
    Nome da tabela: contatos

    Coluna	Tipo	Exemplo
    id	    int	    1
    nome	text	Maria
    numero	text	5511999999999

Configuração
    Clone este repositório:
        git clone https://github.com/Nick2901/desafio-b2bflow-2025.git
        cd src


    Instale as dependências:
        pip install supabase python-dotenv requests
        
    Crie um arquivo .env baseado nos dados a seguir:
        SUPABASE_URL=https://xxxx.supabase.co
        SUPABASE_KEY=sua_chave_do_supabase
        ZAPI_INSTANCE_ID=id_da_sua_instancia
        ZAPI_TOKEN=token_da_instancia
        ZAPI_TOKEN_CLIENT=client_token_do_zapi

Como rodar
    Digite "python main.py"


O código ignora mais de 3 contatos para evitar spam.

Certifique-se que os números estejam no formato DDI+DDD+número, sem traços ou espaços (ex.: 5511999999999).

Lembre-se de conectar a sua instancia do Z-Api para que tudo funcione corretamente.
