import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDial, QDialog, QApplication, QGridLayout, QLabel, QMessageBox, QPushButton, QScrollArea, QSizePolicy, QVBoxLayout, QWidget
from PyQt5.uic import loadUi
from collections import defaultdict
from datetime import datetime, timedelta


class Cocina(QDialog):
    def __init__(self, widget, db):
        super(Cocina, self).__init__()
        self.original_widget = widget
        self.db = db
        dir_a = os.path.dirname(os.path.abspath(__file__))
        ui_a = os.path.join(dir_a, "u_cocina.ui")
        loadUi(ui_a, self)

        self.scroll_area = self.findChild(QScrollArea, 'scroll_area')
        self.scroll_area.setWidgetResizable(True)

        self.content_widget = self.scroll_area.findChild(QWidget, 'scrollAreaWidgetContents')
        self.grid_layout = self.widget_order.findChild(QGridLayout, 'layout_content')

        self.grid_layout = QGridLayout(self.content_widget) #EL ERROR SE CORRIGE CUANDO DEFINIMOS EL GRID Y EL SCROLL AREA CON EL CONTENT WIDGET NUEVAMENMTE, PROBLEMAS DEL DESIGNR
        self.scroll_area.setWidget(self.content_widget)

        self.b_buscar_pedidos.clicked.connect(self.llamar_db)
        self.b_salir_1.clicked.connect(self.salir)
        
    def add_order(self, result):
        orders_by_table = defaultdict(list)
        for row in result:
            order_id, mesa_id, order_time, product_name, quantity, status = row
            orders_by_table[mesa_id].append((product_name, quantity, status, order_id))

            hour_dif = -5
            server_dt_object = datetime.strptime(order_time, '%Y-%m-%d %H:%M:%S')
            local_dt_object = server_dt_object + timedelta(hours=hour_dif)
            local_order_time_display = local_dt_object.strftime('%Y-%m-%d %H:%M:%S')


            while self.grid_layout.count():
                child = self.grid_layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        for mesa_id, orders in orders_by_table.items():
            order_card = QWidget()
            order_card.setStyleSheet("background-color: #f5f5f5; border-radius: 10px; padding: 15px; margin: 10px;")
            order_card.setMinimumSize(200, 350)
        
            card_layout = QVBoxLayout(order_card)

            table_details = QLabel(f"Mesa {mesa_id}\n"
                                   f"Fecha/Hora {local_order_time_display}\n"
                                   f"Estatus: {status}")
            table_details.setStyleSheet("font-weight:Segoe UI; color: #333333; font-size: 14px")
            card_layout.addWidget(table_details)
        
            product_summary = QLabel()
            total_products = sum(item[1] for item in orders)
            product_details = f"Total productos: {total_products}\n \n"
        
            for product_name, quantity, status, _ in orders:
                product_details += f"{product_name} x{quantity}\n"
        
            product_summary.setText(product_details)
            product_summary.setStyleSheet("font-weight:Segoe UI; color: #333333; font-size: 14px")
            card_layout.addWidget(product_summary)
        
            complete_btn = QPushButton("✓ Completar Pedido")
            complete_btn.clicked.connect(lambda: self.completar(order_id))
            card_layout.addWidget(complete_btn)
        
            row_pos = (self.grid_layout.count() // 3)
            col_pos = self.grid_layout.count() % 3
            self.grid_layout.addWidget(order_card, row_pos, col_pos)
        
    def llamar_db(self):
        self.db.dbcursor.execute("""SELECT 
                                        Users.orders.order_id,
                                        Users.orders.mesa_id,
                                        DATE_FORMAT(Users.orders.order_time, '%Y-%m-%d %H:%i:%S') AS formatted_time,
                                        Users.products.name AS product_name,
                                        Users.order_items.quantity,
                                        Users.orders.status
                                    FROM Users.orders
                                    JOIN Users.order_items ON Users.orders.order_id = Users.order_items.order_id
                                    JOIN Users.products ON Users.order_items.product_id = Users.products.product_id
                                    WHERE Users.orders.status = 'pendiente'
                                    ORDER BY Users.orders.order_time DESC;""")
        result = self.db.dbcursor.fetchall()
        self.add_order(result)

    def completar(self, order_id):
        self.db.dbcursor.execute("UPDATE Users.orders SET status = 'completado' WHERE order_id = %s", (order_id,))
        self.db.db.commit()
        self.llamar_db()

############################################################################################# Area de test
    def salir(self):
        from Ui.Login.a_login import Login
        mainwindow = Login(self.original_widget, self.db)
        self.original_widget.addWidget(mainwindow)
        self.original_widget.setFixedWidth(1091)
        self.original_widget.setFixedHeight(501)
        self.original_widget.setCurrentIndex(self.original_widget.currentIndex()+1)


def a4(db, widget):
    cocina_w = Cocina(widget,db)
    widget.addWidget(cocina_w)
    widget.setFixedWidth(1091)
    widget.setFixedHeight(501)
    widget.setCurrentIndex(widget.currentIndex() + 1)