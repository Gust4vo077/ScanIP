from PyQt5.QtWidgets import QApplication, QFileDialog

def telaPegarDiretorio():
    app = QApplication([])
    caminho, _ = QFileDialog.getOpenFileName(None, "Selecione o arquivo")
    return caminho