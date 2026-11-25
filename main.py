from datetime import date
from clinica.clinica import Clinica


def ler_numero(texto):
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print("Digite um número inteiro.")


def ler_valor(texto):
    while True:
        try:
            return float(input(texto).replace(",", "."))
        except ValueError:
            print("Digite um valor válido.")


def ler_data(texto):
    while True:
        try:
            return date.fromisoformat(input(texto + " (AAAA-MM-DD): "))
        except ValueError:
            print("Data inválida.")


def mostrar_tutor(tutor):
    print("Tutor:", tutor.nome, "| CPF:", tutor.cpf, "| Telefone:", tutor.telefone)
    if len(tutor.animais) == 0:
        print("  (sem animais cadastrados)")
    for animal in tutor.animais:
        print("  Animal:", animal.nome, "|", animal.especie, "|", animal.raca, "|", animal.idade, "anos")


def mostrar_prontuario(p):
    situacao = "com alta" if p.alta else "em atendimento"
    print("Prontuário", p.numero, "-", p.nome_animal, "(tutor:", p.nome_tutor + ")",
          "| vet:", p.veterinario, "| consultório", p.consultorio, "|", situacao)
    print("  Aberto em:", p.abertura.strftime("%d/%m/%Y %H:%M"))
    for med in p.medicamentos:
        print("  Medicamento:", med.nome, "x", med.quantidade, "= R$", med.quantidade * med.preco_unitario)
    for proc in p.procedimentos:
        print("  Procedimento:", proc.nome, "= R$", proc.valor)


def mostrar_estoque(c):
    if len(c.estoque.produtos) == 0:
        print("Nenhum produto cadastrado.")
    for produto in c.estoque.produtos:
        print(produto.codigo, "-", produto.nome, "| venda R$", produto.preco_venda,
              "| mínimo", produto.minimo, "| total", produto.total())
        for lote in produto.lotes:
            print("   lote", lote.numero, "| fornecedor", lote.fornecedor, "| compra R$", lote.preco_compra,
                  "| comprado em", lote.data_compra, "| validade", lote.validade, "| qtd", lote.quantidade)


def mostrar_alertas(c):
    alertas = c.estoque.abaixo_do_minimo()
    if len(alertas) == 0:
        print("Nenhum produto abaixo do mínimo.")
    for produto in alertas:
        print("ALERTA:", produto.nome, "está abaixo do mínimo (total", produto.total(), "/ mínimo", produto.minimo, ")")


def mostrar_perdas(c):
    if len(c.estoque.perdas) == 0:
        print("Nenhuma perda registrada.")
    for perda in c.estoque.perdas:
        print("Perda:", perda.nome_produto, "| lote", perda.numero_lote, "| qtd", perda.quantidade,
              "| R$", perda.valor, "| em", perda.data)


def mostrar_relatorios(c):
    print("--- Consumo de medicamentos ---")
    if len(c.consumos.lista) == 0:
        print("Nenhum consumo registrado.")
    for item in c.consumos.lista:
        print("Prontuário", item.numero_prontuario, "| tutor:", item.nome_tutor, "(CPF", item.cpf_tutor + ")",
              "| animal:", item.nome_animal, "|", item.nome_produto, "x", item.quantidade, "= R$", item.valor)
    print("--- Pagamentos ---")
    if len(c.pagamentos.lista) == 0:
        print("Nenhum pagamento registrado.")
    for pag in c.pagamentos.lista:
        parcelas = "" if pag.parcelas is None else " em " + str(pag.parcelas) + "x"
        print("Prontuário", pag.numero_prontuario, "| pagador:", pag.pagador, "|", pag.forma + parcelas,
              "| medicamentos R$", pag.valor_medicamentos, "| procedimentos R$", pag.valor_procedimentos,
              "| total R$", pag.total,
              "|", pag.data_hora.strftime("%d/%m/%Y %H:%M"))
    print("--- Perdas por validade ---")
    mostrar_perdas(c)


def menu_tutores(c):
    while True:
        print("\n--- Tutores e animais ---")
        print("1 - Cadastrar tutor")
        print("2 - Cadastrar animal")
        print("3 - Buscar tutor (CPF)")
        print("4 - Buscar animal (CPF + nome do animal)")
        print("5 - Remover tutor")
        print("6 - Remover animal")
        print("0 - Voltar")
        opcao = input("Opção: ")
        if opcao == "1":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            telefone = input("Telefone: ")
            if c.tutores.cadastrar_tutor(nome, cpf, telefone) is None:
                print("Já existe um tutor com esse CPF.")
            else:
                print("Tutor cadastrado.")
        elif opcao == "2":
            cpf = input("CPF do tutor: ")
            nome = input("Nome do animal: ")
            especie = input("Espécie: ")
            raca = input("Raça: ")
            idade = ler_numero("Idade: ")
            if c.tutores.cadastrar_animal(cpf, nome, especie, raca, idade) is None:
                print("Tutor não encontrado ou animal já cadastrado.")
            else:
                print("Animal cadastrado.")
        elif opcao == "3":
            tutor = c.tutores.buscar_tutor(input("CPF: "))
            if tutor is None:
                print("Tutor não encontrado.")
            else:
                mostrar_tutor(tutor)
        elif opcao == "4":
            cpf = input("CPF do tutor: ")
            animal = c.tutores.buscar_animal(cpf, input("Nome do animal: "))
            if animal is None:
                print("Animal não encontrado.")
            else:
                print("Animal:", animal.nome, "|", animal.especie, "|", animal.raca, "|", animal.idade, "anos")
        elif opcao == "5":
            if c.tutores.remover_tutor(input("CPF: ")) is None:
                print("Tutor não encontrado.")
            else:
                print("Tutor removido.")
        elif opcao == "6":
            cpf = input("CPF do tutor: ")
            if c.tutores.remover_animal(cpf, input("Nome do animal: ")) is None:
                print("Animal não encontrado.")
            else:
                print("Animal removido.")
        elif opcao == "0":
            return
        else:
            print("Opção inválida.")


def menu_atendimento(c):
    while True:
        print("\n--- Atendimento ---")
        print("1 - Registrar chegada do animal")
        print("2 - Ver quem é o próximo")
        print("3 - Chamar próximo (consultório livre) e abrir prontuário")
        print("4 - Ver as filas de espera")
        print("0 - Voltar")
        opcao = input("Opção: ")
        if opcao == "1":
            cpf = input("CPF do tutor: ")
            animal = input("Nome do animal: ")
            queixa = input("Queixa: ")
            emergencia = input("É emergência? (s/n): ").lower() == "s"
            if c.registrar_chegada(cpf, animal, queixa, emergencia) is None:
                print("Tutor ou animal não cadastrado.")
            elif emergencia:
                print("Animal na fila de EMERGÊNCIA.")
            else:
                print("Animal na fila normal.")
        elif opcao == "2":
            proximo = c.atendimento.proximo()
            if proximo is None:
                print("Ninguém na espera.")
            else:
                print("Próximo:", proximo.nome_animal, "(tutor:", proximo.nome_tutor + ") -", proximo.queixa)
        elif opcao == "3":
            if c.atendimento.consultorio_livre() is None:
                print("Nenhum consultório livre.")
            elif c.atendimento.total_espera() == 0:
                print("Ninguém na espera.")
            else:
                veterinario = input("Veterinário responsável: ")
                prontuario = c.chamar_proximo(veterinario)
                print("Chamado para o consultório", prontuario.consultorio, "- prontuário", prontuario.numero, "aberto.")
                mostrar_prontuario(prontuario)
        elif opcao == "4":
            print("Emergência:")
            for chegada in c.atendimento.fila_emergencia:
                print("  -", chegada.nome_animal, "|", chegada.queixa, "|", chegada.data_hora.strftime("%H:%M"))
            print("Normal:")
            for chegada in c.atendimento.fila_normal:
                print("  -", chegada.nome_animal, "|", chegada.queixa, "|", chegada.data_hora.strftime("%H:%M"))
        elif opcao == "0":
            return
        else:
            print("Opção inválida.")


def menu_prontuario(c):
    while True:
        print("\n--- Prontuário ---")
        print("1 - Ver prontuários abertos")
        print("2 - Diagnóstico (árvore de sistemas)")
        print("3 - Adicionar medicamento")
        print("4 - Remover medicamento")
        print("5 - Adicionar procedimento")
        print("6 - Remover procedimento")
        print("7 - Dar alta ao animal")
        print("8 - Fechar prontuário e registrar pagamento")
        print("0 - Voltar")
        opcao = input("Opção: ")
        hoje = date.today()
        if opcao == "1":
            if len(c.prontuarios.abertos) == 0:
                print("Nenhum prontuário aberto.")
            for p in c.prontuarios.abertos:
                mostrar_prontuario(p)
        elif opcao == "2":
            p = c.prontuarios.buscar(ler_numero("Número do prontuário: "))
            if p is None:
                print("Prontuário não encontrado.")
                continue
            p.diagnostico.exibir()
            codigo = input("Código do item alterado (Enter para sair): ")
            if codigo != "":
                if p.diagnostico.marcar_alterado(codigo):
                    print("Item marcado como Alterado.")
                else:
                    print("Código não encontrado.")
        elif opcao == "3":
            numero = ler_numero("Número do prontuário: ")
            codigo = input("Código do medicamento: ")
            quantidade = ler_numero("Quantidade: ")
            if c.adicionar_medicamento(numero, codigo, quantidade, hoje):
                print("Medicamento adicionado.")
            else:
                print("Não foi possível (prontuário/produto inexistente ou estoque insuficiente).")
        elif opcao == "4":
            numero = ler_numero("Número do prontuário: ")
            if c.remover_medicamento(numero, input("Código do medicamento: ")) is None:
                print("Medicamento não encontrado no prontuário.")
            else:
                print("Medicamento removido.")
        elif opcao == "5":
            numero = ler_numero("Número do prontuário: ")
            nome = input("Procedimento: ")
            valor = ler_valor("Valor: R$ ")
            if c.adicionar_procedimento(numero, nome, valor):
                print("Procedimento adicionado.")
            else:
                print("Prontuário não encontrado.")
        elif opcao == "6":
            numero = ler_numero("Número do prontuário: ")
            if c.remover_procedimento(numero, input("Procedimento: ")) is None:
                print("Procedimento não encontrado no prontuário.")
            else:
                print("Procedimento removido.")
        elif opcao == "7":
            if c.dar_alta(ler_numero("Número do prontuário: ")):
                print("Alta registrada. Consultório liberado.")
            else:
                print("Prontuário não encontrado ou alta já registrada.")
        elif opcao == "8":
            numero = ler_numero("Número do prontuário: ")
            print("1 - PIX | 2 - Cartão | 3 - Dinheiro")
            escolha = input("Forma de pagamento: ")
            parcelas = None
            if escolha == "1":
                forma = "PIX"
            elif escolha == "2":
                forma = "CARTAO"
                parcelas = ler_numero("Número de parcelas (1 = à vista): ")
            else:
                forma = "DINHEIRO"
            pagamento, erro = c.fechar_prontuario(numero, forma, parcelas, hoje)
            if pagamento is None:
                print("Não foi possível fechar:", erro)
            else:
                print("Prontuário fechado. Total pago: R$", pagamento.total)
                mostrar_alertas(c)
        elif opcao == "0":
            return
        else:
            print("Opção inválida.")


def menu_estoque(c):
    while True:
        print("\n--- Estoque ---")
        print("1 - Cadastrar produto")
        print("2 - Registrar compra de lote")
        print("3 - Ver estoque")
        print("4 - Ajustar quantidade de um lote")
        print("5 - Descartar lotes vencidos")
        print("6 - Ver alertas de estoque mínimo")
        print("7 - Ver perdas")
        print("0 - Voltar")
        opcao = input("Opção: ")
        if opcao == "1":
            codigo = input("Código: ")
            nome = input("Nome: ")
            preco = ler_valor("Preço de venda: R$ ")
            minimo = ler_numero("Estoque mínimo: ")
            if c.estoque.cadastrar_produto(codigo, nome, preco, minimo) is None:
                print("Já existe um produto com esse código.")
            else:
                print("Produto cadastrado.")
        elif opcao == "2":
            codigo = input("Código do produto: ")
            fornecedor = input("Fornecedor: ")
            preco = ler_valor("Preço de compra: R$ ")
            compra = ler_data("Data da compra")
            validade = ler_data("Data de validade")
            quantidade = ler_numero("Quantidade: ")
            if c.estoque.comprar_lote(codigo, fornecedor, preco, compra, validade, quantidade) is None:
                print("Produto não encontrado.")
            else:
                print("Lote registrado.")
        elif opcao == "3":
            mostrar_estoque(c)
        elif opcao == "4":
            codigo = input("Código do produto: ")
            lote = ler_numero("Número do lote: ")
            quantidade = ler_numero("Nova quantidade: ")
            if c.estoque.ajustar_quantidade(codigo, lote, quantidade):
                print("Quantidade ajustada.")
            else:
                print("Produto ou lote não encontrado.")
        elif opcao == "5":
            descartados = c.estoque.descartar_vencidos(date.today())
            print(descartados, "lote(s) vencido(s) descartado(s).")
        elif opcao == "6":
            mostrar_alertas(c)
        elif opcao == "7":
            mostrar_perdas(c)
        elif opcao == "0":
            return
        else:
            print("Opção inválida.")


def simular():
    c = Clinica(1)
    hoje = date.today()

    print("\n=== Preparando a clínica ===")
    c.tutores.cadastrar_tutor("Ana Souza", "111", "19 99999-0001")
    c.tutores.cadastrar_animal("111", "Rex", "Cão", "Labrador", 3)
    c.tutores.cadastrar_animal("111", "Mia", "Gato", "SRD", 2)
    c.tutores.cadastrar_tutor("Bruno Lima", "222", "19 99999-0002")
    c.tutores.cadastrar_animal("222", "Bolt", "Cão", "Poodle", 5)
    c.estoque.cadastrar_produto("A1", "Antibiótico", 40, 5)
    c.estoque.comprar_lote("A1", "Fornecedor X", 20, date(2025, 1, 10), date(2025, 6, 1), 3)
    c.estoque.comprar_lote("A1", "Fornecedor X", 22, date(2026, 1, 10), date(2030, 1, 1), 4)
    c.estoque.comprar_lote("A1", "Fornecedor Y", 25, date(2026, 3, 10), date(2030, 1, 1), 6)
    c.estoque.cadastrar_produto("V1", "Vacina antirrábica", 80, 3)
    c.estoque.comprar_lote("V1", "Fornecedor Z", 50, date(2026, 5, 5), date(2030, 1, 1), 3)
    mostrar_estoque(c)

    print("\n=== 1. Chegada dos animais ===")
    c.registrar_chegada("111", "Rex", "vômito", False)
    print("Rex chegou (normal)")
    c.registrar_chegada("111", "Mia", "atropelamento", True)
    print("Mia chegou (EMERGÊNCIA)")
    c.registrar_chegada("222", "Bolt", "ferimento na pata", False)
    print("Bolt chegou (normal)")

    print("\n=== 2. Consultório livre: chamar o próximo ===")
    p = c.chamar_proximo("Dra. Carla")
    mostrar_prontuario(p)

    print("\n=== 3. Diagnóstico ===")
    p.diagnostico.marcar_alterado("R01")
    p.diagnostico.marcar_alterado("P02")
    p.diagnostico.exibir()

    print("\n=== 4. Medicamentos e procedimentos ===")
    c.adicionar_medicamento(p.numero, "A1", 2, hoje)
    c.adicionar_procedimento(p.numero, "Consulta", 100)
    c.adicionar_procedimento(p.numero, "Curativo", 60)
    c.adicionar_procedimento(p.numero, "Raio-X", 120)
    print("O tutor não autorizou o Raio-X, removendo do prontuário")
    c.remover_procedimento(p.numero, "Raio-X")
    mostrar_prontuario(p)

    print("\n=== 5. Alta, fechamento e pagamento ===")
    print("Tentando fechar sem alta:", c.fechar_prontuario(p.numero, "PIX", None, hoje)[1])
    c.dar_alta(p.numero)
    pagamento, erro = c.fechar_prontuario(p.numero, "PIX", None, hoje)
    print("Total pago: R$", pagamento.total)
    mostrar_estoque(c)
    mostrar_perdas(c)

    print("\n=== Próximo animal (consultório liberado) ===")
    p2 = c.chamar_proximo("Dr. Pedro")
    c.adicionar_medicamento(p2.numero, "V1", 1, hoje)
    c.adicionar_procedimento(p2.numero, "Consulta", 100)
    c.dar_alta(p2.numero)
    pagamento, erro = c.fechar_prontuario(p2.numero, "CARTAO", 3, hoje)
    print("Total pago: R$", pagamento.total, "em", pagamento.parcelas, "parcelas")
    mostrar_alertas(c)

    print("\n=== Conferência do que foi consumido e recebido ===")
    mostrar_relatorios(c)


def main():
    c = Clinica(2)
    while True:
        print("\n===== Clínica Veterinária Vet Life =====")
        print("1 - Tutores e animais")
        print("2 - Atendimento")
        print("3 - Prontuário")
        print("4 - Estoque")
        print("5 - Relatórios (consumo, pagamentos e perdas)")
        print("6 - Simular um atendimento completo")
        print("0 - Sair")
        opcao = input("Opção: ")
        if opcao == "1":
            menu_tutores(c)
        elif opcao == "2":
            menu_atendimento(c)
        elif opcao == "3":
            menu_prontuario(c)
        elif opcao == "4":
            menu_estoque(c)
        elif opcao == "5":
            mostrar_relatorios(c)
        elif opcao == "6":
            simular()
        elif opcao == "0":
            print("Até logo!")
            return
        else:
            print("Opção inválida.")


main()
