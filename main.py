

from cgitb import reset
from datetime import datetime
import errno
from platform import machine
import shutil
from signal import signal
import sys
import os
from time import sleep
import wmi


from PySide2 import *
from click import progressbar
from qt_material import *
import psutil
import PySide2extn
from user_interface import*


class Worker(QRunnable):
    def __init__(self,fn,*args) :
        super(Worker,self).__init__()

        self.fn=fn
        self.args=args
        
         

        

    @Slot()
    def run(self):
        
            self.fn(*self.args)
       

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        apply_stylesheet(app,theme='dark_cyan.xml')
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        #shadow effect
        self.shadow=QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,92,157,550))
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        #set window icon
        self.setWindowIcon(QtGui.QIcon(u":/icons/airplay.svg"))
        #set window title
        self.setWindowTitle("UTIL Manager")
        QSizeGrip(self.ui.size_grip)
        #minimize window
        self.ui.minimize_window_button.clicked.connect(lambda:self.showMinimized())
        #close window
        self.ui.close_window_button.clicked.connect(lambda:self.close())
        #restore or maximize window
        self.ui.restore_window_button.clicked.connect(lambda:self.restore_or_maximize_window())

        self.ui.pushButton_3.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.cpu_and_memory))
        self.ui.pushButton_4.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.battery))
        self.ui.pushButton_5.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.system_information))
        self.ui.pushButton_6.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.activities))
        self.ui.pushButton_7.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.storage))
        self.ui.pushButton_8.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.sensors))
        self.ui.pushButton_9.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.networks))

        self.ui.header_frame.mouseMoveEvent=self.moveWindow

        self.ui.open_close_side_bar_button.clicked.connect(lambda:self.slideLeftMenu())
        
        #Style clicked menu button
        for w in self.ui.menu_frame.findChildren(QPushButton):
            w.clicked.connect(self.applyButtonStyle)
        #Start Thread
        self.threadpool=QThreadPool()
        self.system_info()
        self.processes()
        self.storage()
        self.sensors()
        self.networks()
        self.show()
        #self.battery()
        #self.cpu_ram()
        self.psutil_thread()
    def psutil_thread(self):
        worker=Worker(self.cpu_ram)

      
        self.threadpool.start(worker)

        battery_worker=Worker(self.battery)

        
        
        self.threadpool.start(battery_worker)

    
    def print_output(self,s):
        print(s)

    def thread_complete(self):
        print("THREAD COMPLETE")

    def progress_fn(self,n):
        print("%d%% done" % n)        

    def cpu_ram(self):
        while True:
            #totalram
            totalRam=1.0
            totalRam=psutil.virtual_memory()[0] *totalRam
            totalRam=totalRam/(1024*1024*1024 )
            self.ui.total_ram.setText("{:.4f}".format(totalRam)+' GB')
            #availableram
            availRam=1.0
            availRam=psutil.virtual_memory()[1] *availRam
            availRam=availRam/(1024*1024*1024)
            self.ui.available_ram.setText("{:.4f}".format(availRam)+' GB')
            #ramused
            ramUsed=1.0
            ramUsed=psutil.virtual_memory()[3] *ramUsed
            ramUsed=ramUsed/(1024*1024*1024)
            self.ui.used_ram.setText("{:.4f}".format(ramUsed)+' GB')
            #ramfree
            ramFree=1.0
            ramFree=psutil.virtual_memory()[4] *ramFree
            ramFree=ramFree/(1024*1024*1024)
            self.ui.free_ram.setText("{:.4f}".format(ramFree)+' GB')
            #ramusage
            ramUsages=str(psutil.virtual_memory()[4] )+ "%"
            self.ui.ram_usage.setText("{:.4f}".format(totalRam)+' GB')

            core=psutil.cpu_count()
            self.ui.cpu_count.setText(str(core))

            cpuPer=psutil.cpu_percent()
            self.ui.cpu_per.setText(str(cpuPer)+" %")

            cpuMainCore=psutil.cpu_count(logical=False)
            self.ui.cpu_main_core.setText(str(cpuMainCore))

            self.ui.cpu_percentage.rpb_setMaximum(100)
            self.ui.cpu_percentage.rpb_setValue(cpuPer)
            self.ui.cpu_percentage.rpb_setBarStyle('Hybrid2') 
            self.ui.cpu_percentage.rpb_setLineColor((255,30,99))   
            self.ui.cpu_percentage.rpb_setPieColor((45,74,83)) 
            self.ui.cpu_percentage.rpb_setTextColor((255,255,255)) 
            self.ui.cpu_percentage.rpb_setInitialPos('West') 
            self.ui.cpu_percentage.rpb_setTextFormat('Percentage') 
            self.ui.cpu_percentage.rpb_setTextFont('Arial') 
            self.ui.cpu_percentage.rpb_setLineWidth(15) 
            self.ui.cpu_percentage.rpb_setPathWidth(15)
            self.ui.cpu_percentage.rpb_setLineCap('RoundCap') 

            self.ui.ram_percentage.spb_setMinimum((0,0,0))

            self.ui.ram_percentage.spb_setMaximum((totalRam,totalRam,totalRam))

            self.ui.ram_percentage.spb_setValue((totalRam,ramUsed,ramFree))

            self.ui.ram_percentage.spb_lineColor(((6,233,38),(6,201,233),(233,6,201)))

            self.ui.ram_percentage.spb_setInitialPos(('West','West','West'))

            self.ui.ram_percentage.spb_lineWidth(15)
            
            self.ui.ram_percentage.spb_setGap(15)

            self.ui.ram_percentage.spb_lineStyle(('SolidLine','SolidLine','SolidLine'))

            self.ui.ram_percentage.spb_lineCap(('RoundCap','RoundCap','RoundCap'))
            
            self.ui.ram_percentage.spb_setPathHidden(True)
            #sleep
            sleep(1)
    def secs2hours(self,secs):
        mm,ss=divmod(secs,60)    
        hh,mm=divmod(mm,60)
        return "%d:%02d:%02d (H:M:S)" % (hh,mm,ss)
    def battery(self):
        while True:
            batt=psutil.sensors_battery()
            
            if batt is None:
                self.ui.battery_status.setText("No battery installed")
            if batt.power_plugged:
                self.ui.battery_charge.setText(str(round(batt.percent,2))+"%")  
                self.ui.battery_time_left.setText("N/A")
                if batt.percent<100:
                    self.ui.battery_status.setText("Charging")
                else:
                    self.ui.battery_status.setText("Fully Charged")    
                self.ui.battery_plugged.setText("Yes")  
            else:
                self.ui.battery_charge.setText(str(round(batt.percent,2))+"%")  
                self.ui.battery_time_left.setText(self.secs2hours(batt.secsleft))  
                if batt.percent<100:
                    self.ui.battery_status.setText("Discharging")
                else:
                    self.ui.battery_status.setText("Fully Charged")    
                self.ui.battery_plugged.setText("No") 
            self.ui.battery_usage.rpb_setMaximum(100)
            self.ui.battery_usage.rpb_setValue(batt.percent)
            self.ui.battery_usage.rpb_setBarStyle('Hybrid2') 
            self.ui.battery_usage.rpb_setLineColor((255,30,99))   
            self.ui.battery_usage.rpb_setPieColor((45,74,83)) 
            self.ui.battery_usage.rpb_setTextColor((255,255,255)) 
            self.ui.battery_usage.rpb_setInitialPos('West') 
            self.ui.battery_usage.rpb_setTextFormat('Percentage') 
            self.ui.battery_usage.rpb_setLineWidth(15) 
            self.ui.battery_usage.rpb_setPathWidth(15)
            self.ui.battery_usage.rpb_setLineCap('RoundCap')
            #sleep
            sleep(1)
    def applyButtonStyle(self):
        for w in self.ui.menu_frame.findChildren(QPushButton):
            if w.objectName()!=self.sender().objectName():
                w.setStyleSheet("border-bottom: none;")
        self.sender().setStyleSheet("border-bottom: 2px solid")
    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            #change icon
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/window-restore-solid.svg"))
        else:
            self.showMaximized()
            #change icon
               
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/cil-window-maximize.svg"))

    def mousePressEvent(self,event):
        self.ClickPosition=event.globalPos()
        
    def moveWindow(e,self):

        if self.isMaximized() == False:


            if e.buttons()==Qt.LeftButton:
                self.move(self.pos()+e.globalPos()-self.clickPosition)
                self.clickPosition=e.globalPos()
                e.accept()

    def slideLeftMenu(self):
        width=self.ui.left_menu_cont_frame.width()
        if(width==40):
            newWidth=200
        else:
            newWidth=40
        self.animation=QPropertyAnimation(self.ui.left_menu_cont_frame,b"minimumWidth")    
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def system_info(self):
        time=datetime.now().strftime('%I:%M:%S %p')
        self.ui.system_time.setText(str(time))
        date=datetime.now().strftime('%Y-%m-%d')
        self.ui.system_date.setText(str(date))

        self.ui.machine.setText(platform.machine())
        self.ui.version.setText(platform.version())
        self.ui.processor.setText(platform.processor())
        self.ui.platform.setText(platform.platform())
        self.ui.system.setText(platform.system())
    
    def processes(self):
        for x in psutil.pids():
            rowPosition=self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)

            try:
                process=psutil.Process(x)
                self.create_table_widget(rowPosition,0,str(process.pid),"tableWidget")
                self.create_table_widget(rowPosition,1,str(process.name()),"tableWidget")
                self.create_table_widget(rowPosition,2,str(process.status()),"tableWidget")
                self.create_table_widget(rowPosition,3,str(datetime.utcfromtimestamp(process.create_time()).strftime('%Y-%m-%d %H:%M:%S')),"tableWidget")

                suspend_btn=QPushButton(self.ui.tableWidget)
                suspend_btn.setText('Suspend')
                suspend_btn.setStyleSheet("color: brown")
                self.ui.tableWidget.setCellWidget(rowPosition,4,suspend_btn)
                resume_btn=QPushButton(self.ui.tableWidget)
                resume_btn.setText('Resume')
                resume_btn.setStyleSheet("color: green")
                self.ui.tableWidget.setCellWidget(rowPosition,5,resume_btn)
                terminate_btn=QPushButton(self.ui.tableWidget)
                terminate_btn.setText('Terminate')
                terminate_btn.setStyleSheet("color: Orange")
                self.ui.tableWidget.setCellWidget(rowPosition,6,terminate_btn)
                kill_btn=QPushButton(self.ui.tableWidget)
                kill_btn.setText('Kill')
                kill_btn.setStyleSheet("color: red")
                self.ui.tableWidget.setCellWidget(rowPosition,7,kill_btn)
            except Exception as e:
                print(e)    
            self.ui.activity_search.textChanged.connect(self.findName)  

    def findName(self):
        name=self.ui.activity_search.text().lower()
        for row in range(self.ui.tableWidget.rowCount()):
            item=self.ui.tableWidget.item(row,1)
            self.ui.tableWidget.setRowHidden(row,name not in item.text().lower())
    def create_table_widget(self,row,column,text,tablename):
        qtablewidgetitem=QTableWidgetItem()

        getattr(self.ui,tablename).setItem(row,column,qtablewidgetitem)
        qtablewidgetitem= getattr(self.ui,tablename).item(row,column)
        qtablewidgetitem.setText(text)
    def storage(self):
        storage_device=psutil.disk_partitions(all=False)
        z=0
        for x in storage_device:
            rowPosition=self.ui.storageTable.rowCount()
            self.ui.storageTable.insertRow(rowPosition)
            self.create_table_widget(rowPosition,0,x.device,"storageTable")
            self.create_table_widget(rowPosition,1,x.mountpoint,"storageTable")
            self.create_table_widget(rowPosition,2,x.opts,"storageTable")
            if(sys.platform=="linux"):
                self.create_table_widget(rowPosition,3,str(x.maxfile),"storageTable")
                self.create_table_widget(rowPosition,4,str(x.maxpath),"storageTable")
            else:
                self.create_table_widget(rowPosition,3,"Function Not Available on this platform","storageTable")
                self.create_table_widget(rowPosition,4,"Function Not Available on this platform","storageTable")  
            disk_usage=shutil.disk_usage(x.mountpoint)
            
            self.create_table_widget(rowPosition,5,str((disk_usage.total/(1024*1024*1024)))+" GB","storageTable")
            self.create_table_widget(rowPosition,7,str((disk_usage.free/(1024*1024*1024)))+" GB","storageTable")
            self.create_table_widget(rowPosition,6,str((disk_usage.used/(1024*1024*1024)))+" GB","storageTable")
            full_disk=(disk_usage.used/disk_usage.total)*100
            progressbar=QProgressBar(self.ui.storageTable)
            progressbar.setObjectName(u"progressBar")
            progressbar.setValue(full_disk)
            self.ui.storageTable.setCellWidget(rowPosition, 8, progressbar)
    def sensors(self):
        w = wmi.WMI(namespace="root\OpenHardwareMonitor")
        temperature_infos = w.Sensor()
        for x in temperature_infos:
            
                
            rowPosition=self.ui.sensors_table.rowCount()
            self.ui.sensors_table.insertRow(rowPosition)
            self.create_table_widget(rowPosition,0,str(x.Name),"sensors_table")
            self.create_table_widget(rowPosition,2,str(x.value),"sensors_table")
            ##self.create_table_widget(rowPosition,2,x.opts,"sensors_table")                
    def networks(self):
        for x in psutil.net_if_stats():
            z=psutil.net_if_stats()

            rowPosition=self.ui.net_stats_table.rowCount()
            self.ui.net_stats_table.insertRow(rowPosition)     

            self.create_table_widget(rowPosition,0,x,"net_stats_table")
            self.create_table_widget(rowPosition,1,str(z[x].isup),"net_stats_table")   
            self.create_table_widget(rowPosition,2,str(z[x].duplex),"net_stats_table")
            self.create_table_widget(rowPosition,3,str(z[x].speed),"net_stats_table") 
            self.create_table_widget(rowPosition,4,str(z[x].mtu),"net_stats_table") 
        for x in psutil.net_io_counters(pernic=True):
            z=psutil.net_io_counters(pernic=True)

            rowPosition=self.ui.net_iocounter_table.rowCount()
            self.ui.net_iocounter_table.insertRow(rowPosition)     

            self.create_table_widget(rowPosition,0,x,"net_iocounter_table")
            self.create_table_widget(rowPosition,1,str(z[x].bytes_sent),"net_iocounter_table")   
            self.create_table_widget(rowPosition,2,str(z[x].bytes_recv),"net_iocounter_table")
            self.create_table_widget(rowPosition,3,str(z[x].packets_sent),"net_iocounter_table") 
            self.create_table_widget(rowPosition,4,str(z[x].packets_recv),"net_iocounter_table")    
            self.create_table_widget(rowPosition,5,str(z[x].errin),"net_iocounter_table") 
            self.create_table_widget(rowPosition,6,str(z[x].errout),"net_iocounter_table")   
            self.create_table_widget(rowPosition,7,str(z[x].dropin),"net_iocounter_table")   
            self.create_table_widget(rowPosition,8,str(z[x].dropout),"net_iocounter_table") 
        for x in psutil.net_if_addrs():
            z=psutil.net_if_addrs()
  
            for y in z[x]:
                
                rowPosition=self.ui.net_addresses_table.rowCount()
                self.ui.net_addresses_table.insertRow(rowPosition)   
                self.create_table_widget(rowPosition,0,x,"net_addresses_table")
                self.create_table_widget(rowPosition,1,str(y.family),"net_addresses_table")   
                self.create_table_widget(rowPosition,2,str(y.address),"net_addresses_table")
                self.create_table_widget(rowPosition,3,str(y.netmask),"net_addresses_table") 
                self.create_table_widget(rowPosition,4,str(y.broadcast),"net_addresses_table")    
                self.create_table_widget(rowPosition,5,str(y.ptp),"net_addresses_table") 
        for x in psutil.net_connections():
            z=psutil.net_connections()

            rowPosition=self.ui.net_connections_table.rowCount()
            self.ui.net_connections_table.insertRow(rowPosition)     

           
            self.create_table_widget(rowPosition,0,str(x.fd),"net_connections_table")   
            self.create_table_widget(rowPosition,1,str(x.family),"net_connections_table")
            self.create_table_widget(rowPosition,2,str(x.type),"net_connections_table") 
            self.create_table_widget(rowPosition,3,str(x.laddr),"net_connections_table")    
            self.create_table_widget(rowPosition,4,str(x.raddr),"net_connections_table") 
            self.create_table_widget(rowPosition,5,str(x.status),"net_connections_table")   
            self.create_table_widget(rowPosition,6,str(x.pid),"net_connections_table")   
                 
                       



if __name__=="__main__":
    
    app=QApplication(sys.argv)
    window=MainWindow()
    sys.exit(app.exec_())
    