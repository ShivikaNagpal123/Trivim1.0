# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Field_Planning.ui'
#
# Created: Sat Nov 29 13:02:05 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
import os, sys
from os.path import expanduser
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.home = expanduser("~")
        self.trivim_home= open(os.path.join(self.home,"Trivim.txt"),'r').readline()
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(300, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../bin_31/bin/isro.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 290, 370))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        
        b= QtGui.QPushButton()
        b= self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 270, 111, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
        
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 50, 161, 30))
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setText(_translate("Dialog", "NAME", None))
        
        
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(80, 50, 150, 31))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        
        fw = open(os.path.join(self.trivim_home,'curr_proj.txt'),'r')
        pathDir = fw.readline()
        fw.close()
        os.chdir(pathDir)
        pathDir=os.getcwd()
        paths = pathDir.split('\\')
        index=len(paths)-1
        projName ='column'+'.txt'
                        
        fw=open(projName,'r')
        global line
        line = fw.readlines()
        

        
        i=0
        self.a=line
        #self.b=[]
        while(i<len(line)):
            
            #self.a[i]= Label(self, text=line[i].upper(), font=self.customFont, height=2)
            #self.a[i].grid(row=(), column=0, columnspan=2, sticky=W)
            
            #self.a[i] = Entry(self)
            #self.a[i].grid(row= (26+4*i),column=6, columnspan =2, sticky = W)
            self.label_2 = QtGui.QLabel(self.groupBox)
            self.label_2.setGeometry(QtCore.QRect(10, 100+50*i, 131, 30))
            self.label_2.setObjectName(_fromUtf8("label_2"))
            self.label_2.setText(_translate("Dialog", self.a[i], None))

            self.plainTextEdit_2= QtGui.QPlainTextEdit(self.groupBox)
            self.plainTextEdit_2.setGeometry(QtCore.QRect(80, 100+50*i, 150, 30))
            self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
            
            i+=1
            
        print "self.a", self.a
        #print "self.b", self.b

        self.buttonBox = QtGui.QDialogButtonBox(self.groupBox)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setGeometry(QtCore.QRect(10, 320, 100, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(Dialog)

        b.clicked.connect(self.DatabaseValue)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        		
        QtCore.QMetaObject.connectSlotsByName(Dialog)
		
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Save Details", None))
        self.pushButton.setText(_translate("Dialog", "SUBMIT", None))
        self.groupBox.setTitle(_translate("Dialog", "Enter Details", None))

        
  
        
    def DatabaseValue(self):
            
            database = [str(self.plainTextEdit.toPlainText())+"\n"]
            print "database", database
            for i in range(0,len(line)):
                #print self.b[i]
                database.append(str(self.plainTextEdit_2.toPlainText())+"\n")
            with open("tempGUI.txt",'w') as data:
                    data.writelines(database)
            self.w= QtGui.QDialog()
            self.w.setObjectName(_fromUtf8("w"))
            self.m = QtGui.QMessageBox(self.w)
            self.m.setObjectName(_fromUtf8("m"))
            self.m.setText(_translate("self.w", "Value Saved Successfully", None))
            self.m.setWindowTitle(_translate("self.w", "Message", None))
            self.m.exec_()    

    

        
        

    def placemark(self,values,lat,longi,altitude): #values is a list of values to be filled in the placemark file
        
        f = open('First.txt','rb')
        linesCol = f.readlines()
        totalLength = len(linesCol)
        f.close()

        f = open('Placemark.kml','r') #reading from the previously created Placemark file
        lines = f.readlines()
        temp = len(lines)
        f.close()
        fw = open('temp.kml','w')
    
        '''Based on the assumption that user-defined attributes does not contain
        Name and values[0] is always the name of the building
        and after that are the other attributes'''
    
        for i in range(temp-2):
            fw.writelines(lines[i])
        
        fw.writelines('<Placemark>\n\
            <name>'+values[0]+'</name>\n\
            <ExtendedData>')
        for i in range(totalLength):
            fw.writelines('<Data name="'+(linesCol[i])[:-2]+'">\n\
                <value>'+values[i+1]+'</value>\n\
              </Data>')
        fw.writelines('</ExtendedData>\n\
            <Point>\n\
              <coordinates>'+lat+','+longi+','+altitude+'</coordinates>\n\
                  <altitudeMode>relativeToGround</altitudeMode>\n\
                  <extrude>1</extrude>\n\
            </Point>\n\
        </Placemark>\n')

        fw.writelines((lines[temp-2]))
        fw.writelines((lines[temp-1]))
        fw.close()
        os.remove('Placemark.kml')
        os.rename('temp.kml','Placemark.kml')
