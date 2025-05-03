# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget,QMessageBox

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

# 通过继承 ui_form 来防止 ui 更新后覆盖原有代码

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        # 为按钮绑定事件函数
        self.ui.addAddressButton.clicked.connect(self.addAddressButton_event)

    def addAddressButton_event(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("你确定要继续吗？")
        msg.setInformativeText("这是一个警告框。")
        msg.setWindowTitle("警告")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)
        ret = msg.exec()
        if ret == QMessageBox.Ok:
            print("用户点击了OK按钮")
        else:
            print("用户点击了Cancel按钮")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
