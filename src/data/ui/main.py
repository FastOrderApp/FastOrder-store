# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QFrame,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.resize(1024, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1024, 768))
        MainWindow.setMaximumSize(QSize(1024, 768))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.stacked_main = QStackedWidget(self.centralwidget)
        self.stacked_main.setObjectName(u"stacked_main")
        self.stacked_main.setGeometry(QRect(0, 160, 1024, 599))
        font = QFont()
        font.setFamilies([u"Pretendard"])
        font.setPointSize(20)
        self.stacked_main.setFont(font)
        self.stacked_main.setStyleSheet(u"#stacked_main{\n"
"background-color:#F9F9F9;\n"
"border:0px solid #F9F9F9;\n"
"}\n"
"#page_history{\n"
"background-color:#F9F9F9;\n"
"border:0px solid #F9F9F9;\n"
"}\n"
"#page_eat{\n"
"background-color:#F9F9F9;\n"
"border:0px solid #F9F9F9;\n"
"}\n"
"#page_pickup{\n"
"background-color:#F9F9F9;\n"
"border:0px solid #F9F9F9;\n"
"}\n"
"#page_setting{\n"
"background-color:#F9F9F9;\n"
"border:0px solid #F9F9F9;\n"
"}")
        self.page_pickup = QWidget()
        self.page_pickup.setObjectName(u"page_pickup")
        self.btn_pickup_wait = QPushButton(self.page_pickup)
        self.btn_pickup_wait.setObjectName(u"btn_pickup_wait")
        self.btn_pickup_wait.setEnabled(False)
        self.btn_pickup_wait.setGeometry(QRect(65, 30, 150, 60))
        self.btn_pickup_wait.setFont(font)
        self.btn_pickup_wait.setStyleSheet(u"QPushButton{\n"
"border:2px solid #8D8D8D;\n"
"border-radius:29px;\n"
"color:#8D8D8D;\n"
"}\n"
"QPushButton:disabled{\n"
"border:2px solid black;\n"
"color:white;\n"
"background-color:black;\n"
"}")
        self.btn_pickup_wait.setCheckable(True)
        self.btn_pickup_wait.setChecked(True)
        self.btn_pickup_processing = QPushButton(self.page_pickup)
        self.btn_pickup_processing.setObjectName(u"btn_pickup_processing")
        self.btn_pickup_processing.setGeometry(QRect(224, 30, 150, 60))
        self.btn_pickup_processing.setFont(font)
        self.btn_pickup_processing.setStyleSheet(u"QPushButton{\n"
"border:2px solid #8D8D8D;\n"
"border-radius:29px;\n"
"color:#8D8D8D;\n"
"}\n"
"QPushButton:disabled{\n"
"border:2px solid black;\n"
"color:white;\n"
"background-color:black;\n"
"}")
        self.btn_pickup_processing.setCheckable(True)
        self.btn_pickup_processing.setChecked(False)
        self.btn_pickup_history = QPushButton(self.page_pickup)
        self.btn_pickup_history.setObjectName(u"btn_pickup_history")
        self.btn_pickup_history.setGeometry(QRect(383, 30, 150, 60))
        self.btn_pickup_history.setFont(font)
        self.btn_pickup_history.setStyleSheet(u"QPushButton{\n"
"border:2px solid #8D8D8D;\n"
"border-radius:29px;\n"
"color:#8D8D8D;\n"
"}\n"
"QPushButton:disabled{\n"
"border:2px solid black;\n"
"color:white;\n"
"background-color:black;\n"
"}")
        self.btn_pickup_history.setCheckable(True)
        self.btn_pickup_history.setChecked(False)
        self.pickup_orders = QWidget(self.page_pickup)
        self.pickup_orders.setObjectName(u"pickup_orders")
        self.pickup_orders.setEnabled(True)
        self.pickup_orders.setGeometry(QRect(55, 109, 812, 440))
        self.pickup_orders.setStyleSheet(u"#pickup_orders{\n"
"border-image: url(:/pickup/pickup/orders_blank.png);\n"
"}\n"
"#pickup_orders:disabled{\n"
"border-image: url(:/pickup/pickup/orders.png);\n"
"}\n"
"")
        self.lay_pickup_order = QVBoxLayout(self.pickup_orders)
        self.lay_pickup_order.setSpacing(22)
        self.lay_pickup_order.setObjectName(u"lay_pickup_order")
        self.lay_pickup_order.setContentsMargins(22, 22, 22, 22)
        self.pickup_updown = QWidget(self.page_pickup)
        self.pickup_updown.setObjectName(u"pickup_updown")
        self.pickup_updown.setEnabled(True)
        self.pickup_updown.setGeometry(QRect(888, 109, 81, 440))
        self.pickup_updown.setStyleSheet(u"#pickup_updown{\n"
"border-image: url(:/pickup/pickup/up_down.png);\n"
"}\n"
"QPushButton{\n"
"background-color:rgba(0,0,0,0);}\n"
"QPushButton:disabled{\n"
"background-color:rgba(249,249,249,0.7);}")
        self.verticalLayout = QVBoxLayout(self.pickup_updown)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 20, 4, 20)
        self.btn_pickup_up = QPushButton(self.pickup_updown)
        self.btn_pickup_up.setObjectName(u"btn_pickup_up")
        self.btn_pickup_up.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_pickup_up.sizePolicy().hasHeightForWidth())
        self.btn_pickup_up.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.btn_pickup_up)

        self.btn_pickup_down = QPushButton(self.pickup_updown)
        self.btn_pickup_down.setObjectName(u"btn_pickup_down")
        self.btn_pickup_down.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.btn_pickup_down.sizePolicy().hasHeightForWidth())
        self.btn_pickup_down.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.btn_pickup_down)

        self.lab_pickup_page = QLabel(self.page_pickup)
        self.lab_pickup_page.setObjectName(u"lab_pickup_page")
        self.lab_pickup_page.setGeometry(QRect(0, 560, 1024, 16))
        font1 = QFont()
        font1.setFamilies([u"Pretendard"])
        font1.setPointSize(24)
        self.lab_pickup_page.setFont(font1)
        self.lab_pickup_page.setStyleSheet(u"color:#8D8D8D;")
        self.lab_pickup_page.setAlignment(Qt.AlignCenter)
        self.lab_pickup_page.setIndent(-1)
        self.stacked_main.addWidget(self.page_pickup)
        self.page_eat = QWidget()
        self.page_eat.setObjectName(u"page_eat")
        self.eat_orders = QWidget(self.page_eat)
        self.eat_orders.setObjectName(u"eat_orders")
        self.eat_orders.setEnabled(True)
        self.eat_orders.setGeometry(QRect(55, 109, 812, 440))
        self.eat_orders.setStyleSheet(u"#eat_orders{\n"
"border-image: url(:/pickup/pickup/orders_blank.png);\n"
"}\n"
"#eat_orders:disabled{\n"
"border-image: url(:/pickup/pickup/orders.png);\n"
"}\n"
"")
        self.lay_eat_order = QVBoxLayout(self.eat_orders)
        self.lay_eat_order.setSpacing(22)
        self.lay_eat_order.setObjectName(u"lay_eat_order")
        self.lay_eat_order.setContentsMargins(22, 22, 22, 22)
        self.eat_updown = QWidget(self.page_eat)
        self.eat_updown.setObjectName(u"eat_updown")
        self.eat_updown.setGeometry(QRect(888, 109, 81, 440))
        self.eat_updown.setStyleSheet(u"#eat_updown{\n"
"border-image: url(:/pickup/pickup/up_down.png);\n"
"}\n"
"QPushButton{\n"
"background-color:rgba(0,0,0,0);}\n"
"\n"
"QPushButton:disabled{\n"
"background-color:rgba(249,249,249,0.7);}")
        self.verticalLayout_3 = QVBoxLayout(self.eat_updown)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(4, 20, 4, 20)
        self.btn_eat_up = QPushButton(self.eat_updown)
        self.btn_eat_up.setObjectName(u"btn_eat_up")
        sizePolicy1.setHeightForWidth(self.btn_eat_up.sizePolicy().hasHeightForWidth())
        self.btn_eat_up.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.btn_eat_up)

        self.btn_eat_down = QPushButton(self.eat_updown)
        self.btn_eat_down.setObjectName(u"btn_eat_down")
        sizePolicy1.setHeightForWidth(self.btn_eat_down.sizePolicy().hasHeightForWidth())
        self.btn_eat_down.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.btn_eat_down)

        self.btn_eat_wait = QPushButton(self.page_eat)
        self.btn_eat_wait.setObjectName(u"btn_eat_wait")
        self.btn_eat_wait.setEnabled(False)
        self.btn_eat_wait.setGeometry(QRect(65, 30, 150, 60))
        self.btn_eat_wait.setFont(font)
        self.btn_eat_wait.setStyleSheet(u"QPushButton{\n"
"border:2px solid #8D8D8D;\n"
"border-radius:29px;\n"
"color:#8D8D8D;\n"
"}\n"
"QPushButton:disabled{\n"
"border:2px solid black;\n"
"color:white;\n"
"background-color:black;\n"
"}")
        self.btn_eat_wait.setCheckable(True)
        self.btn_eat_wait.setChecked(True)
        self.btn_eat_processing = QPushButton(self.page_eat)
        self.btn_eat_processing.setObjectName(u"btn_eat_processing")
        self.btn_eat_processing.setGeometry(QRect(224, 30, 150, 60))
        self.btn_eat_processing.setFont(font)
        self.btn_eat_processing.setStyleSheet(u"QPushButton{\n"
"border:2px solid #8D8D8D;\n"
"border-radius:29px;\n"
"color:#8D8D8D;\n"
"}\n"
"QPushButton:disabled{\n"
"border:2px solid black;\n"
"color:white;\n"
"background-color:black;\n"
"}")
        self.btn_eat_processing.setCheckable(True)
        self.btn_eat_processing.setChecked(False)
        self.lab_eat_page = QLabel(self.page_eat)
        self.lab_eat_page.setObjectName(u"lab_eat_page")
        self.lab_eat_page.setGeometry(QRect(0, 560, 1024, 16))
        self.lab_eat_page.setFont(font1)
        self.lab_eat_page.setStyleSheet(u"color:#8D8D8D;")
        self.lab_eat_page.setAlignment(Qt.AlignCenter)
        self.lab_eat_page.setIndent(-1)
        self.btn_eat_history = QPushButton(self.page_eat)
        self.btn_eat_history.setObjectName(u"btn_eat_history")
        self.btn_eat_history.setGeometry(QRect(383, 30, 150, 60))
        self.btn_eat_history.setFont(font)
        self.btn_eat_history.setStyleSheet(u"QPushButton{\n"
"border:2px solid #8D8D8D;\n"
"border-radius:29px;\n"
"color:#8D8D8D;\n"
"}\n"
"QPushButton:disabled{\n"
"border:2px solid black;\n"
"color:white;\n"
"background-color:black;\n"
"}")
        self.btn_eat_history.setCheckable(True)
        self.btn_eat_history.setChecked(False)
        self.stacked_main.addWidget(self.page_eat)
        self.page_history = QWidget()
        self.page_history.setObjectName(u"page_history")
        self.history_set_wid = QWidget(self.page_history)
        self.history_set_wid.setObjectName(u"history_set_wid")
        self.history_set_wid.setGeometry(QRect(55, 33, 914, 105))
        self.history_set_wid.setStyleSheet(u"#history_set_wid{border-radius: 25px;\n"
"background: rgba(184, 184, 184, 0.40);}\n"
"QRadioButton::indicator {\n"
"    width: 0px; /* indicator \ud06c\uae30 */\n"
"    height: 0px;\n"
"	border:none;\n"
"}\n"
"QRadioButton {\n"
"spacing: 14.5px; /* \ud14d\uc2a4\ud2b8\uc640 \ub77c\ub514\uc624\ubc84\ud2bc \uac04\uaca9 */\n"
"border-radius: 15px;\n"
"border: 1px solid #8D8D8D;\n"
"background: #F9F9F9;\n"
"color:#909090;\n"
"            }\n"
"\n"
"            /* \ube44\ud65c\uc131\ud654\ub41c \uc0c1\ud0dc */\n"
"QRadioButton::checked {\n"
"background: #1B1B1B;\n"
"color:#F9F9F9;\n"
"\n"
"            }\n"
"QPushButton{\n"
"border-radius: 15px;\n"
"border: 1px solid #8D8D8D;\n"
"text-align : left;\n"
"padding:5px;\n"
"padding-left:10px;\n"
"background: #F9F9F9;\n"
"	image: url(:/main/setting/date_icon.png);\n"
"    image-position: right center;\n"
"image-width: 10px; image-height: 10px;\n"
"color:#909090;\n"
"}\n"
"")
        self.history_day = QRadioButton(self.history_set_wid)
        self.history_day.setObjectName(u"history_day")
        self.history_day.setGeometry(QRect(34, 54, 52, 31))
        font2 = QFont()
        font2.setFamilies([u"Pretendard"])
        font2.setPointSize(12)
        self.history_day.setFont(font2)
        self.history_day.setChecked(True)
        self.history_month = QRadioButton(self.history_set_wid)
        self.history_month.setObjectName(u"history_month")
        self.history_month.setGeometry(QRect(146, 54, 52, 31))
        self.history_month.setFont(font2)
        self.history_week = QRadioButton(self.history_set_wid)
        self.history_week.setObjectName(u"history_week")
        self.history_week.setGeometry(QRect(90, 54, 52, 31))
        self.history_week.setFont(font2)
        self.label = QLabel(self.history_set_wid)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(41, 21, 211, 20))
        font3 = QFont()
        font3.setFamilies([u"Pretendard"])
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: #525252;\n"
"font-family: Pretendard;\n"
"font-size: 20px;\n"
"background-color:none;")
        self.history_range = QPushButton(self.history_set_wid)
        self.history_range.setObjectName(u"history_range")
        self.history_range.setGeometry(QRect(210, 54, 201, 31))
        self.history_clander = QCalendarWidget(self.page_history)
        self.history_clander.setObjectName(u"history_clander")
        self.history_clander.setGeometry(QRect(450, 90, 481, 371))
        self.history_clander.setSelectionMode(QCalendarWidget.SingleSelection)
        self.history_clander.setHorizontalHeaderFormat(QCalendarWidget.SingleLetterDayNames)
        self.history_clander.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.history_main_left = QWidget(self.page_history)
        self.history_main_left.setObjectName(u"history_main_left")
        self.history_main_left.setGeometry(QRect(55, 158, 185, 295))
        self.history_main_left.setStyleSheet(u"#history_main_left{\n"
"border:2px solid rgba(178, 178, 178, 1);\n"
"border-right:none;\n"
"border-top-left-radius: 25px;\n"
"border-bottom-left-radius: 25px;\n"
"background: rgba(184, 184, 184, 0.40);\n"
"}\n"
"Line{\n"
"border:2px solid rgba(141, 141, 141, 0.50);\n"
"\n"
"}\n"
"QLabel{\n"
"color:#525252;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.history_main_left)
        self.verticalLayout_4.setSpacing(8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.label_5 = QLabel(self.history_main_left)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_5.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.history_count_complete = QLabel(self.history_main_left)
        self.history_count_complete.setObjectName(u"history_count_complete")
        sizePolicy2.setHeightForWidth(self.history_count_complete.sizePolicy().hasHeightForWidth())
        self.history_count_complete.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setFamilies([u"Pretendard"])
        font4.setPointSize(16)
        self.history_count_complete.setFont(font4)
        self.history_count_complete.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_5.addWidget(self.history_count_complete, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addLayout(self.verticalLayout_5)

        self.line_4 = QFrame(self.history_main_left)
        self.line_4.setObjectName(u"line_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy3)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_4.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_4.addWidget(self.line_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.label_7 = QLabel(self.history_main_left)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_6.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.history_count_cancel = QLabel(self.history_main_left)
        self.history_count_cancel.setObjectName(u"history_count_cancel")
        sizePolicy2.setHeightForWidth(self.history_count_cancel.sizePolicy().hasHeightForWidth())
        self.history_count_cancel.setSizePolicy(sizePolicy2)
        self.history_count_cancel.setFont(font4)
        self.history_count_cancel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_6.addWidget(self.history_count_cancel, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addLayout(self.verticalLayout_6)

        self.line_3 = QFrame(self.history_main_left)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_3)

        self.label_6 = QLabel(self.history_main_left)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)
        self.label_6.setFont(font)

        self.verticalLayout_4.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 1)
        self.verticalLayout_4.setStretch(3, 1)
        self.verticalLayout_4.setStretch(4, 1)
        self.history_main_right = QWidget(self.page_history)
        self.history_main_right.setObjectName(u"history_main_right")
        self.history_main_right.setGeometry(QRect(238, 158, 732, 295))
        self.history_main_right.setFont(font)
        self.history_main_right.setStyleSheet(u"#history_main_right{\n"
"border:2px solid rgba(178, 178, 178, 1);\n"
"border-left:;\n"
"border-top-right-radius: 25px;\n"
"border-bottom-right-radius: 25px;\n"
"background: rgba(249, 249, 249, 1);\n"
"}\n"
"Line{\n"
"border:2px solid rgba(141, 141, 141, 0.50);\n"
"\n"
"}\n"
"QLabel{\n"
"color:#525252;\n"
"}\n"
"\n"
"QLabel[text='\uc5c6\uc74c']{\n"
"color :rgba(82, 82, 82, 0.5);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.history_main_right)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(25, -1, 25, -1)
        self.history_price_complete = QLabel(self.history_main_right)
        self.history_price_complete.setObjectName(u"history_price_complete")
        self.history_price_complete.setFont(font)

        self.verticalLayout_2.addWidget(self.history_price_complete)

        self.line = QFrame(self.history_main_right)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.history_price_cancel = QLabel(self.history_main_right)
        self.history_price_cancel.setObjectName(u"history_price_cancel")
        self.history_price_cancel.setFont(font)

        self.verticalLayout_2.addWidget(self.history_price_cancel)

        self.line_2 = QFrame(self.history_main_right)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.history_price_non = QLabel(self.history_main_right)
        self.history_price_non.setObjectName(u"history_price_non")
        self.history_price_non.setFont(font)

        self.verticalLayout_2.addWidget(self.history_price_non)

        self.history_total = QWidget(self.page_history)
        self.history_total.setObjectName(u"history_total")
        self.history_total.setGeometry(QRect(55, 480, 914, 80))
        self.history_total.setStyleSheet(u"#history_total{\n"
"border:2px solid rgba(178, 178, 178, 1);\n"
"border-radius: 25px;\n"
"background: rgba(249, 249, 249, 1);\n"
"}\n"
"QPushButton{\n"
"border-radius: 15px;\n"
"border: 1px solid #8D8D8D;\n"
"text-align : right;\n"
"padding:5px;\n"
"padding-right:22px;\n"
"background: #F9F9F9;\n"
"	image: url(:/main/setting/date_icon.png);\n"
"    image-position: left center;\n"
"\n"
"color:rgba(82, 82, 82, 1);\n"
"}\n"
"\n"
"QLabel{\n"
"color:rgba(82, 82, 82, 1);\n"
"}\n"
"")
        self.pushButton_2 = QPushButton(self.history_total)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(34, 20, 160, 40))
        self.pushButton_2.setFont(font4)
        self.history_total_2 = QLabel(self.history_total)
        self.history_total_2.setObjectName(u"history_total_2")
        self.history_total_2.setGeometry(QRect(220, 25, 681, 30))
        self.history_total_2.setFont(font)
        self.stacked_main.addWidget(self.page_history)
        self.page_setting = QWidget()
        self.page_setting.setObjectName(u"page_setting")
        self.setting_sound_bar = QProgressBar(self.page_setting)
        self.setting_sound_bar.setObjectName(u"setting_sound_bar")
        self.setting_sound_bar.setGeometry(QRect(252, 140, 520, 16))
        self.setting_sound_bar.setStyleSheet(u"QProgressBar {\n"
"    border: none;\n"
"    border-radius: 8px;            /* \uc9c4\ud589 \ubc14 \uc804\uccb4\uc758 \ub465\uadfc \ubaa8\uc11c\ub9ac */\n"
"    background-color: rgba(184, 184, 184, 0.8);\n"
"	color:rgba(0,0,0,0);\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #F55442;\n"
"    border-radius: 8px;             /* \uccad\ud06c\uc758 \ub465\uadfc \ubaa8\uc11c\ub9ac */\n"
"        /* \uccad\ud06c \uac04\uc758 \uac04\uaca9 (\uc635\uc158) */\n"
"}\n"
"")
        self.setting_sound_bar.setValue(50)
        self.setting_sound_de = QPushButton(self.page_setting)
        self.setting_sound_de.setObjectName(u"setting_sound_de")
        self.setting_sound_de.setGeometry(QRect(197, 128, 40, 40))
        font5 = QFont()
        font5.setFamilies([u"Pretendard"])
        font5.setPointSize(45)
        font5.setBold(False)
        self.setting_sound_de.setFont(font5)
        self.setting_sound_de.setStyleSheet(u"border-image: url(:/main/setting/miners.png);")
        self.setting_sound_in = QPushButton(self.page_setting)
        self.setting_sound_in.setObjectName(u"setting_sound_in")
        self.setting_sound_in.setGeometry(QRect(787, 128, 40, 40))
        self.setting_sound_in.setFont(font5)
        self.setting_sound_in.setStyleSheet(u"border-image: url(:/main/setting/plus.png);")
        self.label_2 = QLabel(self.page_setting)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(65, 30, 150, 60))
        self.label_2.setStyleSheet(u"border-image: url(:/main/setting/title1.png);")
        self.label_3 = QLabel(self.page_setting)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(65, 260, 150, 60))
        self.label_3.setStyleSheet(u"border-image: url(:/main/setting/title2.png);")
        self.setting_print_drop_1 = QComboBox(self.page_setting)
        self.setting_print_drop_1.addItem("")
        self.setting_print_drop_1.setObjectName(u"setting_print_drop_1")
        self.setting_print_drop_1.setGeometry(QRect(65, 323, 191, 31))
        self.setting_print_drop_1.setFont(font)
        self.setting_print_drop_1.setStyleSheet(u"QComboBox{\n"
"border:none;\n"
"background-color:rgba(0,0,0,0);\n"
"}\n"
"QComboBox::drop-down:button{\n"
"	background-color: rgba(0,0,0,0);\n"
"	width: 18px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	border:0px solid none;    \n"
"	image: url(:/main/setting/dropdown_arrow.png);\n"
"}")
        self.setting_print_test_1 = QPushButton(self.page_setting)
        self.setting_print_test_1.setObjectName(u"setting_print_test_1")
        self.setting_print_test_1.setGeometry(QRect(65, 430, 129, 43))
        self.setting_print_test_1.setStyleSheet(u"border-image: url(:/main/setting/_\ud14c\uc2a4\ud2b8\ucd9c\ub825.png);")
        self.setting_print_name_1 = QLineEdit(self.page_setting)
        self.setting_print_name_1.setObjectName(u"setting_print_name_1")
        self.setting_print_name_1.setGeometry(QRect(65, 357, 341, 56))
        self.setting_print_name_1.setFont(font4)
        self.setting_print_name_1.setFocusPolicy(Qt.ClickFocus)
        self.setting_print_name_1.setStyleSheet(u"QLineEdit{\n"
"border-radius: 15px;\n"
"border: 2px solid rgba(9, 9, 9, 0.45);\n"
"padding-left:20px;\n"
"}\n"
"QLineEdit:focus {\n"
"border-radius: 15px;\n"
"border: 2px solid rgba(9, 9, 9, 0.45);\n"
"outline:0px solid rgba(0,0,0,0);\n"
"}")
        self.setting_print_name_1.setFrame(True)
        self.setting_print_name_1.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.label_4 = QLabel(self.page_setting)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(590, 260, 150, 60))
        self.label_4.setStyleSheet(u"border-image: url(:/main/setting/\uc8fc\ubc29\uc774\ub984.png);")
        self.setting_print_name_2 = QLineEdit(self.page_setting)
        self.setting_print_name_2.setObjectName(u"setting_print_name_2")
        self.setting_print_name_2.setGeometry(QRect(590, 357, 341, 56))
        self.setting_print_name_2.setFont(font4)
        self.setting_print_name_2.setFocusPolicy(Qt.ClickFocus)
        self.setting_print_name_2.setStyleSheet(u"QLineEdit{\n"
"border-radius: 15px;\n"
"border: 2px solid rgba(9, 9, 9, 0.45);\n"
"padding-left:20px;\n"
"}\n"
"QLineEdit:focus {\n"
"border-radius: 15px;\n"
"border: 2px solid rgba(9, 9, 9, 0.45);\n"
"outline:0px solid rgba(0,0,0,0);\n"
"}")
        self.setting_print_name_2.setFrame(True)
        self.setting_print_name_2.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.setting_print_test_2 = QPushButton(self.page_setting)
        self.setting_print_test_2.setObjectName(u"setting_print_test_2")
        self.setting_print_test_2.setGeometry(QRect(590, 430, 129, 43))
        self.setting_print_test_2.setStyleSheet(u"border-image: url(:/main/setting/_\ud14c\uc2a4\ud2b8\ucd9c\ub825.png);")
        self.setting_print_drop_2 = QComboBox(self.page_setting)
        self.setting_print_drop_2.addItem("")
        self.setting_print_drop_2.setObjectName(u"setting_print_drop_2")
        self.setting_print_drop_2.setGeometry(QRect(590, 323, 191, 31))
        self.setting_print_drop_2.setFont(font)
        self.setting_print_drop_2.setStyleSheet(u"QComboBox{\n"
"border:none;\n"
"background-color:rgba(0,0,0,0);\n"
"}\n"
"QComboBox::drop-down:button{\n"
"	background-color: rgba(0,0,0,0);\n"
"	width: 18px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	border:0px solid none;    \n"
"	image: url(:/main/setting/dropdown_arrow.png);\n"
"}")
        self.stacked_main.addWidget(self.page_setting)
        self.main = QWidget(self.centralwidget)
        self.main.setObjectName(u"main")
        self.main.setGeometry(QRect(0, 0, 1024, 161))
        self.store_name = QLabel(self.main)
        self.store_name.setObjectName(u"store_name")
        self.store_name.setGeometry(QRect(50, 50, 241, 41))
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.store_name.sizePolicy().hasHeightForWidth())
        self.store_name.setSizePolicy(sizePolicy5)
        font6 = QFont()
        font6.setFamilies([u"Pretendard"])
        font6.setPointSize(36)
        font6.setBold(True)
        self.store_name.setFont(font6)
        self.store_name.setStyleSheet(u"color:white;")
        self.store_name.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.dragarea = QPushButton(self.main)
        self.dragarea.setObjectName(u"dragarea")
        self.dragarea.setGeometry(QRect(0, 0, 1024, 159))
        self.dragarea.setStyleSheet(u"background-color:#323232;\n"
"border:0px solid #323232;")
        self.btn_minimum = QPushButton(self.main)
        self.btn_minimum.setObjectName(u"btn_minimum")
        self.btn_minimum.setGeometry(QRect(940, 6, 81, 41))
        font7 = QFont()
        font7.setFamilies([u"Pretendard"])
        font7.setPointSize(60)
        self.btn_minimum.setFont(font7)
        self.btn_minimum.setStyleSheet(u"QPushButton{\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-radius:29px;\n"
"color:#8D8D8D;\n"
"}")
        self.btn_minimum.setCheckable(True)
        self.btn_minimum.setChecked(False)
        self.btn_eat = QPushButton(self.main)
        self.btn_eat.setObjectName(u"btn_eat")
        self.btn_eat.setGeometry(QRect(597, 40, 155, 120))
        self.btn_eat.setStyleSheet(u"#btn_eat:disabled{\n"
"border-image: url(:/main/main/\ub9e4\uc7a5\uc2dd\uc0ac_checked.png);\n"
"margin-bottom:0px;\n"
"border:none;\n"
"}\n"
"#btn_eat{\n"
"border-image: url(:/main/main/\ub9e4\uc7a5\uc2dd\uc0ac.png);\n"
"border:none;\n"
"margin-bottom:1px;\n"
"}")
        self.btn_eat.setCheckable(True)
        self.btn_eat.setChecked(False)
        self.btn_soldout = QPushButton(self.main)
        self.btn_soldout.setObjectName(u"btn_soldout")
        self.btn_soldout.setGeometry(QRect(320, 51, 91, 42))
        self.btn_soldout.setStyleSheet(u"border-image: url(:/main/main/\ud488\uc808\uc124\uc815.png);")
        self.store_subname = QLabel(self.main)
        self.store_subname.setObjectName(u"store_subname")
        self.store_subname.setGeometry(QRect(46, 99, 231, 41))
        font8 = QFont()
        font8.setFamilies([u"Pretendard"])
        font8.setPointSize(24)
        font8.setBold(False)
        self.store_subname.setFont(font8)
        self.store_subname.setStyleSheet(u"color:white;")
        self.store_subname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.btn_switch = QPushButton(self.main)
        self.btn_switch.setObjectName(u"btn_switch")
        self.btn_switch.setGeometry(QRect(320, 101, 91, 42))
        self.btn_switch.setStyleSheet(u"#btn_switch::checked{\n"
"border-image: url(:/main/main/toggle_on.png);\n"
"}#btn_switch{\n"
"border-image: url(:/main/main/toggle_off.png);\n"
"}")
        self.btn_switch.setCheckable(True)
        self.btn_switch.setChecked(True)
        self.btn_pickup = QPushButton(self.main)
        self.btn_pickup.setObjectName(u"btn_pickup")
        self.btn_pickup.setEnabled(False)
        self.btn_pickup.setGeometry(QRect(433, 40, 155, 120))
        self.btn_pickup.setStyleSheet(u"#btn_pickup:disabled{\n"
"border-image: url(:/main/main/\ud53d\uc5c5_checked.png);\n"
"margin-bottom:0px;\n"
"\n"
"}\n"
"#btn_pickup{\n"
"border-image: url(:/main/main/\ud53d\uc5c5.png);\n"
"margin-bottom:1px;\n"
"}")
        self.btn_pickup.setCheckable(True)
        self.btn_pickup.setChecked(True)
        self.btn_history = QPushButton(self.main)
        self.btn_history.setObjectName(u"btn_history")
        self.btn_history.setGeometry(QRect(771, 74, 97, 86))
        self.btn_history.setStyleSheet(u"#btn_history:disabled{\n"
"border-image: url(:/main/main/\uae30\ub85d_checked.png);\n"
"border:none;\n"
"margin-bottom:0px;\n"
"}\n"
"#btn_history{\n"
"border-image: url(:/main/main/\uae30\ub85d.png);\n"
"border:none;\n"
"margin-bottom:1px;\n"
"}")
        self.btn_history.setCheckable(True)
        self.btn_history.setChecked(False)
        self.btn_setting = QPushButton(self.main)
        self.btn_setting.setObjectName(u"btn_setting")
        self.btn_setting.setGeometry(QRect(880, 74, 97, 86))
        self.btn_setting.setStyleSheet(u"#btn_setting:disabled{\n"
"border-image: url(:/main/main/\uc124\uc815_checked.png);\n"
"border:none;\n"
"margin-bottom:0px;\n"
"}\n"
"#btn_setting{\n"
"border-image: url(:/main/main/\uc124\uc815.png);\n"
"border:none;\n"
"margin-bottom:1px;\n"
"}")
        self.btn_setting.setCheckable(True)
        self.btn_setting.setChecked(False)
        self.dragarea.raise_()
        self.store_name.raise_()
        self.btn_minimum.raise_()
        self.btn_eat.raise_()
        self.btn_soldout.raise_()
        self.store_subname.raise_()
        self.btn_switch.raise_()
        self.btn_pickup.raise_()
        self.btn_history.raise_()
        self.btn_setting.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.main.raise_()
        self.stacked_main.raise_()

        self.retranslateUi(MainWindow)

        self.stacked_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_pickup_wait.setText(QCoreApplication.translate("MainWindow", u"\uc811\uc218\ub300\uae30", None))
        self.btn_pickup_processing.setText(QCoreApplication.translate("MainWindow", u"\uc81c\uc870 \uc911", None))
        self.btn_pickup_history.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\ub09c \uc8fc\ubb38 \uc870\ud68c", None))
        self.btn_pickup_up.setText("")
        self.btn_pickup_down.setText("")
        self.lab_pickup_page.setText(QCoreApplication.translate("MainWindow", u"1/1", None))
        self.btn_eat_up.setText("")
        self.btn_eat_down.setText("")
        self.btn_eat_wait.setText(QCoreApplication.translate("MainWindow", u"\uc811\uc218\ub300\uae30", None))
        self.btn_eat_processing.setText(QCoreApplication.translate("MainWindow", u"\uc81c\uc870 \uc911", None))
        self.lab_eat_page.setText(QCoreApplication.translate("MainWindow", u"1/1", None))
        self.btn_eat_history.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\ub09c \uc8fc\ubb38 \uc870\ud68c", None))
        self.history_day.setText(QCoreApplication.translate("MainWindow", u"\uc77c\uac04", None))
        self.history_month.setText(QCoreApplication.translate("MainWindow", u"\uc6d4\uac04", None))
        self.history_week.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\uac04", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ub9e4\ucd9c \uc870\ud68c \uae30\uac04 \uc124\uc815", None))
        self.history_range.setText(QCoreApplication.translate("MainWindow", u"2024.01.01 - 2024.06.01", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\uc644\ub8cc \uc8fc\ubb38", None))
        self.history_count_complete.setText(QCoreApplication.translate("MainWindow", u"(15\uac74)      ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\uac70\uc808 / \ucde8\uc18c", None))
        self.history_count_cancel.setText(QCoreApplication.translate("MainWindow", u"(15\uac74)           ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\ubbf8\uc815\uc0b0\uae08", None))
        self.history_price_complete.setText(QCoreApplication.translate("MainWindow", u"\ucd1d \uc8fc\ubb38  \uae08\uc561  213,000\uc6d0", None))
        self.history_price_cancel.setText(QCoreApplication.translate("MainWindow", u"\uc5c6\uc74c", None))
        self.history_price_non.setText(QCoreApplication.translate("MainWindow", u"\uc5c6\uc74c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2024.01.01 ", None))
        self.history_total_2.setText(QCoreApplication.translate("MainWindow", u"\ucd1d \uc8fc\ubb38  \uae08\uc561  213,000\uc6d0", None))
        self.setting_sound_de.setText("")
        self.setting_sound_in.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.setting_print_drop_1.setItemText(0, QCoreApplication.translate("MainWindow", u"\ud504\ub9b0\ud130 \uc774\ub984", None))

        self.setting_print_drop_1.setCurrentText(QCoreApplication.translate("MainWindow", u"\ud504\ub9b0\ud130 \uc774\ub984", None))
        self.setting_print_test_1.setText("")
        self.setting_print_name_1.setInputMask("")
        self.setting_print_name_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\ud504\ub9b0\ud130\uc774\ub984\uc744 \uc785\ub825\ud558\uc138\uc694.", None))
        self.label_4.setText("")
        self.setting_print_name_2.setInputMask("")
        self.setting_print_name_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\ud504\ub9b0\ud130\uc774\ub984\uc744 \uc785\ub825\ud558\uc138\uc694.", None))
        self.setting_print_test_2.setText("")
        self.setting_print_drop_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\ud504\ub9b0\ud130 \uc774\ub984", None))

        self.setting_print_drop_2.setCurrentText(QCoreApplication.translate("MainWindow", u"\ud504\ub9b0\ud130 \uc774\ub984", None))
        self.store_name.setText(QCoreApplication.translate("MainWindow", u"\uc5ec\uae30\ub294 \uac00\uac8c \uc774\ub984\uc774 \ub4e4\uc5b4\uac08 \uacf3", None))
        self.dragarea.setText("")
        self.btn_minimum.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_eat.setText("")
        self.btn_soldout.setText("")
        self.store_subname.setText(QCoreApplication.translate("MainWindow", u"(\uc5ec\uae30\ub294 \uc11c\ube0c \uac00\uac8c\uc774\ub984)", None))
        self.btn_switch.setText("")
        self.btn_pickup.setText("")
        self.btn_history.setText("")
        self.btn_setting.setText("")
    # retranslateUi

