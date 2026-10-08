import csv
import re
from datetime import datetime


# ==========================================================
# EXCEÇÃO PERSONALIZADA
# ==========================================================

class FormatoInvalidoError(Exception):
    """Exceção para dados que não atendem às regras de formato."""
    pass


# ==========================================================
# REGEX
# ==========================================================

PADRAO_EMAIL = r"^[\w\.-]+@[\w\.-]+\.\w+$"

PADRAO_CPF = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"

PADRAO_TELEFONE = r"^\(\d{2}\)\s\d{4,5}-\d{4}$"

PADRAO_DATA = r"^\d{2}/\d{2}/\d{4}$"


# ==========================================================
# FUNÇÕES DE VALIDAÇÃO
# ==========================================================

def validar_email(email):
    """Valida o formato de um e-mail."""
    return re.fullmatch(PADRAO_EMAIL, email) is not None


def validar_cpf(cpf):
    """Valida o formato de um CPF."""
    return re.fullmatch(PADRAO_CPF, cpf) is not None


def validar_telefone(telefone):
    """Valida o formato de um telefone."""
    return re.fullmatch(PADRAO_TELEFONE, telefone) is not None


def validar_data(data):
    """
    Valida o formato e verifica se a data realmente existe.
    """
    if not re.fullmatch(PADRAO_DATA, data):
        return False

    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True

    except ValueError:
        return False


# ==========================================================
# VALIDAÇÃO COMPLETA DO REGISTRO
# ==========================================================

def validar_registro(registro):
    """
    Verifica todos os campos obrigatórios do registro.
    """

    erros = []

    email = registro["email"].strip()
    cpf = registro["cpf"].strip()
    telefone = registro["telefone"].strip()
    data = registro["data"].strip()

    if not validar_email(email):
        erros.append("E-mail inválido")

    if not validar_cpf(cpf):
        erros.append("CPF inválido")

    if not validar_telefone(telefone):
        erros.append("Telefone inválido")

    if not validar_data(data):
        erros.append("Data inválida")

    if erros:
        raise FormatoInvalidoError("; ".join(erros))


# ==========================================================
# LEITURA DO ARQUIVO CSV
# ==========================================================

def ler_dados(nome_arquivo):
    """
    Lê o arquivo CSV e retorna uma lista de registros.
    """

    registros = []

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:

        leitor = csv.DictReader(arquivo)

        # Verifica se as colunas necessárias existem.
        colunas_obrigatorias = {
            "email",
            "cpf",
            "telefone",
            "data"
        }

        if leitor.fieldnames is None:
            raise KeyError("O arquivo CSV não possui cabeçalho.")

        colunas_existentes = set(leitor.fieldnames)

        colunas_faltantes = (
            colunas_obrigatorias - colunas_existentes
        )

        if colunas_faltantes:
            raise KeyError(
                f"Colunas ausentes: {', '.join(colunas_faltantes)}"
            )

        for linha in leitor:
            registros.append(linha)

    return registros


# ==========================================================
# ANÁLISE DOS DADOS
# ==========================================================

def analisar_dados(registros):

    validos = []
    invalidos = []

    for numero, registro in enumerate(registros, start=1):

        try:
            validar_registro(registro)

        except FormatoInvalidoError as erro:

            invalidos.append({
                "linha": numero,
                "registro": registro,
                "erro": str(erro)
            })

        else:

            validos.append({
                "linha": numero,
                "registro": registro
            })

        finally:

            print(
                f"Registro {numero} analisado."
            )

    return validos, invalidos


# ==========================================================
# GERAÇÃO DO RELATÓRIO
# ==========================================================

def gerar_relatorio(validos, invalidos, total):

    quantidade_validos = len(validos)
    quantidade_invalidos = len(invalidos)

    if total > 0:
        percentual_validos = (
            quantidade_validos / total
        ) * 100
    else:
        percentual_validos = 0

    relatorio = []

    relatorio.append("=" * 60)
    relatorio.append("RELATÓRIO DE ANÁLISE DE DADOS")
    relatorio.append("=" * 60)

    relatorio.append("")
    relatorio.append("ESTATÍSTICAS")
    relatorio.append("-" * 60)

    relatorio.append(
        f"Total de registros: {total}"
    )

    relatorio.append(
        f"Registros válidos: {quantidade_validos}"
    )

    relatorio.append(
        f"Registros inválidos: {quantidade_invalidos}"
    )

    relatorio.append(
        f"Percentual de válidos: {percentual_validos:.2f}%"
    )

    # ------------------------------------------------------
    # DADOS VÁLIDOS
    # ------------------------------------------------------

    relatorio.append("")
    relatorio.append("DADOS VÁLIDOS")
    relatorio.append("-" * 60)

    if validos:

        for item in validos:

            registro = item["registro"]

            relatorio.append(
                f"Linha {item['linha']}: "
                f"E-mail: {registro['email']} | "
                f"CPF: {registro['cpf']} | "
                f"Telefone: {registro['telefone']} | "
                f"Data: {registro['data']}"
            )

    else:

        relatorio.append(
            "Nenhum registro válido encontrado."
        )

    # ------------------------------------------------------
    # DADOS INVÁLIDOS
    # ------------------------------------------------------

    relatorio.append("")
    relatorio.append("DADOS INVÁLIDOS")
    relatorio.append("-" * 60)

    if invalidos:

        for item in invalidos:

            registro = item["registro"]

            relatorio.append(
                f"Linha {item['linha']}: "
                f"E-mail: {registro['email']} | "
                f"CPF: {registro['cpf']} | "
                f"Telefone: {registro['telefone']} | "
                f"Data: {registro['data']}"
            )

            relatorio.append(
                f"Motivo: {item['erro']}"
            )

    else:

        relatorio.append(
            "Nenhum registro inválido encontrado."
        )

    relatorio.append("")
    relatorio.append("=" * 60)
    relatorio.append("FIM DO RELATÓRIO")
    relatorio.append("=" * 60)

    return "\n".join(relatorio)


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

def main():

    nome_arquivo = "dados.csv"

    arquivo_aberto = False

    try:

        print("=" * 60)
        print("SISTEMA DE ANÁLISE DE DADOS")
        print("=" * 60)

        print(
            f"\nLendo arquivo: {nome_arquivo}"
        )

        registros = ler_dados(nome_arquivo)

        arquivo_aberto = True

        print(
            f"Arquivo carregado com {len(registros)} registros."
        )

        validos, invalidos = analisar_dados(registros)

        relatorio = gerar_relatorio(
            validos,
            invalidos,
            len(registros)
        )

        print("")
        print(relatorio)

        # Salva o relatório em um arquivo.
        with open(
            "relatorio.txt",
            "w",
            encoding="utf-8"
        ) as arquivo_relatorio:

            arquivo_relatorio.write(relatorio)

        print(
            "\nRelatório salvo em: relatorio.txt"
        )

    except FileNotFoundError:

        print(
            f"\nERRO: O arquivo '{nome_arquivo}' não foi encontrado."
        )

    except KeyError as erro:

        print(
            f"\nERRO DE COLUNA: {erro}"
        )

    except ValueError as erro:

        print(
            f"\nERRO DE VALOR: {erro}"
        )

    except Exception as erro:

        print(
            f"\nERRO INESPERADO: {erro}"
        )

    else:

        print(
            "\nAnálise concluída com sucesso."
        )

    finally:

        if arquivo_aberto:
            print(
                "Finalização: arquivo processado corretamente."
            )
        else:
            print(
                "Finalização: o processamento não foi concluído."
            )


# ==========================================================
# EXECUÇÃO
# ==========================================================

if __name__ == "__main__":
    main()