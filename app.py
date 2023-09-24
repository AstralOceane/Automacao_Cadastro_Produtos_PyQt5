import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox

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

        # Você pode chamar uma função aqui para executar comandos externos com esses valores
        # Por enquanto, apenas mostraremos uma mensagem
        QMessageBox.information(self, "Sucesso", "Produto cadastrado com sucesso!")

        # Limpe os campos após o salvamento
        self.entry_cliente.clear()
        self.entry_produto.clear()
        self.entry_quantidade.clear()
        self.combo_categoria.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CadastroProdutosApp()
    window.show()
    sys.exit(app.exec_())
