import requests,os
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidget,QMessageBox 

class http:
    def __init__(self):
    # 从文件中加载UI定义
        qfile_stats=QFile(r"E:\py_TEST\py_ui\request.ui")
        print('url',qfile_stats.fileName())
        print(os.path.exists(qfile_stats.fileName()))
        qfile_stats.open(QFile.ReadOnly)
       
        qfile_stats.close()
        print('1111')
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load(qfile_stats)
        print('2')
        #消息头加事件
        self.ui.pushButton_add.clicked.connect(self.addHeader)
        print('3')
        #消息头减事件
        self.ui.pushButton_delete.clicked.connect(self.removeHeader)
        print(4)
        #发送请求事件
        self.ui.pushButton.clicked.connect(self.request)
        print('6')
    def addHeader(self):
        ##在表格末尾新增一行"""
        
        row_count = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_count)  # 在表格末尾插入一行


        
    def removeHeader(self):
        """删除当前选中的行"""
        
        current_row = self.ui.tableWidget.currentRow()
        if current_row == -1:
            QMessageBox.warning(self.ui, "提示", "请先选中一行！")  # 如果未选中行，则弹出提示
        else:
            self.ui.tableWidget.removeRow(current_row)
    def request(self):
        url地址=self.ui.lineEdit.text()#https://accounts.douban.com/login
        请求方式=self.ui.comboBox.currentText()
        c={'GET':requests.get,'POST':requests.post,'PUT':requests.put,'DELETE':requests.delete}
        chose=c[请求方式]
        print('请求方式:'+请求方式,chose)
        ##请求行=请求方式+' '+url地址        
        #######################请求头
        table_widget=self.ui.tableWidget
        #headers = [table_widget.horizontalHeaderItem(i).text() for i in range(table_widget.columnCount())]   
        #print(headers)
        table_data = []  # 用于存储所有行的数据
        
        # 获取表格行数和列数
        row_count = table_widget.rowCount()
        column_count = table_widget.columnCount()
        
        #遍历每一行
        for row in range(row_count):
            if row_count==0:
                table_data={}
                break
            else:
                row_data = {}
                
                # 获取单元格内容
                item = table_widget.item(row, 0)
                m=item.text()#名称非空
                item = table_widget.item(row, 1)
                n=item.text() if item else ""
                row_data[m] = n  
                table_data=row_data
        print('消息头参数')   
        print(table_data)
        #######################
        消息头=table_data#dict__________查函数
        消息体={}
        p=self.ui.plainTextEdit_body.toPlainText()
        if p=='':
            pass
        else:
            p.split('&')
           
            for item in p:
               key,value=p.split('=')
               消息体[key]=value
               print( '消息体',消息体) 
        #data,json
        #请求消息=请求行+'\n'+消息头+'\n'+消息体
        print('11')
        #response = requests.get(url=url地址,headers=消息头,params=消息体)
        
        response = chose(url=url地址,headers=消息头,params=消息体)
        print(response.text,response.status_code)
        #####结果
        self.ui.plainTextEdit_result.toPlainText=response.text
app = QApplication([])
stats = http()
stats.ui.show()
app.exec_()
