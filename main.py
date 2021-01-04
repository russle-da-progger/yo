from PyQt5 import QtCore, QtGui, QtWidgets
import arrays
import sys


class Ui_MainWindow(object):
    def __init__(self):
        self.i = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(851, 638)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_legend_image_air = QtWidgets.QLabel(self.centralwidget)
        self.label_legend_image_air.setGeometry(QtCore.QRect(660, 80, 181, 21))
        self.label_legend_image_air.setText("")
        self.label_legend_image_air.setPixmap(QtGui.QPixmap("legend_components/air.png"))
        self.label_legend_image_air.setScaledContents(True)
        self.label_legend_image_air.setObjectName("label_legend_image_air")
        self.label_legend_title = QtWidgets.QLabel(self.centralwidget)
        self.label_legend_title.setGeometry(QtCore.QRect(660, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_legend_title.setFont(font)
        self.label_legend_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_legend_title.setObjectName("label_legend_title")
        self.label_legend_text_air = QtWidgets.QLabel(self.centralwidget)
        self.label_legend_text_air.setGeometry(QtCore.QRect(660, 50, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_legend_text_air.setFont(font)
        self.label_legend_text_air.setAlignment(QtCore.Qt.AlignCenter)
        self.label_legend_text_air.setObjectName("label_legend_text_air")
        self.label_legend_text_gen_gas = QtWidgets.QLabel(self.centralwidget)
        self.label_legend_text_gen_gas.setGeometry(QtCore.QRect(660, 230, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_legend_text_gen_gas.setFont(font)
        self.label_legend_text_gen_gas.setAlignment(QtCore.Qt.AlignCenter)
        self.label_legend_text_gen_gas.setObjectName("label_legend_text_gen_gas")
        self.label_legend_image_gen_gas = QtWidgets.QLabel(self.centralwidget)
        self.label_legend_image_gen_gas.setGeometry(QtCore.QRect(660, 260, 181, 21))
        self.label_legend_image_gen_gas.setText("")
        self.label_legend_image_gen_gas.setPixmap(QtGui.QPixmap("legend_components/generator_gas.png"))
        self.label_legend_image_gen_gas.setScaledContents(True)
        self.label_legend_image_gen_gas.setObjectName("label_legend_image_gen_gas")
        self.label_legend_text_helium = QtWidgets.QLabel(self.centralwidget)
        self.label_legend_text_helium.setGeometry(QtCore.QRect(660, 290, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_legend_text_helium.setFont(font)
        self.label_legend_text_helium.setAlignment(QtCore.Qt.AlignCenter)
        self.label_legend_text_helium.setObjectName("label_legend_text_helium")
        self.label_legend_image_helium = QtWidgets.QLabel(self.centralwidget)
        self.label_legend_image_helium.setGeometry(QtCore.QRect(660, 320, 181, 21))
        self.label_legend_image_helium.setText("")
        self.label_legend_image_helium.setPixmap(QtGui.QPixmap("legend_components/helium.png"))
        self.label_legend_image_helium.setScaledContents(True)
        self.label_legend_image_helium.setObjectName("label_legend_image_helium")
        self.label_legend_image_oxygen = QtWidgets.QLabel(self.centralwidget)
        self.label_legend_image_oxygen.setGeometry(QtCore.QRect(660, 200, 181, 21))
        self.label_legend_image_oxygen.setText("")
        self.label_legend_image_oxygen.setPixmap(QtGui.QPixmap("legend_components/oxygen.png"))
        self.label_legend_image_oxygen.setScaledContents(True)
        self.label_legend_image_oxygen.setObjectName("label_legend_image_oxygen")
        self.label_legend_image_hydrogen = QtWidgets.QLabel(self.centralwidget)
        self.label_legend_image_hydrogen.setGeometry(QtCore.QRect(660, 140, 181, 21))
        self.label_legend_image_hydrogen.setText("")
        self.label_legend_image_hydrogen.setPixmap(QtGui.QPixmap("legend_components/hydrogen.png"))
        self.label_legend_image_hydrogen.setScaledContents(True)
        self.label_legend_image_hydrogen.setObjectName("label_legend_image_hydrogen")
        self.label_legend_text_oxygen = QtWidgets.QLabel(self.centralwidget)
        self.label_legend_text_oxygen.setGeometry(QtCore.QRect(660, 170, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_legend_text_oxygen.setFont(font)
        self.label_legend_text_oxygen.setAlignment(QtCore.Qt.AlignCenter)
        self.label_legend_text_oxygen.setObjectName("label_legend_text_oxygen")
        self.label_legend_text_hydrogen = QtWidgets.QLabel(self.centralwidget)
        self.label_legend_text_hydrogen.setGeometry(QtCore.QRect(660, 110, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_legend_text_hydrogen.setFont(font)
        self.label_legend_text_hydrogen.setAlignment(QtCore.Qt.AlignCenter)
        self.label_legend_text_hydrogen.setObjectName("label_legend_text_hydrogen")
        self.label_image_outlines = QtWidgets.QLabel(self.centralwidget)
        self.label_image_outlines.setGeometry(QtCore.QRect(0, -20, 661, 441))
        self.label_image_outlines.setText("")
        self.label_image_outlines.setPixmap(QtGui.QPixmap("4_images/outlines.png"))
        self.label_image_outlines.setScaledContents(True)
        self.label_image_outlines.setObjectName("label_image_outlines")
        self.label_image_overlay = QtWidgets.QLabel(self.centralwidget)
        self.label_image_overlay.setGeometry(QtCore.QRect(0, -20, 661, 441))
        self.label_image_overlay.setText("")
        self.label_image_overlay.setPixmap(QtGui.QPixmap("4_images/one.png"))
        self.label_image_overlay.setScaledContents(True)
        self.label_image_overlay.setObjectName("label_image_overlay")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(140, 430, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_forward = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_forward.setGeometry(QtCore.QRect(350, 430, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_forward.setFont(font)
        self.pushButton_forward.setObjectName("pushButton_forward")
        self.label_modes_text = QtWidgets.QLabel(self.centralwidget)
        self.label_modes_text.setGeometry(QtCore.QRect(660, 430, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_modes_text.setFont(font)
        self.label_modes_text.setAlignment(QtCore.Qt.AlignCenter)
        self.label_modes_text.setObjectName("label_modes_text")
        self.textBrowser_description = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_description.setGeometry(QtCore.QRect(10, 480, 641, 151))
        self.textBrowser_description.setObjectName("textBrowser_description")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 460, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_modes_RM_to_ARM_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_modes_RM_to_ARM_2.setGeometry(QtCore.QRect(660, 600, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_modes_RM_to_ARM_2.setFont(font)
        self.pushButton_modes_RM_to_ARM_2.setObjectName("pushButton_modes_RM_to_ARM_2")
        self.radioButton_ground_launch = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_ground_launch.setGeometry(QtCore.QRect(660, 480, 191, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.radioButton_ground_launch.setFont(font)
        self.radioButton_ground_launch.setObjectName("radioButton_ground_launch")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(660, 510, 181, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(660, 540, 171, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(660, 570, 171, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.radioButton_ground_launch.clicked.connect(self.choose_f1)
        self.radioButton_2.clicked.connect(self.choose_f2)
        self.radioButton_3.clicked.connect(self.choose_f3)
        self.radioButton_4.clicked.connect(self.choose_f4)

        self.pushButton_forward.clicked.connect(self.show_next)
        self.pushButton_back.clicked.connect(self.show_prev)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_legend_title.setText(_translate("MainWindow", "Легенда"))
        self.label_legend_text_air.setText(_translate("MainWindow", "Воздух"))
        self.label_legend_text_gen_gas.setText(_translate("MainWindow", "Генераторный Газ"))
        self.label_legend_text_helium.setText(_translate("MainWindow", "Гелий"))
        self.label_legend_text_oxygen.setText(_translate("MainWindow", "Кислород"))
        self.label_legend_text_hydrogen.setText(_translate("MainWindow", "Водород"))
        self.pushButton_back.setText(_translate("MainWindow", "Назад"))
        self.pushButton_forward.setText(_translate("MainWindow", "Вперед"))
        self.label_modes_text.setText(_translate("MainWindow", "Режимы"))
        self.label.setText(_translate("MainWindow", "Описание"))
        self.pushButton_modes_RM_to_ARM_2.setText(_translate("MainWindow", "Полная схема"))
        self.radioButton_ground_launch.setText(_translate("MainWindow", "Наземный запуск двигателя"))
        self.radioButton_2.setText(_translate("MainWindow", "Воздушно-реактивный режим"))
        self.radioButton_3.setText(_translate("MainWindow", "Из ВРР в ракетный режим"))
        self.radioButton_4.setText(_translate("MainWindow", "Из ракетного режима в ВРР"))

    def choose_f1(self):
        self.label_image_overlay.setPixmap(QtGui.QPixmap(arrays.a[0]))
        self.buffer = arrays.a

    def choose_f2(self):
        self.label_image_overlay.setPixmap(QtGui.QPixmap(arrays.b[0]))
        self.buffer = arrays.b

    def choose_f3(self):
        self.label_image_overlay.setPixmap(QtGui.QPixmap(arrays.c[0]))
        self.buffer = arrays.c

    def choose_f4(self):
        self.label_image_overlay.setPixmap(QtGui.QPixmap(arrays.d[0]))
        self.buffer = arrays.d


    def show_prev(self):
        array_ = self.buffer
        self.i -= 1
        if self.i < 0:
            i = len(array_) - 1
        self.label_image_overlay.setPixmap(QtGui.QPixmap(array_[self.i]))

    def show_next(self):
        array_ = self.buffer
        self.i += 1
        if self.i == len(self.b1):
            self.i: int = 0
        self.label_image_overlay.setPixmap(QtGui.QPixmap(array_[self.i]))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec_())
