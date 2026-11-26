import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)  # 1. la aplicación
ventana = QMainWindow()      # 2. la ventana
ventana.setWindowTitle("Cooperativa")
ventana.resize(800, 500)

ventana.show()
sys.exit(app.exec())