Vet Life

Sistema de gerenciamento de uma clínica veterinária desenvolvido em Python para a disciplina de Estrutura de Dados. O sistema gerencia todo o ciclo de atendimento, desde o cadastro do animal até o fechamento do prontuário e pagamento.

*LINK DA APRESENTAÇÃO*: https://youtu.be/TrMUGA2TB3E

Funcionalidades

- Cadastro, busca e remoção de tutores e animais.
- Atendimento por ordem de chegada, com prioridade para emergências.
- Controle de consultórios.
- Diagnóstico por meio de uma árvore de sistemas do animal.
- Controle de estoque, lotes, validade e perdas.
- Ajuste de inventário e alertas de estoque mínimo.
- Gerenciamento de prontuários, medicamentos e procedimentos.
- Alta, pagamento e relatórios de consumo.

Estruturas de dados

O projeto utiliza implementações próprias de listas encadeadas, filas e árvores N-árias, separadas das regras de funcionamento da clínica.

Lista + Lista — Tutores e animais

Classes: "Lista", "CadastroTutores", "Tutor" e "Animal".

Métodos: "cadastrar_tutor()", "buscar_tutor()", "cadastrar_animal()" e "buscar_animal()".

Cada tutor possui sua própria lista de animais, permitindo cadastrar novos animais sem limite pré-definido. A busca ocorre primeiro pelo CPF do tutor e depois pelo nome do animal.

Uma única lista poderia exigir a repetição dos dados dos tutores, dificultando a organização dos registros.

Fila + Fila — Atendimento prioritário

Classes: "Fila" e "Atendimento".

Métodos: "registrar_chegada()", "proximo()" e "chamar_proximo()".

Duas filas independentes organizam os atendimentos normais e emergenciais. A fila de emergência possui prioridade, mantendo a ordem de chegada dentro de cada categoria.

Uma única fila convencional exigiria percorrer ou reorganizar seus elementos para priorizar emergências.

Lista + Fila — Estoque

Classes: "Lista", "Fila", "Estoque", "Produto" e "Lote".

Métodos: "buscar_produto()", "comprar_lote()" e "baixar()".

Cada produto armazenado na lista possui uma fila de lotes organizada pela data de compra, garantindo que os lotes mais antigos sejam consumidos primeiro.

Uma única estrutura dificultaria a organização dos lotes por produto e o controle da ordem de consumo.

Árvore N-ária — Diagnóstico

A árvore representa a hierarquia dos sistemas, órgãos e estruturas do animal. Cada nó pode possuir vários filhos.

A exibição utiliza o percurso em profundidade em pré-ordem. Os nós podem ser localizados pelo nome ou código e marcados como alterados.

Complexidade das operações

Operação| Complexidade
Inserção, busca e remoção na lista| O(n)
Inserção e remoção na fila| O(1)
Consulta ao próximo animal| O(1)
Busca de um nó na árvore| O(n)
Visitação dos nós em pré-ordem| O(n)
Busca de um animal| O(t + a)
Inserção ordenada de um lote| O(p + l)

Considerando o pior caso, "n" representa a quantidade de elementos ou nós, "t" os tutores, "a" os animais do tutor, "p" os produtos e "l" os lotes do produto.

Organização do projeto

- "main.py" — Menu interativo e simulação de atendimento.
- "clinica/" — Regras de funcionamento da clínica.
- "estruturas/" — Implementação das estruturas de dados.

Como executar

Com o Python 3 instalado, execute o seguinte comando na pasta principal do projeto:

python main.py

O sistema permite realizar um atendimento completo manualmente pelo menu ou utilizar a opção de simulação automática.
