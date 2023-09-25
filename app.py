import sys
import openpyxl
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt, QTimer

class CadastroProdutosApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configuração da interface gráfica
        self.setWindowTitle("Cadastro de Produtos")
        self.setGeometry(100, 100, 400, 250)

        # Criação de elementos da interface
        self.label_cliente = QLabel("Cliente:", self)
        self.label_cliente.setGeometry(20, 20, 60, 20)
        self.entry_cliente = QLineEdit(self)
        self.entry_cliente.setGeometry(120, 20, 200, 20)

        self.label_produto = QLabel("Produto:", self)
        self.label_produto.setGeometry(20, 50, 60, 20)
        self.entry_produto = QLineEdit(self)
        self.entry_produto.setGeometry(120, 50, 200, 20)

        self.label_quantidade = QLabel("Quantidade:", self)
        self.label_quantidade.setGeometry(20, 80, 80, 20)
        self.entry_quantidade = QLineEdit(self)
        self.entry_quantidade.setGeometry(120, 80, 50, 20)

        self.label_categoria = QLabel("Categoria do Produto:", self)
        self.label_categoria.setGeometry(20, 110, 140, 20)
        self.combo_categoria = QComboBox(self)
        self.combo_categoria.setGeometry(170, 110, 150, 20)
        self.combo_categoria.addItems(["Eletrônicos", "Móveis", "Roupas", "Brinquedos", "Comida", "Bebidas",
                                       "Cosméticos", "Livros", "Esportes", "Jardinagem"])

        self.button_salvar = QPushButton("Salvar", self)
        self.button_salvar.setGeometry(120, 150, 80, 30)
        self.button_salvar.clicked.connect(self.salvar)

    def salvar(self):
               
        # Simular um cadastro de sucesso exibindo uma mensagem
        success_box = QMessageBox()
        success_box.setText("Produto cadastrado com sucesso!")

        # Iniciar um temporizador para fechar a mensagem após 2 segundos
        QTimer.singleShot(2000, success_box.accept)

        success_box.exec_()

        # Limpar os campos após o salvamento
        self.entry_cliente.clear()
        self.entry_produto.clear()
        self.entry_quantidade.clear()
        self.combo_categoria.setCurrentIndex(0)

def preencher_campos_e_clicar(window):
    # Abra o arquivo Excel
    excel_file_path = 'vendas_de_produtos.xlsx'
    workbook = openpyxl.load_workbook(excel_file_path)
    worksheet = workbook.active

    # Se estivermos na primeira chamada, inicie o loop iterando pelas linhas
    if not hasattr(window, 'row_iterator'):
        window.row_iterator = iter(worksheet.iter_rows(min_row=2, values_only=True))

    try:
        # Leia os dados da próxima linha da planilha
        window.current_row = next(window.row_iterator)
        cliente, produto, quantidade, categoria = window.current_row

        # Preencha os campos com os valores lidos do arquivo Excel
        window.entry_cliente.setText(cliente)
        window.entry_produto.setText(produto)
        window.entry_quantidade.setText(str(quantidade))

        # Selecione a categoria correta na combobox
        index = window.combo_categoria.findText(categoria)
        if index >= 0:
            window.combo_categoria.setCurrentIndex(index)

        # Clique no botão "Salvar"
        QTest.mouseClick(window.button_salvar, Qt.LeftButton)

        # Aguarde mais 2 segundos antes de processar a próxima linha
        QTimer.singleShot(2000, lambda: preencher_campos_e_clicar(window))
        
    except StopIteration:
        print("Todos os clientes foram registrados.")
        # Feche a aplicação após registrar todos os clientes
        QTimer.singleShot(2000, window.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CadastroProdutosApp()
    window.show()

    # Aguardar 2 segundos e, em seguida, preencher os campos e clicar no botão "Salvar"
    QTimer.singleShot(2000, lambda: preencher_campos_e_clicar(window))

    sys.exit(app.exec_())
