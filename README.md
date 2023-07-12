
# API Vestido - 2023 😲

Produzido Pelos Alunos do 3IRC - 2023 :)
```
"Tudo que ta ruim pode piorar"
 Vieira,Alfredo 2017
```

## Autores

- [@Vineees](https://www.github.com/Vineees) - Implementação
- [@PsyShadowF](https://github.com/PsyShadowF) - Backend Dev/Front


## Introdução

Projeto iniciado no ano de 2023 onde o objetivo foi a criação de uma API onde o vestido e os fogos seriam controlados via uma interface web. 
- #### AMBIENTE DE PRODUÇÃO EM LINUX! TESTES NÃO FORAM FEITOS EM WINDOWS

## Requisitos/Ambiente  

- Para esse projeto fui utilizado o esp8266 para o controle dos fogos e do vestido, já para o carregamento da API utilizamos um RASPBERRY.
- Esquema de Rede pode Ser encontrado: [AQUI](https://github.com/Os-Bocaberta/Gerenciamento-Redes)
- Poder de Vontade <3

## Dependências  
- Django==4.2.2
- SqLite
- Git
- python3
- VirtualEnv
- Django-rest-framework

## Deployment
### 1. Preparando Ambiente
1. Clonando Repositório:
```
git clone https://github.com/Os-Bocaberta/API-vestido.git
```
2. Criando Virtual Environment:

```
python3 -m venv env
```
Para Entrar no venv:
```
source env/bin/activate
```

3. Instalando dependências:
```
pip install -r requirements.txt
```

4. Iniciando Servidor:

```
python3 manage.py runserver
```

## Solução de Problemas
#### Qualquer Tipo de Problema:
- [@Vineees](https://www.github.com/Vineees) :)
- Dependendo do ambiente onde você estiver trabalhando será preciso a criação de um proxy reverso, pode ser tanto Apache2 ou Nginx, porém nosso ambiente foi utilizado o nginx. Verifique os templates para ter uma ideia de como configurar 
## Outros Link's
#### Reverse Proxy Templates [AQUI](https://github.com/Vineees/Django-ReverseProxy)
