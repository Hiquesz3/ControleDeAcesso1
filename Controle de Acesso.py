import sys
import random
import pickle
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, 
    QMessageBox, QMainWindow, QAction, QMenu, QFileDialog, QListWidget, QDialog, 
    QListWidgetItem, QDialogButtonBox, QDateEdit, QGroupBox, QGridLayout
)
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize, QDate

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configurando a janela de login
        self.setWindowTitle("Controle de Acesso - Escola Jubisclaudios Juniors")
        self.setWindowIcon(QIcon('login_icon.png'))

        # Layout principal
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setSpacing(20)

        # Adicionando os widgets
        self.label = QLabel("Bem-vindo ao Sistema", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 24, QFont.Bold))

        self.username_label = QLabel("Nome de usuário:", self)
        self.username_label.setFont(QFont("Arial", 16))
        self.username_input = QLineEdit(self)
        self.username_input.setFont(QFont("Arial", 14))

        self.password_label = QLabel("Senha:", self)
        self.password_label.setFont(QFont("Arial", 16))
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFont(QFont("Arial", 14))

        self.login_button = QPushButton("Login", self)
        self.login_button.setStyleSheet("background-color: #4CAF50; color: white;")
        self.login_button.setFont(QFont("Arial", 16, QFont.Bold))
        self.login_button.clicked.connect(self.open_main_window)

        # Adicionando widgets ao layout
        layout.addWidget(self.label)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addStretch(1)

        self.setLayout(layout)

    def open_main_window(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Verificação de credenciais (simples para exemplo)
        if username == "admin" and password == "admin":
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "Login", "Nome de usuário ou senha incorretos.")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurando a janela principal
        self.setWindowTitle("Sistema")
        self.setWindowIcon(QIcon('login_icon.png'))
        self.setGeometry(500, 200, 800, 600)

        # Configurando a barra de menu
        self.menu_bar = self.menuBar()
        self.cadastro_menu = self.menu_bar.addMenu("Cadastros")

        # Adicionando ações ao menu "Cadastros"
        self.cadastrar_aluno_action = QAction("Cadastrar Aluno", self)
        self.cadastrar_aluno_action.triggered.connect(self.cadastrar_aluno)
        self.cadastro_menu.addAction(self.cadastrar_aluno_action)

        self.cadastrar_usuario_action = QAction("Cadastrar Usuário", self)
        self.cadastrar_usuario_action.triggered.connect(self.cadastrar_usuario)
        self.cadastro_menu.addAction(self.cadastrar_usuario_action)

        self.consulta_menu = self.menu_bar.addMenu("Consulta")

        # Adicionando ações ao menu "Consulta"
        self.consulta_aluno_action = QAction("Consulta Aluno", self)
        self.consulta_aluno_action.triggered.connect(self.consulta_aluno)
        self.consulta_menu.addAction(self.consulta_aluno_action)

        self.consulta_usuario_action = QAction("Consulta Usuário", self)
        self.consulta_usuario_action.triggered.connect(self.consulta_usuario)
        self.consulta_menu.addAction(self.consulta_usuario_action)

        self.acesso_menu = self.menu_bar.addMenu("Liberar Acesso")

        # Adicionando ação ao menu "Liberar Acesso"
        self.liberar_acesso_action = QAction("Liberar Acesso", self)
        self.liberar_acesso_action.triggered.connect(self.liberar_acesso)
        self.acesso_menu.addAction(self.liberar_acesso_action)

    def cadastrar_aluno(self):
        self.cadastrar_aluno_window = CadastrarAlunoWindow()
        self.setCentralWidget(self.cadastrar_aluno_window)

    def cadastrar_usuario(self):
        self.cadastrar_usuario_window = CadastrarUsuarioWindow()
        self.setCentralWidget(self.cadastrar_usuario_window)

    def consulta_aluno(self):
        self.consulta_aluno_window = ConsultaAlunoWindow()
        self.setCentralWidget(self.consulta_aluno_window)

    def consulta_usuario(self):
        self.consulta_usuario_window = ConsultaUsuarioWindow()
        self.setCentralWidget(self.consulta_usuario_window)

    def liberar_acesso(self):
        self.liberar_acesso_window = LiberarAcessoWindow()
        self.setCentralWidget(self.liberar_acesso_window)

class Aluno:
    def __init__(self, nome, mae, pai, telefone, email, cep, endereco, numero, complemento, codigo, foto, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.mae = mae
        self.pai = pai
        self.telefone = telefone
        self.email = email
        self.cep = cep
        self.endereco = endereco
        self.numero = numero
        self.complemento = complemento
        self.codigo = codigo
        self.foto = foto

class CadastrarAlunoWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Layout principal
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)

        # GroupBox para o formulário
        groupbox = QGroupBox("Cadastro de Aluno")
        groupbox.setFont(QFont("Arial", 18, QFont.Bold))
        groupbox.setStyleSheet("QGroupBox { background-color: #f0f0f0; border: 2px solid #CCCCCC; border-radius: 10px; padding: 20px; }")

        # Layout em grade para o formulário
        grid_layout = QGridLayout()

        # Campos do formulário
        self.nome_label = QLabel("Nome do Aluno:", self)
        self.nome_label.setFont(QFont("Arial", 16))
        grid_layout.addWidget(self.nome_label, 1, 0)
        self.nome_input = QLineEdit(self)
        self.nome_input.setFont(QFont("Arial", 14))
        grid_layout.addWidget(self.nome_input, 1, 1)

        self.data_nascimento_label = QLabel("Data de Nascimento:", self)
        self.data_nascimento_label.setFont(QFont("Arial", 16))
        grid_layout.addWidget(self.data_nascimento_label, 2, 0)
        self.data_nascimento_input = QDateEdit(self)
        self.data_nascimento_input.setFont(QFont("Arial", 14))
        self.data_nascimento_input.setCalendarPopup(True)
        self.data_nascimento_input.setDate(QDate.currentDate())
        grid_layout.addWidget(self.data_nascimento_input, 2, 1)

        self.mae_label = QLabel("Nome da Mãe:", self)
        self.mae_label.setFont(QFont("Arial", 16))
        grid_layout.addWidget(self.mae_label, 3, 0)
        self.mae_input = QLineEdit(self)
        self.mae_input.setFont(QFont("Arial", 14))
        grid_layout.addWidget(self.mae_input, 3, 1)

        self.pai_label = QLabel("Nome do Pai:", self)
        self.pai_label.setFont(QFont("Arial", 16))
        grid_layout.addWidget(self.pai_label, 4, 0)
        self.pai_input = QLineEdit(self)
        self.pai_input.setFont(QFont("Arial", 14))
        grid_layout.addWidget(self.pai_input, 4, 1)

        self.telefone_label = QLabel("Telefone:", self)
        self.telefone_label.setFont(QFont("Arial", 16))
        grid_layout.addWidget(self.telefone_label, 5, 0)
        self.telefone_input = QLineEdit(self)
        self.telefone_input.setFont(QFont("Arial", 14))
        grid_layout.addWidget(self.telefone_input, 5, 1)

        self.email_label = QLabel("E-mail:", self)
        self.email_label.setFont(QFont("Arial", 16))
        grid_layout.addWidget(self.email_label, 6, 0)
        self.email_input = QLineEdit(self)
        self.email_input.setFont(QFont("Arial", 14))
        grid_layout.addWidget(self.email_input, 6, 1)

        self.cep_label = QLabel("CEP:", self)
        self.cep_label.setFont(QFont("Arial", 16))
        grid_layout.addWidget(self.cep_label, 7, 0)
        self.cep_input = QLineEdit(self)
        self.cep_input.setFont(QFont("Arial", 14))
        grid_layout.addWidget(self.cep_input, 7, 1)
        self.cep_input.editingFinished.connect(self.buscar_endereco)

        self.endereco_label = QLabel("Endereço:", self)
        self.endereco_label.setFont(QFont("Arial", 16))
        grid_layout.addWidget(self.endereco_label, 8, 0)
        self.endereco_input = QLineEdit(self)
        self.endereco_input.setFont(QFont("Arial", 14))
        grid_layout.addWidget(self.endereco_input, 8, 1)

        self.numero_label = QLabel("Nº:", self)
        self.numero_label.setFont(QFont("Arial", 16))
        grid_layout.addWidget(self.numero_label, 9, 0)
        self.numero_input = QLineEdit(self)
        self.numero_input.setFont(QFont("Arial", 14))
        grid_layout.addWidget(self.numero_input, 9, 1)

        self.complemento_label = QLabel("Complemento:", self)
        self.complemento_label.setFont(QFont("Arial", 16))
        grid_layout.addWidget(self.complemento_label, 10, 0)
        self.complemento_input = QLineEdit(self)
        self.complemento_input.setFont(QFont("Arial", 14))
        grid_layout.addWidget(self.complemento_input, 10, 1)

        self.codigo_label = QLabel("Código de Acesso:", self)
        self.codigo_label.setFont(QFont("Arial", 16))
        grid_layout.addWidget(self.codigo_label, 11, 0)
        self.codigo_input = QLineEdit(self)
        self.codigo_input.setFont(QFont("Arial", 14))
        self.codigo_input.setReadOnly(True)
        grid_layout.addWidget(self.codigo_input, 11, 1)

        # Botões de ações
        hbox = QHBoxLayout()
        self.gerar_codigo_button = QPushButton("Gerar Código", self)
        self.gerar_codigo_button.setFont(QFont("Arial", 14))
        self.gerar_codigo_button.clicked.connect(self.gerar_codigo)
        hbox.addWidget(self.gerar_codigo_button)

        self.foto_button = QPushButton("Selecionar Foto", self)
        self.foto_button.setFont(QFont("Arial", 14))
        self.foto_button.clicked.connect(self.selecionar_foto)
        hbox.addWidget(self.foto_button)

        grid_layout.addLayout(hbox, 12, 0, 1, 2)
        self.salvar_button = QPushButton("Salvar", self)
        self.salvar_button.setFont(QFont("Arial", 16, QFont.Bold))
        self.salvar_button.clicked.connect(self.salvar_aluno)
        grid_layout.addWidget(self.salvar_button, 13, 0, 1, 2)

        groupbox.setLayout(grid_layout)
        layout.addWidget(groupbox)
        self.setLayout(layout)

        self.foto_data = None

    def buscar_endereco(self):
        cep = self.cep_input.text()
        if cep:
            try:
                response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
                data = response.json()
                endereco = data.get("logradouro", "")
                bairro = data.get("bairro", "")
                cidade = data.get("localidade", "")
                uf = data.get("uf", "")
                self.endereco_input.setText(f"{endereco}, {bairro}, {cidade} - {uf}")
            except Exception as e:
                QMessageBox.warning(self, "Erro", f"Erro ao buscar endereço: {str(e)}")
                self.endereco_input.clear()
        else:
            self.endereco_input.clear()

    def gerar_codigo(self):
        codigo = ''.join(random.choices('0123456789', k=5))
        self.codigo_input.setText(codigo)

    def selecionar_foto(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Selecionar Foto", "", "Imagens (*.png *.jpg *.jpeg)")
        if filename:
            with open(filename, "rb") as file:
                self.foto_data = file.read()

    def salvar_aluno(self):
        nome = self.nome_input.text()
        data_nascimento = self.data_nascimento_input.date().toString(Qt.ISODate)
        mae = self.mae_input.text()
        pai = self.pai_input.text()
        telefone = self.telefone_input.text()
        email = self.email_input.text()
        cep = self.cep_input.text()
        endereco = self.endereco_input.text()
        numero = self.numero_input.text()
        complemento = self.complemento_input.text()
        codigo = self.codigo_input.text()

        if not all([nome, mae, pai, telefone, email, cep, endereco, numero, complemento, codigo]):
            QMessageBox.warning(self, "Erro", "Todos os campos são obrigatórios.")
            return

        aluno = Aluno(nome, mae, pai, telefone, email, cep, endereco, numero, complemento, codigo, self.foto_data, data_nascimento)

        try:
            with open('alunos.pkl', 'ab') as f:
                pickle.dump(aluno, f)
            QMessageBox.information(self, "Sucesso", "Aluno cadastrado com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar os dados: {str(e)}")

        self.reset_form()

    def reset_form(self):
        self.nome_input.clear()
        self.data_nascimento_input.setDate(QDate.currentDate())
        self.mae_input.clear()
        self.pai_input.clear()
        self.telefone_input.clear()
        self.email_input.clear()
        self.cep_input.clear()
        self.endereco_input.clear()
        self.numero_input.clear()
        self.complemento_input.clear()
        self.codigo_input.clear()
        self.foto_data = None

class ConsultaAlunoWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Layout principal
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)

        # Lista de alunos
        self.alunos_list = QListWidget(self)
        self.alunos_list.setFont(QFont("Arial", 14))
        layout.addWidget(self.alunos_list)

        self.load_alunos()

        self.setLayout(layout)

    def load_alunos(self):
        self.alunos_list.clear()
        try:
            with open('alunos.pkl', 'rb') as f:
                while True:
                    try:
                        aluno = pickle.load(f)
                        item = QListWidgetItem(aluno.nome)
                        item.setData(Qt.UserRole, aluno)
                        self.alunos_list.addItem(item)
                    except EOFError:
                        break
        except FileNotFoundError:
            pass

class DetalhesAlunoDialog(QDialog):
    def __init__(self, aluno):
        super().__init__()

        # Configurando a janela de detalhes do aluno
        self.setWindowTitle(aluno.nome)
        self.setWindowIcon(QIcon('login_icon.png'))

        # Layout principal
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        # Adicionando os widgets com os detalhes do aluno
        layout.addWidget(QLabel(f"Nome: {aluno.nome}", self))
        layout.addWidget(QLabel(f"Data de Nascimento: {aluno.data_nascimento}", self))
        layout.addWidget(QLabel(f"Nome da Mãe: {aluno.mae}", self))
        layout.addWidget(QLabel(f"Nome do Pai: {aluno.pai}", self))
        layout.addWidget(QLabel(f"Telefone: {aluno.telefone}", self))
        layout.addWidget(QLabel(f"E-mail: {aluno.email}", self))
        layout.addWidget(QLabel(f"CEP: {aluno.cep}", self))
        layout.addWidget(QLabel(f"Endereço: {aluno.endereco}", self))
        layout.addWidget(QLabel(f"Nº: {aluno.numero}", self))
        layout.addWidget(QLabel(f"Complemento: {aluno.complemento}", self))
        layout.addWidget(QLabel(f"Código de Acesso: {aluno.codigo}", self))

        if aluno.foto:
            pixmap = QPixmap()
            pixmap.loadFromData(aluno.foto)
            foto_label = QLabel(self)
            foto_label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            layout.addWidget(foto_label)

        # Botão para fechar a janela
        button_box = QDialogButtonBox(QDialogButtonBox.Ok)
        button_box.accepted.connect(self.accept)
        layout.addWidget(button_box)

        self.setLayout(layout)

class CadastrarUsuarioWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Layout principal
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)

        # GroupBox para o formulário
        groupbox = QGroupBox("Cadastro de Usuário")
        groupbox.setFont(QFont("Arial", 18, QFont.Bold))
        groupbox.setStyleSheet("QGroupBox { background-color: #f0f0f0; border: 2px solid #CCCCCC; border-radius: 10px; padding: 20px; }")

        # Layout em grade para o formulário
        grid_layout = QGridLayout()

        # Campos do formulário
        self.nome_label = QLabel("Nome do Usuário:", self)
        self.nome_label.setFont(QFont("Arial", 16))
        grid_layout.addWidget(self.nome_label, 1, 0)
        self.nome_input = QLineEdit(self)
        self.nome_input.setFont(QFont("Arial", 14))
        grid_layout.addWidget(self.nome_input, 1, 1)

        self.senha_label = QLabel("Senha:", self)
        self.senha_label.setFont(QFont("Arial", 16))
        grid_layout.addWidget(self.senha_label, 2, 0)
        self.senha_input = QLineEdit(self)
        self.senha_input.setFont(QFont("Arial", 14))
        self.senha_input.setEchoMode(QLineEdit.Password)
        grid_layout.addWidget(self.senha_input, 2, 1)

        self.salvar_button = QPushButton("Salvar", self)
        self.salvar_button.setFont(QFont("Arial", 16, QFont.Bold))
        self.salvar_button.clicked.connect(self.salvar_usuario)
        grid_layout.addWidget(self.salvar_button, 3, 0, 1, 2)

        groupbox.setLayout(grid_layout)
        layout.addWidget(groupbox)
        self.setLayout(layout)

    def salvar_usuario(self):
        nome = self.nome_input.text()
        senha = self.senha_input.text()

        if not nome or not senha:
            QMessageBox.warning(self, "Erro", "Todos os campos são obrigatórios.")
            return

        try:
            with open('usuarios.pkl', 'ab') as f:
                pickle.dump((nome, senha), f)
            QMessageBox.information(self, "Sucesso", "Usuário cadastrado com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar os dados: {str(e)}")

        self.nome_input.clear()
        self.senha_input.clear()

class ConsultaUsuarioWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Layout principal
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)

        # Lista de usuários
        self.usuarios_list = QListWidget(self)
        self.usuarios_list.setFont(QFont("Arial", 14))
        layout.addWidget(self.usuarios_list)

        self.load_usuarios()

        self.setLayout(layout)

    def load_usuarios(self):
        self.usuarios_list.clear()
        try:
            with open('usuarios.pkl', 'rb') as f:
                while True:
                    try:
                        nome, _ = pickle.load(f)
                        item = QListWidgetItem(nome)
                        self.usuarios_list.addItem(item)
                    except EOFError:
                        break
        except FileNotFoundError:
            pass

class LiberarAcessoWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Layout principal
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setSpacing(20)

        # GroupBox para o formulário
        groupbox = QGroupBox("Liberar Acesso")
        groupbox.setFont(QFont("Arial", 18, QFont.Bold))
        groupbox.setStyleSheet("QGroupBox { background-color: #f0f0f0; border: 2px solid #CCCCCC; border-radius: 10px; padding: 20px; }")

        # Layout em grade para o formulário
        grid_layout = QGridLayout()

        # Campo para inserir o código
        self.codigo_label = QLabel("Código de Acesso:", self)
        self.codigo_label.setFont(QFont("Arial", 16))
        grid_layout.addWidget(self.codigo_label, 1, 0)
        self.codigo_input = QLineEdit(self)
        self.codigo_input.setFont(QFont("Arial", 14))
        grid_layout.addWidget(self.codigo_input, 1, 1)

        # Botões de ações
        self.liberar_button = QPushButton("Liberar Aluno", self)
        self.liberar_button.setFont(QFont("Arial", 16, QFont.Bold))
        self.liberar_button.clicked.connect(self.liberar_aluno)
        grid_layout.addWidget(self.liberar_button, 2, 0)

        self.registrar_saida_button = QPushButton("Registrar Saída", self)
        self.registrar_saida_button.setFont(QFont("Arial", 16, QFont.Bold))
        self.registrar_saida_button.clicked.connect(self.registrar_saida)
        grid_layout.addWidget(self.registrar_saida_button, 2, 1)

        groupbox.setLayout(grid_layout)
        layout.addWidget(groupbox)

        # Lista de alunos
        self.alunos_list = QListWidget(self)
        self.alunos_list.setFont(QFont("Arial", 14))
        layout.addWidget(self.alunos_list)

        self.setLayout(layout)

        self.load_alunos()

    def load_alunos(self):
        self.alunos_list.clear()
        try:
            with open('alunos_liberados.pkl', 'rb') as f:
                while True:
                    try:
                        aluno = pickle.load(f)
                        item = QListWidgetItem(f"{aluno.nome} (Código: {aluno.codigo})")
                        self.alunos_list.addItem(item)
                    except EOFError:
                        break
        except FileNotFoundError:
            pass

    def liberar_aluno(self):
        codigo = self.codigo_input.text()

        if not codigo:
            QMessageBox.warning(self, "Erro", "O código de acesso é obrigatório.")
            return

        try:
            with open('alunos.pkl', 'rb') as f:
                alunos = []
                while True:
                    try:
                        aluno = pickle.load(f)
                        if aluno.codigo == codigo:
                            with open('alunos_liberados.pkl', 'ab') as f_liberados:
                                pickle.dump(aluno, f_liberados)
                            self.load_alunos()
                            QMessageBox.information(self, "Sucesso", f"Acesso liberado para {aluno.nome}")
                            return
                        alunos.append(aluno)
                    except EOFError:
                        break

            with open('alunos.pkl', 'wb') as f:
                for aluno in alunos:
                    pickle.dump(aluno, f)

            QMessageBox.warning(self, "Erro", "Código de acesso não encontrado.")
        except FileNotFoundError:
            QMessageBox.warning(self, "Erro", "Nenhum aluno cadastrado.")

    def registrar_saida(self):
        codigo = self.codigo_input.text()

        if not codigo:
            QMessageBox.warning(self, "Erro", "O código de acesso é obrigatório.")
            return

        try:
            with open('alunos_liberados.pkl', 'rb') as f:
                alunos_liberados = []
                while True:
                    try:
                        aluno = pickle.load(f)
                        if aluno.codigo != codigo:
                            alunos_liberados.append(aluno)
                    except EOFError:
                        break

            with open('alunos_liberados.pkl', 'wb') as f:
                for aluno in alunos_liberados:
                    pickle.dump(aluno, f)

            self.load_alunos()
            QMessageBox.information(self, "Sucesso", "Saída registrada com sucesso.")
        except FileNotFoundError:
            QMessageBox.warning(self, "Erro", "Nenhum aluno liberado.")

# Função principal para executar o aplicativo
def main():
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
