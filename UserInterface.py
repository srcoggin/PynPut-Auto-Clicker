# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AutoClicker(object):
    def setupUi(self, AutoClicker):
        AutoClicker.setObjectName("AutoClicker")
        AutoClicker.resize(450, 350)
        AutoClicker.setMinimumSize(QtCore.QSize(450, 350))
        AutoClicker.setMaximumSize(QtCore.QSize(450, 350))
        self.widget = QtWidgets.QWidget(AutoClicker)
        self.widget.setGeometry(QtCore.QRect(0, 0, 451, 341))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(270, 20))
        self.label_2.setMaximumSize(QtCore.QSize(270, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setUnderline(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(100, 20))
        self.label_3.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.Delay_Time_Input = QtWidgets.QLineEdit(self.widget)
        self.Delay_Time_Input.setMinimumSize(QtCore.QSize(115, 20))
        self.Delay_Time_Input.setMaximumSize(QtCore.QSize(115, 20))
        self.Delay_Time_Input.setObjectName("Delay_Time_Input")
        self.horizontalLayout_4.addWidget(self.Delay_Time_Input)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(100, 20))
        self.label_4.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.Start_Key_Input = QtWidgets.QLineEdit(self.widget)
        self.Start_Key_Input.setMinimumSize(QtCore.QSize(115, 20))
        self.Start_Key_Input.setMaximumSize(QtCore.QSize(115, 20))
        self.Start_Key_Input.setObjectName("Start_Key_Input")
        self.horizontalLayout_3.addWidget(self.Start_Key_Input)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setMinimumSize(QtCore.QSize(100, 20))
        self.label_5.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.Stop_Key_Input = QtWidgets.QLineEdit(self.widget)
        self.Stop_Key_Input.setMinimumSize(QtCore.QSize(115, 20))
        self.Stop_Key_Input.setMaximumSize(QtCore.QSize(115, 20))
        self.Stop_Key_Input.setObjectName("Stop_Key_Input")
        self.horizontalLayout_2.addWidget(self.Stop_Key_Input)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.Exit_Button = QtWidgets.QPushButton(self.widget)
        self.Exit_Button.setMinimumSize(QtCore.QSize(90, 30))
        self.Exit_Button.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Exit_Button.setFont(font)
        self.Exit_Button.setObjectName("Exit_Button")
        self.horizontalLayout.addWidget(self.Exit_Button)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem12)
        self.Start_Button = QtWidgets.QPushButton(self.widget)
        self.Start_Button.setMinimumSize(QtCore.QSize(90, 30))
        self.Start_Button.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Start_Button.setFont(font)
        self.Start_Button.setObjectName("Start_Button")
        self.horizontalLayout.addWidget(self.Start_Button)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem13)
        self.About_Me_Button = QtWidgets.QPushButton(self.widget)
        self.About_Me_Button.setMinimumSize(QtCore.QSize(90, 30))
        self.About_Me_Button.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.About_Me_Button.setFont(font)
        self.About_Me_Button.setObjectName("About_Me_Button")
        self.horizontalLayout.addWidget(self.About_Me_Button)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem14)
        self.Save_Info_Button = QtWidgets.QPushButton(self.widget)
        self.Save_Info_Button.setMinimumSize(QtCore.QSize(90, 30))
        self.Save_Info_Button.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Save_Info_Button.setFont(font)
        self.Save_Info_Button.setObjectName("Save_Info_Button")
        self.horizontalLayout.addWidget(self.Save_Info_Button)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem15)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem16)

        self.retranslateUi(AutoClicker)
        QtCore.QMetaObject.connectSlotsByName(AutoClicker)

    def retranslateUi(self, AutoClicker):
        _translate = QtCore.QCoreApplication.translate
        AutoClicker.setWindowTitle(_translate("AutoClicker", "Form"))
        self.label.setText(_translate("AutoClicker", "@srcoggin\'s Automatic Mouse Clicker"))
        self.label_2.setText(_translate("AutoClicker", "Input the information below:"))
        self.label_3.setText(_translate("AutoClicker", "Delay Time:"))
        self.label_4.setText(_translate("AutoClicker", "Start Key:"))
        self.label_5.setText(_translate("AutoClicker", "Stop Key:"))
        self.Exit_Button.setText(_translate("AutoClicker", "Exit"))
        self.Start_Button.setText(_translate("AutoClicker", "Start"))
        self.About_Me_Button.setText(_translate("AutoClicker", "About Me"))
        self.Save_Info_Button.setText(_translate("AutoClicker", "Save Info"))
