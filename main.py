import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QDial, QSlider, QApplication, QBoxLayout


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.dl = QDial()
        self.sd = QSlider(Qt.Horizontal)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("Signal Slot")
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        self.setLayout(form_lbx)

        form_lbx.addWidget(self.dl)
        form_lbx.addWidget(self.sd)

        # 시그널 슬롯 연결
        # 다이얼의 값이 변하면 슬라이더의 값을 변경하는 슬롯과 연결
        # 슬라이더의 값이 변화하면 다이얼의 값을 변경하는 슬롯과 연결
        # 두 위젯의 valueChange 시그널은 현재값을 int형으로 반환
        # 두 위젯의 setValue 슬롯은 int형만을 받는다.
        self.dl.valueChanged.connect(self.sd.setValue)
        self.sd.valueChanged.connect(self.dl.setValue)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
