# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vmf2obj.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
import subprocess


class Ui_vmf2obj(object):
    fullstring = "Nothing"
    a = False
    b = False
    c = False
    d = False
    e = False
    t = False
    def textchange(self):
        if len(self.lineEdit.text()) < 1:
            self.e = False
        else:
            self.e = True
        self.updatecheck()

    def vmf2objscript(self):
        # toolbrush check
        # Launch
        x = 'java -jar .\VMF2OBJ.jar'
        # vmf location
        # y = '.\spawn_test.vmf'
        # Team fortress 2 folder location
        # z = 'E:\Steam\steamapps\common\Team Fortress 2'
        # Output location
        # v = 'C:\POOP'
        # Output name
        # v1 = 'anus'
        ax = self.tf2_text.text()
        a1 = ax + r"\tf\tf2_misc_dir.vpk"
        a2 = ax + r"\tf\tf2_textures_dir.vpk"
        a3 = ax + r"\hl2\hl2_misc_dir.vpk"
        a4 = ax + r"\hl2\hl2_textures_dir.vpk"
        fullstring = (f'{x} "{self.vmf_text.text()}" "{self.output_text.text()}\\{self.lineEdit.text()}" "{a1};{a2};{a3};{a4}" -e "{self.custom_text.text()}"')
        if self.t == True:
            fullstring = fullstring+" -t"
        print(fullstring)
        subprocess.run(fullstring,shell=True)
    def updatecheck(self):
        if self.a == True and self.b == True and self.c == True and self.d == True and self.e == True:
            self.VMF2OBJ_Start.setEnabled(True)
        else:
            self.VMF2OBJ_Start.setEnabled(False)

    def vmf_find(self):
        vmf_location = QtWidgets.QFileDialog.getOpenFileName(None, "Select Vmf", "", "Vmf Files (*.vmf)")
        self.vmf_text.setText(vmf_location[0])
        if len(str(self.vmf_text)) != 0:
            self.d = True
        else:
            self.d = False
        self.updatecheck()

    def tf2_find(self):
        tf2_location = QtWidgets.QFileDialog.getExistingDirectory(None, "Select your Team Fortress 2 folder", "C:/")
        self.tf2_text.setText(tf2_location)
        if len(str(self.tf2_text)) != 0:
            self.c = True
        else:
            self.c = False
        self.updatecheck()

    def custom_find(self):
        custom_location = QtWidgets.QFileDialog.getExistingDirectory(None, "Select your custom content folder")
        self.custom_text.setText(custom_location)
        if len(str(self.custom_text)) != 0:
            self.b = True
        else:
            self.b = False
        self.updatecheck()

    def output_find(self):
        output_location = QtWidgets.QFileDialog.getExistingDirectory(None, "Select your output folder")
        self.output_text.setText(output_location)
        if len(str(self.output_text)) != 0:
            self.a = True
        else:
            self.a = False
        self.updatecheck()

    def checkboxfun(self):
        if self.checkBox.checkState() == 0:
            self.t = False
        else:
            self.t = True

    def setupUi(self, vmf2obj):
        vmf2obj.setObjectName("vmf2obj")
        vmf2obj.resize(401, 220)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(vmf2obj.sizePolicy().hasHeightForWidth())
        vmf2obj.setSizePolicy(sizePolicy)
        vmf2obj.setMinimumSize(QtCore.QSize(401, 220))
        vmf2obj.setMaximumSize(QtCore.QSize(401, 220))
        vmf2obj.setWindowTitle("VMF2OBJ")
        self.VMF2OBJ_Start = QtWidgets.QPushButton(vmf2obj)
        self.VMF2OBJ_Start.setEnabled(False)
        self.VMF2OBJ_Start.setGeometry(QtCore.QRect(130, 170, 261, 41))
        self.VMF2OBJ_Start.setCheckable(False)
        self.VMF2OBJ_Start.setObjectName("VMF2OBJ_Start")
        self.vmf_button = QtWidgets.QToolButton(vmf2obj)
        self.vmf_button.setGeometry(QtCore.QRect(10, 10, 41, 31))
        self.vmf_button.setObjectName("vmf_button")
        self.vmf_text = QtWidgets.QLineEdit(vmf2obj)
        self.vmf_text.setGeometry(QtCore.QRect(60, 10, 331, 31))
        self.vmf_text.setReadOnly(True)
        self.vmf_text.setObjectName("vmf_text")
        self.tf2_text = QtWidgets.QLineEdit(vmf2obj)
        self.tf2_text.setGeometry(QtCore.QRect(60, 50, 331, 31))
        self.tf2_text.setReadOnly(True)
        self.tf2_text.setObjectName("tf2_text")
        self.tf2_button = QtWidgets.QToolButton(vmf2obj)
        self.tf2_button.setGeometry(QtCore.QRect(10, 50, 41, 31))
        self.tf2_button.setObjectName("tf2_button")
        self.output_button = QtWidgets.QToolButton(vmf2obj)
        self.output_button.setGeometry(QtCore.QRect(10, 130, 41, 31))
        self.output_button.setObjectName("output_button")
        self.output_text = QtWidgets.QLineEdit(vmf2obj)
        self.output_text.setGeometry(QtCore.QRect(60, 130, 331, 31))
        self.output_text.setReadOnly(True)
        self.output_text.setObjectName("output_text")
        self.custom_button = QtWidgets.QToolButton(vmf2obj)
        self.custom_button.setGeometry(QtCore.QRect(10, 90, 41, 31))
        self.custom_button.setObjectName("custom_button")
        self.custom_text = QtWidgets.QLineEdit(vmf2obj)
        self.custom_text.setGeometry(QtCore.QRect(60, 90, 331, 31))
        self.custom_text.setText("")
        self.custom_text.setReadOnly(True)
        self.custom_text.setObjectName("custom_text")
        self.checkBox = QtWidgets.QCheckBox(vmf2obj)
        self.checkBox.setGeometry(QtCore.QRect(10, 170, 121, 17))
        self.checkBox.setObjectName("checkBox")
        self.lineEdit = QtWidgets.QLineEdit(vmf2obj)
        self.lineEdit.setGeometry(QtCore.QRect(10, 190, 113, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(vmf2obj)
        QtCore.QMetaObject.connectSlotsByName(vmf2obj)

        self.VMF2OBJ_Start.clicked.connect(self.vmf2objscript)
        self.vmf_button.clicked.connect(self.vmf_find)
        self.tf2_button.clicked.connect(self.tf2_find)
        self.custom_button.clicked.connect(self.custom_find)
        self.output_button.clicked.connect(self.output_find)
        self.checkBox.clicked.connect(self.checkboxfun)
        self.lineEdit.textChanged.connect(self.textchange)

    def retranslateUi(self, vmf2obj):
        _translate = QtCore.QCoreApplication.translate
        self.VMF2OBJ_Start.setText(_translate("vmf2obj", "VMF2OBJ"))
        self.vmf_button.setText(_translate("vmf2obj", "Vmf"))
        self.vmf_text.setPlaceholderText(_translate("vmf2obj", "Your vmf location"))
        self.tf2_text.setPlaceholderText(_translate("vmf2obj", "Your Team Fortress 2 folder location"))
        self.tf2_button.setText(_translate("vmf2obj", "Tf2"))
        self.output_button.setText(_translate("vmf2obj", "Output"))
        self.output_text.setPlaceholderText(_translate("vmf2obj", "Output folder for your .obj"))
        self.custom_button.setText(_translate("vmf2obj", "Custom"))
        self.custom_text.setPlaceholderText(_translate("vmf2obj", "Custom assets folder"))
        self.checkBox.setText(_translate("vmf2obj", "Ignore tool brushes"))
        self.lineEdit.setPlaceholderText(_translate("vmf2obj", "Outputname"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    vmf2obj = QtWidgets.QDialog()
    ui = Ui_vmf2obj()
    ui.setupUi(vmf2obj)
    vmf2obj.show()
    sys.exit(app.exec_())
