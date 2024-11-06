# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'order_unit.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_unit(object):
    def setupUi(self, unit):
        if not unit.objectName():
            unit.setObjectName(u"unit")
        unit.resize(635, 117)
        unit.setStyleSheet(u"#unit{\n"
"background-color:rgba(0,0,0,0)\n"
"}\n"
"#wid_order{\n"
"border:2px solid rgba(9,9,9,0.45);\n"
"border-left:none;\n"
"border-top-right-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"\n"
"background-color:rgba(249,249,249,1);\n"
"}\n"
"#wid_user{\n"
"border:2px solid #1B1B1B;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"border-right:none;\n"
"background-color:#1B1B1B\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(unit)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.wid_user = QWidget(unit)
        self.wid_user.setObjectName(u"wid_user")
        self.wid_user.setMinimumSize(QSize(0, 117))
        self.wid_user.setMaximumSize(QSize(16777215, 117))
        self.wid_user.setStyleSheet(u"#user_name{\n"
"color:rgba(249, 249, 249, 1);\n"
"}\n"
"#user_time{\n"
"color:rgba(184, 184, 184, 1);\n"
"}\n"
"QLabel{\n"
"background-color:rgba(0,0,0,0);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.wid_user)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(40, 20, 40, 20)
        self.user_name = QLabel(self.wid_user)
        self.user_name.setObjectName(u"user_name")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_name.sizePolicy().hasHeightForWidth())
        self.user_name.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Pretendard"])
        font.setPointSize(20)
        self.user_name.setFont(font)
        self.user_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.user_name)

        self.user_time = QLabel(self.wid_user)
        self.user_time.setObjectName(u"user_time")
        sizePolicy.setHeightForWidth(self.user_time.sizePolicy().hasHeightForWidth())
        self.user_time.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Pretendard"])
        font1.setPointSize(16)
        self.user_time.setFont(font1)
        self.user_time.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.user_time)


        self.horizontalLayout_4.addWidget(self.wid_user)

        self.wid_order = QWidget(unit)
        self.wid_order.setObjectName(u"wid_order")
        self.wid_order.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.wid_order.sizePolicy().hasHeightForWidth())
        self.wid_order.setSizePolicy(sizePolicy1)
        self.wid_order.setMinimumSize(QSize(0, 117))
        self.wid_order.setMaximumSize(QSize(16777215, 117))
        self.wid_order.setFont(font1)
        self.wid_order.setStyleSheet(u"#order_state{\n"
"border:0px solid none;\n"
"border-radius:37px;\n"
"background-color:#1B1B1B;\n"
"color:#F9F9F9;\n"
"}\n"
"#order_state:disabled{\n"
"border:0px solid none;\n"
"border-radius:37px;\n"
"background-color:#E4E4E4;\n"
"color:#ABABAB;\n"
"}\n"
"#user_requirement{\n"
"color:#EC424C;\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.wid_order)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 24, 0)
        self.widget_2 = QWidget(self.wid_order)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.widget_2.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(24, 1, 24, 1)
        self.menu_count_price = QLabel(self.widget_2)
        self.menu_count_price.setObjectName(u"menu_count_price")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.menu_count_price.sizePolicy().hasHeightForWidth())
        self.menu_count_price.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setFamilies([u"Pretendard"])
        font2.setPointSize(26)
        self.menu_count_price.setFont(font2)

        self.verticalLayout_2.addWidget(self.menu_count_price)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menu_detail = QLabel(self.widget_3)
        self.menu_detail.setObjectName(u"menu_detail")
        sizePolicy3.setHeightForWidth(self.menu_detail.sizePolicy().hasHeightForWidth())
        self.menu_detail.setSizePolicy(sizePolicy3)
        self.menu_detail.setFont(font)

        self.horizontalLayout_2.addWidget(self.menu_detail)

        self.user_requirement = QLabel(self.widget_3)
        self.user_requirement.setObjectName(u"user_requirement")
        sizePolicy.setHeightForWidth(self.user_requirement.sizePolicy().hasHeightForWidth())
        self.user_requirement.setSizePolicy(sizePolicy)
        self.user_requirement.setFont(font1)

        self.horizontalLayout_2.addWidget(self.user_requirement)


        self.verticalLayout_2.addWidget(self.widget_3)


        self.horizontalLayout_3.addWidget(self.widget_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.order_state = QPushButton(self.wid_order)
        self.order_state.setObjectName(u"order_state")
        self.order_state.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.order_state.sizePolicy().hasHeightForWidth())
        self.order_state.setSizePolicy(sizePolicy4)
        self.order_state.setMinimumSize(QSize(74, 74))
        self.order_state.setMaximumSize(QSize(74, 74))
        self.order_state.setFont(font1)
        self.order_state.setCheckable(True)
        self.order_state.setChecked(False)

        self.horizontalLayout_3.addWidget(self.order_state)


        self.horizontalLayout_4.addWidget(self.wid_order)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 5)

        self.retranslateUi(unit)

        QMetaObject.connectSlotsByName(unit)
    # setupUi

    def retranslateUi(self, unit):
        unit.setWindowTitle(QCoreApplication.translate("unit", u"Form", None))
        self.user_name.setText(QCoreApplication.translate("unit", u"\uae40\ub3c4\ud6c8 \ub2d8", None))
        self.user_time.setText(QCoreApplication.translate("unit", u"12:30\ubd84 \uc8fc\ubb38", None))
        self.menu_count_price.setText(QCoreApplication.translate("unit", u"\uba54\ub274 2\uac1c \u2022 \ucd1d 13,000\uc6d0", None))
        self.menu_detail.setText(QCoreApplication.translate("unit", u"\uae40\uce58\ubcf6\uc74c\ubc25\uc678 1\uac1c", None))
        self.user_requirement.setText(QCoreApplication.translate("unit", u"\uace0\uac1d\uc694\uccad\uc0ac\ud56d \uc788\uc74c", None))
        self.order_state.setText(QCoreApplication.translate("unit", u"\uc870\ub9ac\uc644\ub8cc", None))
    # retranslateUi

