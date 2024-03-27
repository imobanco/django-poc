### Preparando o ambiente
Após clonar este repositório, execute os comandos abaixo:

### Compilar estress test
Baixe este repositório e compile ele por meio de um `make` https://github.com/wg/wrk

```bash
# Cria virtual env na pasta corrente
python3 -m venv .venv
# Ativa ambiente python
source .venv/bin/activate
# Instala dependências
pip install -r requirements.txt
```

### Testando modelo sync
Iniciar primeiro terminal e executar `make run.gunicorn`

Apos o serviço esta pronto, abra um novo terminal na raiz onde o wrk foi compilado e execute: `./wrk -t 8 -c 500 -d 10 --latency http://localhost:8000/sync_sleep/\?sleep\=0.1`

### Testando modelo async
Iniciar primeiro terminal e executar `make run.uvicorn`

Apos o serviço esta pronto, abra um novo terminal na raiz onde o wrk foi compilado e execute: `./wrk -t 8 -c 500 -d 10 --latency http://localhost:8000/sync_sleep/\?sleep\=0.1`

Ambos os servidores irão utilizar apenas um processo ou uma thread, a ideia é testar o cenário de exaustão sem esforço,
apenas precisamos entender quais situações estão críticas para o nosso cenário e onde precisaremos de correções para adotar
o modelo async.

### Testes com sujeira
Inicie o serviço com `make run.uvicorn`

Abra um navegador para o endpoint http://localhost:8000/dirty/?sleep=0.3&email=dev

Abra outro navegador para o endpoint http://localhost:8000/dirty/?sleep=7&email=test

Realize algumas atualizações de página no primeiro navegador que tem o tempo mais curto.

Ambas as páginas retornarão um conteúdo simples, porém o email do primeiro navegador estranhamente veio parar no segundo, o que era esperado de se acontecer.

Embora esse seja um cenário que não esperamos ter no nosso contexto, é extremamente crucial realizar uma validação criteriosa.

### Considerações finais
- Quanto mais baixo o sleep time, menos sentido faz termos o uvicorn com handles async, o contrário também é verdadeiro.
- Um bom teste de experiência de usuário final é abrir dois navegadores e realizar no modelo sync e async os testes nos mesmos endpoints.
- Se formos adotar uma abordagem de reescrita dos handles http + metódos que já usamos hoje, precisamos entender e investigar bem todos os lugares para que não caiamos em comportamento inesperado.
- Varrer e revisar corretamente os testes de sujeira de memória, ou seja em que ponto um dado valor que estava dentro de um objeto foi parar na execução de outra tarefa async, ver seção testes com sujeira.
