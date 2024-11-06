from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QSpacerItem, QPushButton, QVBoxLayout, QWidget, QScrollArea,QButtonGroup
from PySide6.QtCore import Qt, QTimer, QRect, QEvent, QPoint, QThread, Signal, QFile, QUrl
from PySide6.QtGui import QFont, QFontDatabase, QMouseEvent, QCursor, QPixmap
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings
import math, datetime, requests, json, os, time, threading, base64, sys
import base64
from PySide6.QtWidgets import QApplication, QListWidget, QListWidgetItem, QFrame, QVBoxLayout, QWidget, QSizePolicy, QLabel
from PySide6.QtCore import Qt, QSize, Signal, Slot
from PySide6.QtGui import QResizeEvent
from data.decorate import *
import data.restApi as api
import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget


@decorate_log
def uic_all_file():
    current_file_directory = os.path.dirname(os.path.abspath(__file__))
    print(current_file_directory)
    # 상위 디렉토리로 이동하여 'ui' 폴더 경로 설정
    ui_directory = os.path.join(current_file_directory,  "ui")
    print(ui_directory)
    # 경로를 sys.path에 추가하여 임포트 가능하게 설정

    sys.path.append(ui_directory)

    # 'ui' 폴더 안의 모든 .py 파일에서 클래스 임포트
    for filename in os.listdir(ui_directory):
        if filename.endswith(".ui"):
            modification_time_ui = os.path.getmtime(os.path.join(ui_directory,filename))
            # py 파일이 있는지 체크
            if os.path.exists(os.path.join(ui_directory,filename[:-2]+'py')):            
                modification_time_py = os.path.getmtime(os.path.join(ui_directory,filename[:-2]+'py'))
                if modification_time_ui < modification_time_py:
                    continue
            print(filename )
            os.system(f"pyside6-uic {os.path.join(ui_directory,filename)} -o {os.path.join(ui_directory,filename[:-2]+'py')}")


uic_all_file()