# Vet Life – Clínica Veterinária

## Sobre o projeto

O Vet Life é um sistema de gerenciamento de uma clínica veterinária desenvolvido em Python para a disciplina de Estrutura de Dados.

O objetivo é gerenciar o ciclo de atendimento de um animal, desde sua chegada à clínica até o fechamento do prontuário e pagamento, utilizando estruturas de dados implementadas manualmente.

## Funcionalidades

- Cadastro, busca e remoção de tutores e animais.
- Fila de atendimento normal e emergencial.
- Controle de ocupação dos consultórios.
- Diagnóstico utilizando uma árvore de sistemas do animal.
- Controle de estoque de medicamentos, vacinas e materiais.
- Controle de lotes, validade e registro de perdas.
- Ajuste de estoque e alertas de quantidade mínima.
- Gerenciamento de prontuários, medicamentos e procedimentos.
- Alta, fechamento do prontuário e pagamento.
- Relatórios de consumo, pagamentos e perdas.
- Simulação de um atendimento completo.

## Estruturas de dados utilizadas

As estruturas foram implementadas em classes próprias, separando as estruturas de dados das regras de funcionamento da clínica.

- **Lista encadeada:** utilizada no armazenamento de tutores, animais, produtos, prontuários e registros.
- **Fila:** utilizada no controle de atendimento e dos lotes de medicamentos.
- **Árvore N-ária:** utilizada para representar os sistemas, órgãos e estruturas do animal durante o diagnóstico.

## Combinações de estruturas de dados

### 1. Lista + Lista — Tutores e animais

**Classes envolvidas:** `Lista`, `CadastroTutores` e `Tutor`.

**Métodos envolvidos:** `cadastrar_tutor()`, `buscar_tutor()`, `cadastrar_animal()`, `buscar_animal()` e `remover_animal()`.

O cadastro possui uma lista de tutores, e cada tutor possui sua própria lista de animais. Para buscar um animal, primeiro é localizado o tutor pelo CPF e, depois, o animal pelo nome.

Essa combinação permite que cada tutor tenha uma quantidade dinâmica de animais, mantendo seus dados organizados.

Utilizar uma única lista exigiria misturar os registros dos tutores e animais ou repetir informações dos tutores, dificultando o gerenciamento.

### 2. Fila + Fila — Atendimento prioritário

**Classes envolvidas:** `Fila` e `Atendimento`.

**Métodos envolvidos:** `registrar_chegada()`, `proximo()` e `chamar_proximo()`.

O atendimento utiliza duas filas: uma para casos normais e outra para emergências.

O sistema verifica primeiro a fila de emergência. Caso esteja vazia, o próximo animal é retirado da fila normal. Ambas respeitam a ordem de chegada dentro de sua categoria.

Uma única fila comum não permitiria priorizar emergências sem realizar buscas ou reorganizar seus elementos.

### 3. Lista + Fila — Estoque de medicamentos

**Classes envolvidas:** `Lista`, `Fila`, `Estoque`, `Produto` e `Lote`.

**Métodos envolvidos:** `cadastrar_produto()`, `buscar_produto()`, `comprar_lote()`, `baixar()` e `descartar_vencidos()`.

O estoque utiliza uma lista de produtos, em que cada produto possui uma fila de lotes.

A lista permite localizar os produtos pelo código, enquanto a fila organiza a saída dos lotes pelo princípio FIFO (First In, First Out). Para consumir primeiro os lotes mais antigos, eles devem estar organizados em ordem cronológica de compra.

Essa combinação facilita o controle individual de quantidade, fornecedor, preço de compra e validade de cada lote.

Utilizar uma única estrutura dificultaria a separação dos lotes de cada produto e o controle da ordem de consumo.

## Árvore de diagnóstico

A árvore de diagnóstico utiliza as classes `Arvore` e `NoArvore`.

Cada nó pode possuir vários filhos, representando a hierarquia dos sistemas, órgãos e estruturas do animal.

A exibição utiliza o percurso em profundidade em pré-ordem, apresentando primeiro o nó atual e depois seus filhos.

Durante o diagnóstico, é possível marcar estruturas identificadas por código como alteradas.

## Organização do projeto

- `main.py` — Menu principal e simulação de atendimento.
- `clinica/` — Classes e regras de funcionamento da clínica.
- `estruturas/` — Implementação das estruturas de dados e seus testes.

## Como executar

É necessário possuir o Python 3 instalado.

Abra o terminal na pasta principal do projeto e execute:

`python main.py`

## Menu principal

1. Tutores e animais
2. Atendimento
3. Prontuário
4. Estoque
5. Relatórios
6. Simular um atendimento completo
0. Sair

O sistema permite realizar as operações manualmente pelo menu ou utilizar a opção de simulação automática.

## Tecnologias utilizadas

- Python 3
- Git
- GitHub

## Finalidade acadêmica

Projeto desenvolvido para a disciplina de Estrutura de Dados, com o objetivo de aplicar os conceitos de listas encadeadas, filas, árvores e combinações de estruturas de dados em um sistema de gerenciamento de clínica veterinária.
