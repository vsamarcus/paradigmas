# Number to Words Converter

Este projeto oferece duas implementações diferentes de um conversor de números para palavras, suportando múltiplos idiomas através da biblioteca `num2words`.

## Instalação

1. Crie um ambiente virtual Python:
```bash
python -m venv .venv
```

2. Ative o ambiente virtual:
```bash
# Linux/MacOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install num2words
```

## Implementações

### 1. Versão Imperativa (`imperative.py`)

Implementação usando programação imperativa tradicional, com uma função principal que realiza a conversão.

#### Características:
- Abordagem direta e procedural
- Função única com responsabilidade específica
- Mais simples de entender para iniciantes
- Boa para scripts pequenos e diretos

#### Execução:
```bash
# Exemplo em português (padrão)
python imperative.py --number 1234.56

# Exemplo em inglês
python imperative.py --number 1234.56 --language en
```

### 2. Versão Orientada a Objetos (`oo.py`)

Implementação usando paradigma de orientação a objetos, encapsulando a lógica em uma classe.

#### Características:
- Encapsulamento de dados e comportamento
- Melhor organização do código
- Mais fácil de estender e manter
- Ideal para sistemas mais complexos

#### Execução:
```bash
# Exemplo em português (padrão)
python oo.py --number 1234.56

# Exemplo em inglês
python oo.py --number 1234.56 --language en
```

## Comparação das Implementações

### Versão Imperativa
#### Vantagens:
- Código mais direto e simples
- Menor curva de aprendizado
- Bom para scripts pequenos
- Fácil de entender o fluxo de execução

#### Desvantagens:
- Menos flexível para extensões
- Pode ficar confuso em sistemas maiores
- Difícil de reutilizar código
- Menos organizado em projetos grandes

### Versão Orientada a Objetos
#### Vantagens:
- Melhor organização do código
- Mais fácil de manter e estender
- Melhor encapsulamento
- Ideal para sistemas complexos

#### Desvantagens:
- Mais código inicial (boilerplate)
- Curva de aprendizado maior
- Pode ser excessivo para scripts simples
- Requer mais planejamento inicial

## Parâmetros

Ambas implementações aceitam os mesmos parâmetros:

- `--number`: Número a ser convertido (obrigatório)
  - Exemplo: 1234.56

- `--language`: Código do idioma (opcional)
  - Padrão: 'pt_BR'
  - Opções comuns: 'pt_BR', 'en'
  - Aceita qualquer código de idioma suportado pela biblioteca num2words

## Exemplos de Uso

```bash
# Versão Imperativa
python imperative.py --number 1234.56
python imperative.py --number 42 --language en

# Versão Orientada a Objetos
python oo.py --number 1234.56
python oo.py --number 42 --language en
```

## Tratamento de Erros

Ambas as implementações incluem:
- Validação de tipos de dados
- Tratamento de erros de conversão
- Mensagens de erro claras
- Códigos de retorno apropriados (0 para sucesso, 1 para erro)

## Dicionário de Código

### Versão Imperativa (`imperative.py`)

#### Funções
- `convert_number(number: Union[int, float, Decimal], language: str) -> str`: 
  - Converte um número para sua representação por extenso
  - Parâmetros: número e idioma
  - Retorna: string com o número por extenso

- `validate_number(number: Union[int, float, Decimal]) -> None`:
  - Valida se o input é um valor numérico
  - Parâmetros: número a ser validado
  - Retorna: None ou levanta TypeError

- `create_parser() -> argparse.ArgumentParser`:
  - Cria e configura o parser de argumentos CLI
  - Retorna: objeto ArgumentParser configurado

- `main() -> int`:
  - Ponto de entrada do programa
  - Processa argumentos CLI e executa a conversão
  - Retorna: 0 para sucesso, 1 para erro

#### Variáveis
- `parser`: Instância de ArgumentParser para processar argumentos CLI
- `args`: Argumentos processados da linha de comando
- `result`: Resultado da conversão do número para texto

### Versão Orientada a Objetos (`oo.py`)

#### Classe
- `NumberToWords`: Classe principal para conversão de números

#### Atributos
- `number`: Número a ser convertido
- `language`: Código do idioma para conversão

#### Métodos
- `__init__(self, number: Union[int, float, Decimal], language: str = 'pt_BR')`:
  - Construtor da classe
  - Inicializa número e idioma
  - Valida o número recebido

- `_validate_number(self, number: Union[int, float, Decimal]) -> None`:
  - Método privado para validação do número
  - Verifica se é um tipo numérico válido

- `convert(self) -> str`:
  - Método público principal
  - Realiza a conversão do número para texto
  - Retorna o resultado por extenso

#### Funções Auxiliares
- `create_parser() -> argparse.ArgumentParser`:
  - Cria e configura o parser de argumentos CLI
  - Retorna: objeto ArgumentParser configurado

- `main() -> int`:
  - Ponto de entrada do programa
  - Processa argumentos e executa a conversão
  - Retorna: 0 para sucesso, 1 para erro

#### Variáveis
- `parser`: Instância de ArgumentParser para processar argumentos CLI
- `args`: Argumentos processados da linha de comando
- `converter`: Instância da classe NumberToWords
- `result`: Resultado da conversão do número para texto

## Tipos de Dados Utilizados

### Tipos Básicos
- `int`: Números inteiros
- `float`: Números decimais
- `str`: Textos e strings
- `bool`: Valores booleanos

### Tipos Compostos
- `Union[int, float, Decimal]`: União de tipos numéricos aceitos
- `argparse.ArgumentParser`: Tipo para processamento de argumentos CLI
- `Exception`: Tipos de exceções para tratamento de erros
