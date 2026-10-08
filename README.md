# Sistema de Análise de Dados em Python

## Descrição

Este projeto foi desenvolvido como atividade prática de Python, com o objetivo de aplicar conceitos de manipulação de arquivos, expressões regulares (Regex), tratamento de exceções e geração de relatórios.

O programa lê um arquivo CSV contendo informações de e-mail, CPF, telefone e data. Cada registro é analisado e classificado como válido ou inválido de acordo com os padrões definidos.

---

## Estrutura do projeto



sistema-analise-dados/ │ ├── app.py ├── dados.csv ├── README.md └── relatorio.txt


O arquivo `relatorio.txt` é gerado automaticamente pelo programa após a análise.

---

## Tecnologias utilizadas

- Python 3
- Módulo `csv`
- Módulo `re`
- Módulo `datetime`

---

# Validação com Regex

As expressões regulares foram utilizadas para verificar se os dados possuem o formato esperado.

## E-mail

Foi utilizado o seguinte padrão:



r"^[\w.-]+@[\w.-]+.\w+$"


Esse padrão verifica uma estrutura básica de e-mail, como:



usuario@email.com


Os principais elementos utilizados são:

- `^` indica o início da string.
- `$` indica o final da string.
- `\w` representa caracteres de palavra.
- `\.` representa um ponto literal.
- `+` indica uma ou mais ocorrências.

---

## CPF

O padrão utilizado foi:



r"^\d{3}.\d{3}.\d{3}-\d{2}$"


Ele espera um CPF no formato:



123.456.789-09


O `\d` representa um dígito numérico.

---

## Telefone

O padrão utilizado foi:



r"^
\d
2
\s\d{4,5}-\d{4}$"


Ele aceita formatos como:



(11) 98765-4321


Nesse padrão:

- `\d` representa números.
- `\s` representa espaço em branco.
- `{2}` indica exatamente dois caracteres.
- `{4,5}` indica entre quatro e cinco caracteres.

---

## Data

O padrão utilizado foi:



r"^\d{2}/\d{2}/\d{4}$"


O formato esperado é:



15/03/2025


Além da Regex, o programa utiliza `datetime.strptime()` para verificar se a data realmente existe.

Por exemplo:



31/02/2025


possui o formato esperado, mas não é uma data válida.

---

# Métodos de validação

O programa possui funções específicas para cada tipo de dado:



validaremail() validarcpf() validartelefone() validardata()


Essas funções utilizam o módulo `re` para verificar os padrões definidos.

A função `validar_data()` também utiliza o módulo `datetime` para verificar se a data informada realmente existe.

---

# Tratamento de exceções

O programa utiliza `try`, `except`, `else` e `finally` para tratar possíveis erros durante a execução.

## FileNotFoundError

É utilizado quando o arquivo CSV não é encontrado.

Exemplo:



except FileNotFoundError: print("Arquivo não encontrado.")


---

## ValueError

O `ValueError` é utilizado para tratar valores inválidos, principalmente durante conversões ou validações de dados.

---

## KeyError

O `KeyError` é utilizado quando alguma coluna obrigatória não existe no arquivo CSV.

As colunas esperadas são:



email cpf telefone data


---

# Exceção personalizada

Foi criada uma exceção personalizada chamada:



class FormatoInvalidoError(Exception): pass


Essa exceção é utilizada quando um registro não atende às regras de validação.

Por exemplo, quando o e-mail, CPF, telefone ou data estão em formato inválido.

A criação de uma exceção personalizada permite tratar especificamente erros relacionados às regras de negócio do sistema.

---

# Uso de try, except, else e finally

O programa utiliza a seguinte estrutura:



try:

processamento

except:

tratamento do erro

else:

executado quando não ocorre erro

finally:

executado sempre

O bloco `finally` é importante porque sempre será executado, independentemente de ocorrer uma exceção ou não.

---

# Arquivo de entrada

O arquivo `dados.csv` contém informações como:



email,cpf,telefone,data joao@email.com,123.456.789-09,(11) 98765-4321,15/03/2025 maria@email.com,987.654.321-00,(21) 91234-5678,20/04/2025


Também existem registros propositalmente inválidos para testar o funcionamento das validações.

---

# Relatório

Após analisar os registros, o programa gera um relatório contendo:

- Total de registros.
- Quantidade de registros válidos.
- Quantidade de registros inválidos.
- Percentual de registros válidos.
- Dados dos registros válidos.
- Dados dos registros inválidos.
- Motivo da invalidação.

O relatório utiliza `f-strings` para formatar as informações.

Exemplo:



f"Total de registros: {total}"


O resultado é salvo no arquivo:



relatorio.txt


---

# Como executar

Primeiro, certifique-se de que o Python está instalado.

Abra o terminal na pasta do projeto e execute:



python app.py


Em alguns sistemas, pode ser necessário utilizar:



python3 app.py


---

# Exemplo de saída



============================================================ RELATÓRIO DE ANÁLISE DE DADOS ============================================================

ESTATÍSTICAS

Total de registros: 6 Registros válidos: 3 Registros inválidos: 3 Percentual de válidos: 50.00%

DADOS VÁLIDOS

...

DADOS INVÁLIDOS

...

============================================================ FIM DO RELATÓRIO ============================================================


---

# Conclusão

O projeto demonstra a aplicação prática de conceitos importantes da linguagem Python.

Foram utilizados:

1. Manipulação de arquivos com `with open()`.
2. Expressões regulares com o módulo `re`.
3. Tratamento de exceções com `try`, `except`, `else` e `finally`.
4. Exceção personalizada herdando de `Exception`.
5. Formatação de informações utilizando `f-strings`.
6. Geração de um relatório com os resultados da análise.

Dessa forma, o sistema consegue ler dados, validar as informações, identificar erros e gerar um relatório organizado com os resultados.
