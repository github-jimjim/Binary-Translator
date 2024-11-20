import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class BinaryToTextConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Binary to Text Converter")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.input_line = QLineEdit(self)
        self.input_line.setPlaceholderText("Gib den binären Text hier ein (z.B. 01001000 01100101 01101100 01101100 01101111 00100000 01010111 01101111 01110010 01101100 01100100)")
        layout.addWidget(self.input_line)

        self.convert_button = QPushButton("In Text umwandeln", self)
        self.convert_button.clicked.connect(self.convert_to_text)
        layout.addWidget(self.convert_button)

        self.result_label = QLabel("Textdarstellung: ", self)
        layout.addWidget(self.result_label)

        self.copy_line = QLineEdit(self)
        self.copy_line.setPlaceholderText("Hier wird der konvertierte Text angezeigt (kopierbar)")
        self.copy_line.setReadOnly(True)
        layout.addWidget(self.copy_line)

        self.copy_button = QPushButton("Kopieren", self)
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        layout.addWidget(self.copy_button)

        self.setLayout(layout)

    def convert_to_text(self):
        binary_input = self.input_line.text()
        try:
            binary_values = binary_input.split(' ')
            ascii_characters = [chr(int(bv, 2)) for bv in binary_values]
            text_output = ''.join(ascii_characters)
            self.result_label.setText(f"Textdarstellung: {text_output}")
            self.copy_line.setText(text_output)
        except ValueError:
            self.result_label.setText("Ungültige Eingabe. Bitte gib gültigen binären Text ein.")

    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.copy_line.text())
        QMessageBox.information(self, "Kopiert", "Der konvertierte Text wurde in die Zwischenablage kopiert.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = BinaryToTextConverterApp()
    converter.show()
    sys.exit(app.exec_())
