# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cica.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
##############################################################################

from PySide6.QtCore import QCoreApplication, QRect
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QWidget, QLabel, QLineEdit, 
                              QPushButton, QMessageBox)
from sql import Session, User

class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.pushButton_2.clicked.connect(self.login)

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Form")
        self.resize(400, 337)
        
        # Поле логина
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(QRect(80, 110, 241, 20))
        
        # Поле пароля
        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setGeometry(QRect(80, 170, 241, 20))
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        
        # Надписи
        font = QFont()
        font.setPointSize(10)
        
        self.label = QLabel("Логин", self)
        self.label.setGeometry(QRect(90, 90, 47, 13))
        self.label.setFont(font)
        
        self.label_2 = QLabel("Пароль", self)
        self.label_2.setGeometry(QRect(90, 150, 47, 13))
        self.label_2.setFont(font)
        
        self.label_3 = QLabel("Вход в систему", self)
        self.label_3.setGeometry(QRect(150, 20, 111, 20))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_3.setFont(font1)
        
        # Кнопка входа
        self.pushButton_2 = QPushButton("Вход", self)
        self.pushButton_2.setGeometry(QRect(80, 200, 241, 23))
        self.pushButton_2.setFont(font)

    def login(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()

        session = Session()
        try:
            user = session.query(User).filter_by(
                login=login,
                password=password
            ).first()

            if user:
                QMessageBox.information(
                    self,
                    "Успешный вход",
                    f"Добро пожаловать, {user.fio}!"
                )
                self.close()
            else:
                QMessageBox.warning(
                    self,
                    "Ошибка",
                    "Неверный логин или пароль"
                )
        finally:
            session.close()



