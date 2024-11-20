import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class BinaryConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Text to Binary Converter")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.input_line = QLineEdit(self)
        self.input_line.setPlaceholderText("Gib den Text hier ein (z.B. deutsch)")
        layout.addWidget(self.input_line)

        self.convert_button = QPushButton("In Binär umwandeln", self)
        self.convert_button.clicked.connect(self.convert_to_binary)
        layout.addWidget(self.convert_button)

        self.result_label = QLabel("Binäre Darstellung: ", self)
        layout.addWidget(self.result_label)

        self.copy_line = QLineEdit(self)
        self.copy_line.setPlaceholderText("Hier wird der binäre Text angezeigt (kopierbar)")
        self.copy_line.setReadOnly(True)
        layout.addWidget(self.copy_line)

        self.copy_button = QPushButton("Kopieren", self)
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        layout.addWidget(self.copy_button)

        self.setLayout(layout)

    def convert_to_binary(self):
        text = self.input_line.text()
        binary = ' '.join(format(ord(char), '08b') for char in text)
        self.result_label.setText(f"Binäre Darstellung: {binary}")
        self.copy_line.setText(binary)

    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.copy_line.text())
        QMessageBox.information(self, "Kopiert", "Der binäre Text wurde in die Zwischenablage kopiert.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = BinaryConverterApp()
    converter.show()
    sys.exit(app.exec_())
