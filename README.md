<h1 align="center"> Script de visualização de vagas do ciee </h1>

<h2>Descrição</h2>

Este algoritmo entra no site do ciee (https://web.ciee.org.br/estudante) e mostra as vagas de Estágio disponíveis, uma vaga por aba do navegador.

<h2>Observações</h2> 

- O algoritmo é muito dependente da estrutura atual do site. Ele funciona perfeitamente na data de publicação do algoritmo, mas pode se tornar obsoleto dependendo das mudanças do site.
- O algoritmo só funciona com o Firefox.
- O script dificilmente funciona em segundo plano.

<h2>Como usar</h2>

Set up no Windows:

- Clone o repositório:

`git clone git@github.com:pedroyen21/visualizacao-vagas-ciee-selenium.git`

- Eu recomendo que instale as dependências em um ambiente virtual para isolar o projeto; nesse caso vou usar a biblioteca 'virtualenv' para tal.
   - Se não tiver o virtualenv instalado: 
      `pip install virtualenv`
  
   - Se já tiver, inicie o ambiente virtual:
       `python -m virtualenv <nome do ambiente virtual>`
   
   - Ative o ambiente virtual: 
       `<nome do ambiente virtual>\Scripts\activate`

- Instale as dependências do projeto no ambiente virtual: 
  `pip install requirements.txt`

- Troque os nomes dos valores da constante `INFO` do arquivo app.py para o seu usuário e sua senha.

- Rode o arquivo "execute_app.exe"
