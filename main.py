import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Input Nilai Mahasiswa")
        self.setGeometry(100, 100, 400, 300)

       
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.label_uts = QLabel("Nilai UTS:", self)
        self.input_uts = QLineEdit(self)
        layout.addWidget(self.label_uts)
        layout.addWidget(self.input_uts)

        self.label_uas = QLabel("Nilai UAS:", self)
        self.input_uas = QLineEdit(self)
        layout.addWidget(self.label_uas)
        layout.addWidget(self.input_uas)

        self.label_tugas = QLabel("Nilai Tugas:", self)
        self.input_tugas = QLineEdit(self)
        layout.addWidget(self.label_tugas)
        layout.addWidget(self.input_tugas)

        self.label_praktik = QLabel("Nilai Praktikum:", self)
        self.input_praktik = QLineEdit(self)
        layout.addWidget(self.label_praktik)
        layout.addWidget(self.input_praktik)

       
        self.label_nilai_sebelum = QLabel("Nilai Sebelum Diitung:", self)
        layout.addWidget(self.label_nilai_sebelum)

      
        self.button_hitung = QPushButton("Hitung Nilai Akhir", self)
        self.button_hitung.clicked.connect(self.calculate_final_score)
        layout.addWidget(self.button_hitung)

       
        self.button_kosongkan = QPushButton("Kosongkan Inputan", self)
        self.button_kosongkan.clicked.connect(self.clear_inputs)
        layout.addWidget(self.button_kosongkan)

    def calculate_final_score(self):
      
        nilai_uts = float(self.input_uts.text())
        nilai_uas = float(self.input_uas.text())
        nilai_tugas = float(self.input_tugas.text())
        nilai_praktik = float(self.input_praktik.text())

      
        nilai_akhir = (0.2 * nilai_uts) + (0.2 * nilai_uas) + (0.3 * nilai_tugas) + (0.3 * nilai_praktik)

       
        if nilai_akhir >= 80:
            nilai_huruf = "A"
        elif nilai_akhir >= 71:
            nilai_huruf = "B+"
        elif nilai_akhir >= 65:
            nilai_huruf = "B"
        elif nilai_akhir >= 60:
            nilai_huruf = "C+"
        elif nilai_akhir >= 55:
            nilai_huruf = "C"
        elif nilai_akhir >= 50:
            nilai_huruf = "D+"
        elif nilai_akhir >= 40:
            nilai_huruf = "D"
        else:
            nilai_huruf = "E"

       
        msg = f"Nilai Akhir: {nilai_akhir:.2f} | Nilai Huruf: {nilai_huruf}"
        self.statusBar().showMessage(msg)

        
        msg_sebelum = f"UTS: {nilai_uts}, UAS: {nilai_uas}, Tugas: {nilai_tugas}, Praktikum: {nilai_praktik}"
        self.label_nilai_sebelum.setText(msg_sebelum)

    def clear_inputs(self):
     
        self.input_uts.clear()
        self.input_uas.clear()
        self.input_tugas.clear()
        self.input_praktik.clear()
        self.label_nilai_sebelum.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
