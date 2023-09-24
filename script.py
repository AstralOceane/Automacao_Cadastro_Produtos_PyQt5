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
        self.setWindowTitle("Cadastro de Produtos")
        self.setGeometry(100, 100, 400, 250)

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
        cliente = self.entry_cliente.text()
        produto = self.entry_produto.text()
        quantidade = self.entry_quantidade.text()
        categoria = self.combo_categoria.currentText()

        # Simule um cadastro de sucesso
        success_box = QMessageBox()
        success_box.setText("Produto cadastrado com sucesso!")

        # Inicie um temporizador para fechar a mensagem após 2 segundos
        QTimer.singleShot(2000, success_box.accept)

        success_box.exec_()

        # Limpe os campos após o salvamento
        self.entry_cliente.clear()
        self.entry_produto.clear()
        self.entry_quantidade.clear()
        self.combo_categoria.setCurrentIndex(0)

def preencher_campos_e_clicar(window):
    # Abra o arquivo Excel
    excel_file_path = 'vendas_de_produtos.xlsx'
    workbook = openpyxl.load_workbook(excel_file_path)
    worksheet = workbook.active

    # Leia os dados da primeira linha do arquivo Excel
    row = next(worksheet.iter_rows(min_row=2, values_only=True))
    cliente, produto, _, _ = row

    # Preencha os campos com os valores lidos do arquivo Excel
    window.entry_cliente.setText(cliente)
    window.entry_produto.setText(produto)
    window.entry_quantidade.setText("10")  # Defina a quantidade como 10

    # Clique no botão "Salvar"
    QTest.mouseClick(window.button_salvar, Qt.LeftButton)

    # Aguarde 2 segundos e, em seguida, envie a tecla "ENTER"
    QTimer.singleShot(2000, lambda: pressionar_enter_na_janela("Python"))

def pressionar_enter_na_janela(janela_titulo):
    # Enviar a tecla "ENTER" para a janela com o título "Python"
    for widget in QApplication.topLevelWidgets():
        if widget.windowTitle() == janela_titulo:
            widget.setFocus()
            QTest.keyClick(widget, Qt.Key_Enter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CadastroProdutosApp()
    window.show()

    # Aguarde 2 segundos e, em seguida, preencha os campos e clique no botão "Salvar"
    QTimer.singleShot(2000, lambda: preencher_campos_e_clicar(window))

    sys.exit(app.exec_())
