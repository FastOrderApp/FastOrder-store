from data.libs import *
from data.ui.main import Ui_MainWindow
from data.ui.order_unit import Ui_unit
import images_rc
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        # 초기설정
        super().__init__()
        self.setupUi(self)
        # frameless window
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.lay_pickup_order.setAlignment(Qt.AlignTop)
        self.lay_eat_order.setAlignment(Qt.AlignTop)
        # 미니멈 버튼
        self.btn_minimum.clicked.connect(self.showMinimized)
        self.dragarea.mousePressEvent = self.start_drag
        self.dragarea.mouseMoveEvent = self.drag_window
        self.store_name.mousePressEvent = self.start_drag
        self.store_name.mouseMoveEvent = self.drag_window
        self.store_subname.mousePressEvent = self.start_drag
        self.store_subname.mouseMoveEvent = self.drag_window
        # 버튼들 정의
        self.main_btns = [self.btn_pickup,self.btn_eat,self.btn_setting,self.btn_history]
        self.pickup_btns = [self.btn_pickup_wait,self.btn_pickup_processing,self.btn_pickup_history]
        self.eat_btns = [self.btn_eat_wait,self.btn_eat_processing,self.btn_eat_history]
        # 상태정의
        self.state = {"state":True,"title":"pickup","pickup":{"order_type":"wait"},"eat":{"order_type":"wait"}}
        # unit 정의
        self.units = {"pickup":[OrderUnit(self,"pickup") for _ in range(3)],"eat":[OrderUnit(self,"eat") for _ in range(3)]}
        # orders unit 추가
        for unit in self.units["pickup"]+self.units["eat"]:getattr(self,f"lay_{unit.type}_order").addWidget(unit)

        # 메인화면 버튼 클릭 이벤트
        self.btn_switch.clicked.connect(lambda state = self.btn_switch.isChecked():self.state.update({"state":state}))
        for btn in self.main_btns+self.pickup_btns+self.eat_btns:btn.clicked.connect(lambda state, btn=btn: self.change_title(btn))
        # self.stacked_main.currentChanged.connect(lambda index: self.update_order())
            
        # 버튼 클릭 이벤트
        for button in self.findChildren(QPushButton):button.clicked.connect(lambda state, button=button: print(f"Button '{button.objectName()}' clicked"))
        self.history_clander.hide()
        # 기록 날짜 선택
        self.history_day_group = QButtonGroup(self)
        self.history_day_group.addButton(self.history_day)
        self.history_day_group.addButton(self.history_week)
        self.history_day_group.addButton(self.history_month)
        self.history_day_group.buttonClicked.connect(lambda button: self.update_history())
        # 기록화면 show 이벤트
        self.page_history.showEvent = lambda event: self.update_history()
        self.setting_sound_de.clicked.connect(lambda: self.setting_sound_bar.setValue(self.setting_sound_bar.value()-10 if self.setting_sound_bar.value() > 0 else 0))
        self.setting_sound_in.clicked.connect(lambda: self.setting_sound_bar.setValue(self.setting_sound_bar.value()+10 if self.setting_sound_bar.value() < 100 else 100))
        self.update_init()
        self.update_order()
        self.update_history()
        

    def start_drag(self, event):
        # 마우스 버튼이 눌릴 때 드래그 시작 위치를 계산
        if event.button() == Qt.LeftButton:
            self.dragging = True
            # 마우스 클릭 위치와 창의 왼쪽 상단 사이의 차이 계산
            self.start_pos = event.globalPosition().toPoint() - self.pos()

    def drag_window(self, event):
        # 드래그 상태일 때 창 위치 이동
        if self.dragging and event.buttons() == Qt.LeftButton:
            # 마우스의 현재 위치에서 시작 위치를 빼서 새 위치 계산
            new_pos = event.globalPosition().toPoint() - self.start_pos
            self.move(new_pos)

    def mouseReleaseEvent(self, event):
        # 마우스가 떼어지면 드래그 상태를 종료
        if event.button() == Qt.LeftButton:
            self.dragging = False
        

    def update_init(self):
        data = {"store_name":"백소정","store_subname":"안산 한양대점","store_address":"주소","store_tel":"전화번호","store_img":"images/store.png"}
        self.store_name.setText(data["store_name"])
        self.store_subname.setText(f"({data['store_subname']})")
        

    def update_order(self):
        if self.state["title"] in ['setting','history']:return
        if self.state["title"] == "pickup":
            data = {'page':1,"total_page":2,"order_count":3,'total_order_count':5,"orders":[
                    {"menu_detail":"내가 배고파","user_requirement":"밥주세요","order_state":"완료",'order_time':'10:10','menu_count':1,'price':10000,'main_menu': '김치볶음밥',"order_id":1,"user_name":"김도훈"},
                    {"menu_detail":"짬뽕 곱배기","user_requirement":"젓가락 주세요","order_state":"대기",'order_time':'10:10','menu_count':1,'price':10000,'main_menu': '김치볶음밥',"order_id":2,"user_name":"김도훈"},
                    {"menu_detail":"치킨라이스","user_requirement":"일회용품 알잘딱","order_state":"완료",'order_time':'10:10','menu_count':1,'price':10000,'main_menu': '김치볶음밥',"order_id":3,"user_name":"김도훈"},]}
        else:
            data = {'page':1,"total_page":1,"order_count":2,'total_order_count':2,"orders":[
                    {"menu_detail":"사탕수수","user_requirement":"요청사항","order_state":"완료",'order_time':'10:10','menu_count':1,'price':10000,'main_menu': '김치볶음밥',"order_id":4,"user_name":"김도훈"},
                    # {"menu_detail":"던킨도넛","user_requirement":"요청사항","order_state":"대기",'order_time':'10:10','menu_count':1,'price':10000,'main_menu': '김치볶음밥',"order_id":5,"user_name":"김도훈"},
                    {"menu_detail":"아이스 아메리카노","user_requirement":"요청사항","order_state":"대기",'order_time':'10:10','menu_count':1,'price':10000,'main_menu': '김치볶음밥',"order_id":6,"user_name":"김도훈"},]}
        print(f"state\n{self.state}\ndata\n{data}")
        getattr(self,f"lab_{self.state['title']}_page").setText(f"{data['page']} / {data['total_page']}")
        # for unit,order in zip(self.units[self.state['title']],data["orders"]):
        for index,unit in enumerate(self.units[self.state['title']]):
            unit.update(data["orders"][index] if index < len(data["orders"]) else {})
        # for i in range(3,data["order_count"],-1):
        #     unit[self.state['title']][i].hide()
        getattr(self,f"{self.state['title']}_orders").setEnabled(data["total_order_count"] != 0)
        getattr(self,f"btn_{self.state['title']}_up").setEnabled(data["page"] != 1)
        getattr(self,f"btn_{self.state['title']}_down").setEnabled(data["page"] != data["total_page"])
    def change_title(self,btn):
        splited_obj = btn.objectName().split("_")
        match len(splited_obj):
            case 3:     ### order
                self.state[splited_obj[1]]["order_type"] = splited_obj[2]
                btns = getattr(self,splited_obj[1]+"_btns")
                self.update_order()
                
            case 2:     ### 타이틀
                self.state["title"] = splited_obj[1]
                self.stacked_main.setCurrentWidget(getattr(self,btn.objectName().replace("btn","page")))    
                btns = self.main_btns
                self.update_order()
                
        btns = btns.copy()
        btns.remove(btn)
        for b in btns:
            b.setEnabled(True)
        btn.setEnabled(False)
    
    def update_history(self):
        if self.history_day.isChecked():daterange = 0
        elif self.history_week.isChecked():daterange = 6
        elif self.history_month.isChecked():daterange = 29
        date = datetime.datetime.today().strftime("%Y.%m.%d")+" - "+(datetime.datetime.today()+datetime.timedelta(days=-daterange)).strftime("%Y.%m.%d")
        params = {'daterange':date,}
        data = {"count_complete":4,"count_cancel":1,"price_complete":100000,"price_cancel":10000}
        self.history_range.setText(date)
        self.history_count_complete.setText(f"({data['count_complete']}건)          ")
        self.history_count_cancel.setText(f"({data['count_cancel']}건)            ")
        self.history_price_complete.setText(f"총 주문 금액 {data['price_complete']:,}원")
        self.history_price_cancel.setText(f"총 취소 금액 {data['price_cancel']:,}원")
        # self.history_clander.show()

class OrderUnit(QWidget,Ui_unit):
    def __init__(self,parent,type):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.type = type
        self.order_id = 0
        self.order_state.clicked.connect(self.complete_order)

    def complete_order(self):
        # api.post("complete_order",{"order_id":self.order_id})
        print(f"order_id {self.order_id} is completed")
    def update(self,order):
        if order == {}:
            self.hide()
        else:
            self.order_id = order["order_id"]
            self.user_name.setText(order["user_name"]+" 님")
            self.user_time.setText(order["order_time"] + " 주문")
            self.menu_count_price.setText(f"메뉴 {order['menu_count']}개 • 총 {order['price']:,}원")
            self.menu_detail.setText(f"{order["menu_detail"]} 외 {order['menu_count']-1}개" if order['menu_count'] > 1 else order["main_menu"])
            self.user_requirement.setText(order["user_requirement"])
            # self.order_state.setText(order["order_state"])
            if order["order_state"] == "완료":
                self.order_state.setEnabled(False)

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())