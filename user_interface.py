# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar
from PySide2extn.SpiralProgressBar import spiralProgressBar

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(824, 600)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy)
        self.header_frame.setStyleSheet(u"background-color: rgb(28, 71, 117);")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_left_frame = QFrame(self.header_frame)
        self.header_left_frame.setObjectName(u"header_left_frame")
        self.header_left_frame.setStyleSheet(u"padding:0;\n"
"margin:0;")
        self.header_left_frame.setFrameShape(QFrame.StyledPanel)
        self.header_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_left_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.open_close_side_bar_button = QPushButton(self.header_left_frame)
        self.open_close_side_bar_button.setObjectName(u"open_close_side_bar_button")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.open_close_side_bar_button.setFont(font)
        self.open_close_side_bar_button.setStyleSheet(u"margin:0;")
        icon = QIcon()
        icon.addFile(u":/icons/align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar_button.setIcon(icon)
        self.open_close_side_bar_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.open_close_side_bar_button, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.header_left_frame)

        self.header_center_frame = QFrame(self.header_frame)
        self.header_center_frame.setObjectName(u"header_center_frame")
        self.header_center_frame.setStyleSheet(u"")
        self.header_center_frame.setFrameShape(QFrame.StyledPanel)
        self.header_center_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_center_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.header_center_frame)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.label_2.setPixmap(QPixmap(u":/icons/airplay.svg"))

        self.horizontalLayout_3.addWidget(self.label_2, 0, Qt.AlignRight)

        self.label = QLabel(self.header_center_frame)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.header_center_frame)

        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        self.header_right_frame.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.header_right_frame)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.header_right_frame)
        self.restore_window_button.setObjectName(u"restore_window_button")
        icon2 = QIcon()
        icon2.addFile(u":/icons/window-restore-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon2)
        self.restore_window_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.header_right_frame)
        self.close_window_button.setObjectName(u"close_window_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon3)
        self.close_window_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.close_window_button)


        self.horizontalLayout.addWidget(self.header_right_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy1)
        self.main_body_frame.setMinimumSize(QSize(0, 0))
        self.main_body_frame.setMaximumSize(QSize(16777215, 16777215))
        self.main_body_frame.setFrameShape(QFrame.NoFrame)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.left_menu_cont_frame = QFrame(self.main_body_frame)
        self.left_menu_cont_frame.setObjectName(u"left_menu_cont_frame")
        self.left_menu_cont_frame.setMinimumSize(QSize(40, 0))
        self.left_menu_cont_frame.setMaximumSize(QSize(20, 16777215))
        self.left_menu_cont_frame.setStyleSheet(u"background-color: rgb(28, 71, 117);\n"
"")
        self.left_menu_cont_frame.setFrameShape(QFrame.StyledPanel)
        self.left_menu_cont_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.left_menu_cont_frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.left_menu_cont_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(100, 0))
        self.menu_frame.setMaximumSize(QSize(16777215, 16777215))
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.menu_frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_7 = QPushButton(self.menu_frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(36, 36))
        self.pushButton_7.setMaximumSize(QSize(36, 36))
        self.pushButton_7.setStyleSheet(u"padding:0;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/disc.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon4)
        self.pushButton_7.setIconSize(QSize(32, 32))

        self.gridLayout_2.addWidget(self.pushButton_7, 4, 0, 1, 1, Qt.AlignLeft)

        self.pushButton_6 = QPushButton(self.menu_frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(36, 36))
        self.pushButton_6.setMaximumSize(QSize(36, 36))
        self.pushButton_6.setStyleSheet(u"padding:0;")
        icon5 = QIcon()
        icon5.addFile(u":/icons/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QSize(32, 32))

        self.gridLayout_2.addWidget(self.pushButton_6, 3, 0, 1, 1, Qt.AlignLeft)

        self.pushButton_5 = QPushButton(self.menu_frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(36, 36))
        self.pushButton_5.setMaximumSize(QSize(36, 36))
        self.pushButton_5.setStyleSheet(u"padding:0;")
        icon6 = QIcon()
        icon6.addFile(u":/icons/monitor.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon6)
        self.pushButton_5.setIconSize(QSize(32, 32))

        self.gridLayout_2.addWidget(self.pushButton_5, 2, 0, 1, 1, Qt.AlignLeft)

        self.label_4 = QLabel(self.menu_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMargin(5)

        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1, Qt.AlignLeft)

        self.pushButton_8 = QPushButton(self.menu_frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(36, 36))
        self.pushButton_8.setMaximumSize(QSize(36, 36))
        self.pushButton_8.setStyleSheet(u"padding:0;")
        icon7 = QIcon()
        icon7.addFile(u":/icons/thermometer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setIconSize(QSize(32, 32))

        self.gridLayout_2.addWidget(self.pushButton_8, 5, 0, 1, 1, Qt.AlignLeft)

        self.pushButton_9 = QPushButton(self.menu_frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(36, 36))
        self.pushButton_9.setMaximumSize(QSize(36, 36))
        self.pushButton_9.setStyleSheet(u"padding:0;")
        icon8 = QIcon()
        icon8.addFile(u":/icons/wifi.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon8)
        self.pushButton_9.setIconSize(QSize(32, 32))

        self.gridLayout_2.addWidget(self.pushButton_9, 6, 0, 1, 1, Qt.AlignLeft)

        self.label_5 = QLabel(self.menu_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMargin(5)

        self.gridLayout_2.addWidget(self.label_5, 1, 1, 1, 1, Qt.AlignLeft)

        self.label_6 = QLabel(self.menu_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMargin(5)

        self.gridLayout_2.addWidget(self.label_6, 2, 1, 1, 1, Qt.AlignLeft)

        self.label_7 = QLabel(self.menu_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMargin(5)

        self.gridLayout_2.addWidget(self.label_7, 3, 1, 1, 1, Qt.AlignLeft)

        self.label_8 = QLabel(self.menu_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMargin(5)

        self.gridLayout_2.addWidget(self.label_8, 4, 1, 1, 1, Qt.AlignLeft)

        self.label_9 = QLabel(self.menu_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMargin(5)

        self.gridLayout_2.addWidget(self.label_9, 5, 1, 1, 1, Qt.AlignLeft)

        self.label_10 = QLabel(self.menu_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMargin(5)

        self.gridLayout_2.addWidget(self.label_10, 6, 1, 1, 1, Qt.AlignLeft)

        self.pushButton_3 = QPushButton(self.menu_frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)
        self.pushButton_3.setMinimumSize(QSize(36, 36))
        self.pushButton_3.setMaximumSize(QSize(36, 36))
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/cpu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon9)
        self.pushButton_3.setIconSize(QSize(32, 32))

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 0, 1, 1, Qt.AlignLeft)

        self.pushButton_4 = QPushButton(self.menu_frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(36, 36))
        self.pushButton_4.setMaximumSize(QSize(36, 36))
        self.pushButton_4.setStyleSheet(u"padding:0;")
        icon10 = QIcon()
        icon10.addFile(u":/icons/battery-charging.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon10)
        self.pushButton_4.setIconSize(QSize(32, 32))

        self.gridLayout_2.addWidget(self.pushButton_4, 1, 0, 1, 1, Qt.AlignLeft)


        self.gridLayout.addWidget(self.menu_frame, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_8.addWidget(self.left_menu_cont_frame)

        self.main_body_contents = QFrame(self.main_body_frame)
        self.main_body_contents.setObjectName(u"main_body_contents")
        sizePolicy.setHeightForWidth(self.main_body_contents.sizePolicy().hasHeightForWidth())
        self.main_body_contents.setSizePolicy(sizePolicy)
        self.main_body_contents.setMaximumSize(QSize(16777215, 16777215))
        self.main_body_contents.setFrameShape(QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_body_contents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.main_body_contents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.cpu_and_memory = QWidget()
        self.cpu_and_memory.setObjectName(u"cpu_and_memory")
        self.verticalLayout_3 = QVBoxLayout(self.cpu_and_memory)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Cpu_info = QFrame(self.cpu_and_memory)
        self.Cpu_info.setObjectName(u"Cpu_info")
        self.Cpu_info.setFrameShape(QFrame.StyledPanel)
        self.Cpu_info.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.Cpu_info)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.cpu_main_core = QLabel(self.Cpu_info)
        self.cpu_main_core.setObjectName(u"cpu_main_core")

        self.gridLayout_4.addWidget(self.cpu_main_core, 2, 1, 1, 1)

        self.label_12 = QLabel(self.Cpu_info)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 1)

        self.cpu_count = QLabel(self.Cpu_info)
        self.cpu_count.setObjectName(u"cpu_count")

        self.gridLayout_4.addWidget(self.cpu_count, 0, 1, 1, 1)

        self.label_14 = QLabel(self.Cpu_info)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_14, 2, 0, 1, 1)

        self.label_13 = QLabel(self.Cpu_info)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_4.addWidget(self.label_13, 1, 0, 1, 1)

        self.cpu_per = QLabel(self.Cpu_info)
        self.cpu_per.setObjectName(u"cpu_per")

        self.gridLayout_4.addWidget(self.cpu_per, 1, 1, 1, 1)

        self.cpu_percentage = roundProgressBar(self.Cpu_info)
        self.cpu_percentage.setObjectName(u"cpu_percentage")
        self.cpu_percentage.setMinimumSize(QSize(150, 150))
        self.cpu_percentage.setMaximumSize(QSize(150, 150))

        self.gridLayout_4.addWidget(self.cpu_percentage, 0, 2, 3, 1)


        self.verticalLayout_3.addWidget(self.Cpu_info)

        self.ram_info = QFrame(self.cpu_and_memory)
        self.ram_info.setObjectName(u"ram_info")
        self.ram_info.setFrameShape(QFrame.StyledPanel)
        self.ram_info.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.ram_info)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_15 = QLabel(self.ram_info)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_3.addWidget(self.label_15, 0, 0, 1, 1)

        self.total_ram = QLabel(self.ram_info)
        self.total_ram.setObjectName(u"total_ram")

        self.gridLayout_3.addWidget(self.total_ram, 0, 1, 1, 1)

        self.label_17 = QLabel(self.ram_info)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_3.addWidget(self.label_17, 2, 0, 1, 1)

        self.available_ram = QLabel(self.ram_info)
        self.available_ram.setObjectName(u"available_ram")

        self.gridLayout_3.addWidget(self.available_ram, 1, 1, 1, 1)

        self.label_16 = QLabel(self.ram_info)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_3.addWidget(self.label_16, 1, 0, 1, 1)

        self.used_ram = QLabel(self.ram_info)
        self.used_ram.setObjectName(u"used_ram")

        self.gridLayout_3.addWidget(self.used_ram, 2, 1, 1, 1)

        self.free_ram = QLabel(self.ram_info)
        self.free_ram.setObjectName(u"free_ram")

        self.gridLayout_3.addWidget(self.free_ram, 3, 1, 1, 1)

        self.label_21 = QLabel(self.ram_info)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_3.addWidget(self.label_21, 3, 0, 1, 1)

        self.label_22 = QLabel(self.ram_info)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_3.addWidget(self.label_22, 4, 0, 1, 1)

        self.ram_usage = QLabel(self.ram_info)
        self.ram_usage.setObjectName(u"ram_usage")

        self.gridLayout_3.addWidget(self.ram_usage, 4, 1, 1, 1)

        self.ram_percentage = spiralProgressBar(self.ram_info)
        self.ram_percentage.setObjectName(u"ram_percentage")
        self.ram_percentage.setMinimumSize(QSize(150, 150))
        self.ram_percentage.setMaximumSize(QSize(150, 150))

        self.gridLayout_3.addWidget(self.ram_percentage, 0, 2, 5, 1)


        self.verticalLayout_3.addWidget(self.ram_info)

        self.stackedWidget.addWidget(self.cpu_and_memory)
        self.battery = QWidget()
        self.battery.setObjectName(u"battery")
        self.verticalLayout_4 = QVBoxLayout(self.battery)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_28 = QLabel(self.battery)
        self.label_28.setObjectName(u"label_28")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_28.setFont(font3)

        self.verticalLayout_4.addWidget(self.label_28, 0, Qt.AlignBottom)

        self.frame_3 = QFrame(self.battery)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_29 = QLabel(self.frame_3)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_5.addWidget(self.label_29, 0, 0, 1, 1)

        self.battery_status = QLabel(self.frame_3)
        self.battery_status.setObjectName(u"battery_status")

        self.gridLayout_5.addWidget(self.battery_status, 0, 1, 1, 1)

        self.label_30 = QLabel(self.frame_3)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_5.addWidget(self.label_30, 1, 0, 1, 1)

        self.label_31 = QLabel(self.frame_3)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_5.addWidget(self.label_31, 2, 0, 1, 1)

        self.battery_time_left = QLabel(self.frame_3)
        self.battery_time_left.setObjectName(u"battery_time_left")

        self.gridLayout_5.addWidget(self.battery_time_left, 2, 1, 1, 1)

        self.battery_charge = QLabel(self.frame_3)
        self.battery_charge.setObjectName(u"battery_charge")

        self.gridLayout_5.addWidget(self.battery_charge, 1, 1, 1, 1)

        self.label_32 = QLabel(self.frame_3)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_5.addWidget(self.label_32, 3, 0, 1, 1)

        self.battery_plugged = QLabel(self.frame_3)
        self.battery_plugged.setObjectName(u"battery_plugged")

        self.gridLayout_5.addWidget(self.battery_plugged, 3, 1, 1, 1)

        self.battery_usage = roundProgressBar(self.frame_3)
        self.battery_usage.setObjectName(u"battery_usage")
        self.battery_usage.setMinimumSize(QSize(150, 150))
        self.battery_usage.setMaximumSize(QSize(150, 150))

        self.gridLayout_5.addWidget(self.battery_usage, 0, 2, 4, 1)


        self.verticalLayout_4.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.battery)
        self.system_information = QWidget()
        self.system_information.setObjectName(u"system_information")
        self.verticalLayout_6 = QVBoxLayout(self.system_information)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_4 = QFrame(self.system_information)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_56 = QLabel(self.frame_4)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font)

        self.gridLayout_7.addWidget(self.label_56, 2, 2, 1, 1)

        self.system_date = QLabel(self.frame_4)
        self.system_date.setObjectName(u"system_date")

        self.gridLayout_7.addWidget(self.system_date, 4, 1, 1, 1)

        self.label_51 = QLabel(self.frame_4)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font)

        self.gridLayout_7.addWidget(self.label_51, 4, 0, 1, 1)

        self.label_60 = QLabel(self.frame_4)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font)

        self.gridLayout_7.addWidget(self.label_60, 0, 0, 1, 1)

        self.platform = QLabel(self.frame_4)
        self.platform.setObjectName(u"platform")

        self.gridLayout_7.addWidget(self.platform, 2, 1, 1, 1)

        self.version = QLabel(self.frame_4)
        self.version.setObjectName(u"version")

        self.gridLayout_7.addWidget(self.version, 3, 1, 1, 1)

        self.label_58 = QLabel(self.frame_4)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font)

        self.gridLayout_7.addWidget(self.label_58, 2, 0, 1, 1)

        self.label_61 = QLabel(self.frame_4)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font)

        self.gridLayout_7.addWidget(self.label_61, 3, 0, 1, 1)

        self.system = QLabel(self.frame_4)
        self.system.setObjectName(u"system")
        self.system.setFont(font)

        self.gridLayout_7.addWidget(self.system, 1, 0, 1, 1)

        self.label_55 = QLabel(self.frame_4)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font)

        self.gridLayout_7.addWidget(self.label_55, 3, 2, 1, 1)

        self.label_52 = QLabel(self.frame_4)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font)

        self.gridLayout_7.addWidget(self.label_52, 4, 2, 1, 1)

        self.processor = QLabel(self.frame_4)
        self.processor.setObjectName(u"processor")

        self.gridLayout_7.addWidget(self.processor, 2, 3, 1, 1)

        self.machine = QLabel(self.frame_4)
        self.machine.setObjectName(u"machine")

        self.gridLayout_7.addWidget(self.machine, 3, 3, 1, 1)

        self.system_time = QLabel(self.frame_4)
        self.system_time.setObjectName(u"system_time")

        self.gridLayout_7.addWidget(self.system_time, 4, 3, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.system_information)
        self.activities = QWidget()
        self.activities.setObjectName(u"activities")
        self.verticalLayout_5 = QVBoxLayout(self.activities)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_5 = QFrame(self.activities)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_65 = QLabel(self.frame_5)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_65)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.activity_search = QLineEdit(self.frame_8)
        self.activity_search.setObjectName(u"activity_search")

        self.horizontalLayout_10.addWidget(self.activity_search)

        self.pushButton_10 = QPushButton(self.frame_8)
        self.pushButton_10.setObjectName(u"pushButton_10")
        icon11 = QIcon()
        icon11.addFile(u":/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon11)

        self.horizontalLayout_10.addWidget(self.pushButton_10)


        self.horizontalLayout_9.addWidget(self.frame_8, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.activities)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tableWidget = QTableWidget(self.frame_6)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_7.addWidget(self.tableWidget)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.activities)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_11 = QPushButton(self.frame_7)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout_11.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.frame_7)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.horizontalLayout_11.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.frame_7)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.horizontalLayout_11.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.frame_7)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.horizontalLayout_11.addWidget(self.pushButton_14)


        self.verticalLayout_5.addWidget(self.frame_7, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.activities)
        self.storage = QWidget()
        self.storage.setObjectName(u"storage")
        self.verticalLayout_8 = QVBoxLayout(self.storage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_66 = QLabel(self.storage)
        self.label_66.setObjectName(u"label_66")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_66.setFont(font4)

        self.verticalLayout_8.addWidget(self.label_66)

        self.storageTable = QTableWidget(self.storage)
        if (self.storageTable.columnCount() < 9):
            self.storageTable.setColumnCount(9)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(8, __qtablewidgetitem16)
        self.storageTable.setObjectName(u"storageTable")

        self.verticalLayout_8.addWidget(self.storageTable)

        self.stackedWidget.addWidget(self.storage)
        self.sensors = QWidget()
        self.sensors.setObjectName(u"sensors")
        self.verticalLayout_9 = QVBoxLayout(self.sensors)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_67 = QLabel(self.sensors)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font4)

        self.verticalLayout_9.addWidget(self.label_67)

        self.sensors_table = QTableWidget(self.sensors)
        if (self.sensors_table.columnCount() < 6):
            self.sensors_table.setColumnCount(6)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.sensors_table.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.sensors_table.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.sensors_table.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.sensors_table.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.sensors_table.setHorizontalHeaderItem(4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.sensors_table.setHorizontalHeaderItem(5, __qtablewidgetitem22)
        self.sensors_table.setObjectName(u"sensors_table")

        self.verticalLayout_9.addWidget(self.sensors_table)

        self.stackedWidget.addWidget(self.sensors)
        self.networks = QWidget()
        self.networks.setObjectName(u"networks")
        self.verticalLayout_10 = QVBoxLayout(self.networks)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.scrollArea = QScrollArea(self.networks)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -279, 469, 812))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_68 = QLabel(self.frame_9)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font4)

        self.verticalLayout_12.addWidget(self.label_68)

        self.net_stats_table = QTableWidget(self.frame_9)
        if (self.net_stats_table.columnCount() < 5):
            self.net_stats_table.setColumnCount(5)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(4, __qtablewidgetitem27)
        self.net_stats_table.setObjectName(u"net_stats_table")
        self.net_stats_table.setMinimumSize(QSize(0, 150))

        self.verticalLayout_12.addWidget(self.net_stats_table)


        self.verticalLayout_11.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_69 = QLabel(self.frame_10)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font4)

        self.verticalLayout_13.addWidget(self.label_69)

        self.net_iocounter_table = QTableWidget(self.frame_10)
        if (self.net_iocounter_table.columnCount() < 9):
            self.net_iocounter_table.setColumnCount(9)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.net_iocounter_table.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.net_iocounter_table.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.net_iocounter_table.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.net_iocounter_table.setHorizontalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.net_iocounter_table.setHorizontalHeaderItem(4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.net_iocounter_table.setHorizontalHeaderItem(5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.net_iocounter_table.setHorizontalHeaderItem(6, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.net_iocounter_table.setHorizontalHeaderItem(7, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.net_iocounter_table.setHorizontalHeaderItem(8, __qtablewidgetitem36)
        self.net_iocounter_table.setObjectName(u"net_iocounter_table")
        self.net_iocounter_table.setMinimumSize(QSize(0, 150))

        self.verticalLayout_13.addWidget(self.net_iocounter_table)


        self.verticalLayout_11.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.scrollAreaWidgetContents)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_11)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_70 = QLabel(self.frame_11)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setFont(font4)

        self.verticalLayout_14.addWidget(self.label_70)

        self.net_addresses_table = QTableWidget(self.frame_11)
        if (self.net_addresses_table.columnCount() < 6):
            self.net_addresses_table.setColumnCount(6)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(3, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(4, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(5, __qtablewidgetitem42)
        self.net_addresses_table.setObjectName(u"net_addresses_table")
        self.net_addresses_table.setMinimumSize(QSize(0, 150))

        self.verticalLayout_14.addWidget(self.net_addresses_table)


        self.verticalLayout_11.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.scrollAreaWidgetContents)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_12)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_71 = QLabel(self.frame_12)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setFont(font4)

        self.verticalLayout_15.addWidget(self.label_71)

        self.net_connections_table = QTableWidget(self.frame_12)
        if (self.net_connections_table.columnCount() < 7):
            self.net_connections_table.setColumnCount(7)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(2, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(3, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(4, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(5, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(6, __qtablewidgetitem49)
        self.net_connections_table.setObjectName(u"net_connections_table")
        self.net_connections_table.setMinimumSize(QSize(0, 150))

        self.verticalLayout_15.addWidget(self.net_connections_table)


        self.verticalLayout_11.addWidget(self.frame_12)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_10.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.networks)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addWidget(self.main_body_contents)

        self.right_frame = QFrame(self.main_body_frame)
        self.right_frame.setObjectName(u"right_frame")
        sizePolicy3.setHeightForWidth(self.right_frame.sizePolicy().hasHeightForWidth())
        self.right_frame.setSizePolicy(sizePolicy3)
        self.right_frame.setMaximumSize(QSize(250, 16777215))
        self.right_frame.setStyleSheet(u"background-color: rgb(28, 71, 117);")
        self.right_frame.setFrameShape(QFrame.StyledPanel)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.right_frame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_11 = QLabel(self.right_frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)

        self.verticalLayout_16.addWidget(self.label_11)

        self.textBrowser = QTextBrowser(self.right_frame)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_16.addWidget(self.textBrowser)


        self.horizontalLayout_8.addWidget(self.right_frame)


        self.verticalLayout.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        sizePolicy3.setHeightForWidth(self.footer_frame.sizePolicy().hasHeightForWidth())
        self.footer_frame.setSizePolicy(sizePolicy3)
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.footer_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)


        self.horizontalLayout_5.addWidget(self.frame)

        self.frame_2 = QFrame(self.footer_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_7.addWidget(self.pushButton_2, 0, Qt.AlignRight)

        self.size_grip = QFrame(self.frame_2)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.size_grip, 0, Qt.AlignBottom)


        self.horizontalLayout_5.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.open_close_side_bar_button.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Task MANAGER", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.pushButton_7.setText("")
        self.pushButton_6.setText("")
        self.pushButton_5.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.pushButton_8.setText("")
        self.pushButton_9.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Battery", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Activity", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Storage", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Network", None))
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.cpu_main_core.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"CPU Count", None))
        self.cpu_count.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"CPU Main Core", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"CPU Per", None))
        self.cpu_per.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Total Ram", None))
        self.total_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Used Ram", None))
        self.available_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Available Ram", None))
        self.used_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.free_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Free Ram", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Ram Usage", None))
        self.ram_usage.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Battery Information", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.battery_status.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Time Left", None))
        self.battery_time_left.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.battery_charge.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Plugged In", None))
        self.battery_plugged.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Processor", None))
        self.system_date.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"System Date", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"System Inforamation", None))
        self.platform.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Platform", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.system.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Machine", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"System Time", None))
        self.processor.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.machine.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_time.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Activities", None))
        self.activity_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Processes", None))
        self.pushButton_10.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Process ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Process Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Process Status", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Started", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Suspend", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Resume", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Terminate", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Kill", None));
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Suspend", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Resume", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Terminate", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Kill", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Disk Partition", None))
        ___qtablewidgetitem8 = self.storageTable.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Device", None));
        ___qtablewidgetitem9 = self.storageTable.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Moint Point", None));
        ___qtablewidgetitem10 = self.storageTable.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"OPTS", None));
        ___qtablewidgetitem11 = self.storageTable.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Max file", None));
        ___qtablewidgetitem12 = self.storageTable.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Max Path", None));
        ___qtablewidgetitem13 = self.storageTable.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Total Storage", None));
        ___qtablewidgetitem14 = self.storageTable.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Used Storage", None));
        ___qtablewidgetitem15 = self.storageTable.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Free Storage", None));
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        ___qtablewidgetitem16 = self.sensors_table.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Sensor", None));
        ___qtablewidgetitem17 = self.sensors_table.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Label", None));
        ___qtablewidgetitem18 = self.sensors_table.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Current", None));
        ___qtablewidgetitem19 = self.sensors_table.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"High", None));
        ___qtablewidgetitem20 = self.sensors_table.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Critical", None));
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        ___qtablewidgetitem21 = self.net_stats_table.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"ISUP", None));
        ___qtablewidgetitem22 = self.net_stats_table.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Duplex", None));
        ___qtablewidgetitem23 = self.net_stats_table.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Speed", None));
        ___qtablewidgetitem24 = self.net_stats_table.horizontalHeaderItem(4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"MTU", None));
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Network IO Counter", None))
        ___qtablewidgetitem25 = self.net_iocounter_table.horizontalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"IO", None));
        ___qtablewidgetitem26 = self.net_iocounter_table.horizontalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Bytes Sent", None));
        ___qtablewidgetitem27 = self.net_iocounter_table.horizontalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Bytes Received", None));
        ___qtablewidgetitem28 = self.net_iocounter_table.horizontalHeaderItem(3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Packets Sent", None));
        ___qtablewidgetitem29 = self.net_iocounter_table.horizontalHeaderItem(4)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Packets Received", None));
        ___qtablewidgetitem30 = self.net_iocounter_table.horizontalHeaderItem(5)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"ERR In", None));
        ___qtablewidgetitem31 = self.net_iocounter_table.horizontalHeaderItem(6)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"ERR Out", None));
        ___qtablewidgetitem32 = self.net_iocounter_table.horizontalHeaderItem(7)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Drop In", None));
        ___qtablewidgetitem33 = self.net_iocounter_table.horizontalHeaderItem(8)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Drop Out", None));
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Network Addresses", None))
        ___qtablewidgetitem34 = self.net_addresses_table.horizontalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Family", None));
        ___qtablewidgetitem35 = self.net_addresses_table.horizontalHeaderItem(2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem36 = self.net_addresses_table.horizontalHeaderItem(3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Netmask", None));
        ___qtablewidgetitem37 = self.net_addresses_table.horizontalHeaderItem(4)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Broadcast", None));
        ___qtablewidgetitem38 = self.net_addresses_table.horizontalHeaderItem(5)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"PTP", None));
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Network Connections", None))
        ___qtablewidgetitem39 = self.net_connections_table.horizontalHeaderItem(0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"FD", None));
        ___qtablewidgetitem40 = self.net_connections_table.horizontalHeaderItem(1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Family", None));
        ___qtablewidgetitem41 = self.net_connections_table.horizontalHeaderItem(2)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Family", None));
        ___qtablewidgetitem42 = self.net_connections_table.horizontalHeaderItem(3)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"LADDR", None));
        ___qtablewidgetitem43 = self.net_connections_table.horizontalHeaderItem(4)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"RADDR", None));
        ___qtablewidgetitem44 = self.net_connections_table.horizontalHeaderItem(5)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem45 = self.net_connections_table.horizontalHeaderItem(6)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"PID", None));
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">App Designed And</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Developed By Dhia Eddin</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Boukthir.</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Version 1.0 ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

