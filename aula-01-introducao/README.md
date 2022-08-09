# Aula 01 - Introdução à Orientação a Objetos e Estruturas de Dados

## Estrutura de Dados

### Tipos primitivos
| Tipo     | Exemplo              |
|----------|----------------------|
| int      | x = 10               |
| float    | x = 10.5             |
| string   | y = "gato"           |
| boolean  | y = true             |
| date     | z = date(2022,4,18)  |
| time     | z = time(21,30,00)   |
| datetime | z = datetime.now()   |
| timedelta| z = timedelta(days=1)|

### Operadores
| Operadores           | Categoria               |
|----------------------|-------------------------|
| **                   | potenciação             |  
| *                    | multiplicação           |
| /                    | divisão                 |
| //                   | divisão                 |
| %                    | módulo                  |
| +                    | soma                    |
| -                    | subtração               |
| ==, !=, <=, >=, >, < | relacional              |
| not, and, or         | lógico                  |


## Orientação a Objetos

Orientação a Objetos é um paradigma dentro da programação, onde sua ideia principal é modelar os dados de acordo com o agrupamento de dados semelhantes. Este paradigma também pode ser associado a como o reino animal é dividido, onde os grupos são dividos de acordo com as características semelhantes.

A partir disso temos algums conceitos base para conseguir aplicar POO, como:

### Classe
Estrutura inicial, onde definimos que características e comportamentos o nosso objeto vai ter, sendo que:
  - **atributos**: são as variáveis dentro da classe que define as características do objeto;
  - **métodos**: são as funções dentro da classe que define os comportamentos do objeto.

### Objeto
O objeto é a utilização da classe. Onde a gente pega a estrutura criada na classe e cria uma variavel com base na classe. 

Isso acontece no momento que instanciamos a classe.