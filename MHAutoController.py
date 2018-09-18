# -- coding: UTF-8 --
# 控制器
import wx
from mhView import *
from mhModel import * 

class MHAutoController(object):

	def __init__(self):
		#实例化
		self.app = wx.App(False)
		self.frame = wx.Frame(None, wx.ID_ANY,"MH辅助软件",pos=(800+4,600-320) ,size=(480,320))
		self.frame.SetBackgroundColour((255,255,255))
		self.frame.Show(True)

		# 初始化控件view
		self.mhV = mhView(self.frame)
		#初始化模型
		self.mhModel = mhModel()

		#点击保存按钮,输出保存设置
		def saveClick(event):
			# tea = mhV.teachChe.GetValue()
			self.mhModel.printStr = ('当前已选择任务：\n')
			if self.mhV.teachChe.GetValue() == True:
				self.mhModel.printStr = self.mhModel.printStr + ('自动师门\n')
				self.mhModel.isTeach = True
			if self.mhV.demonChe.GetValue() == True:
				self.mhModel.printStr = self.mhModel.printStr + ('秘境降妖\n')
				self.mhModel.isDemon = True
			if self.mhV.mapChe.GetValue() == True:
				self.mhModel.isMap = True
				self.mhModel.printStr = self.mhModel.printStr + ('自动宝图\n')
			if self.mhV.moveChe.GetValue() == True:
				self.mhModel.isMove = True
				self.mhModel.printStr = self.mhModel.printStr + ('自动运镖\n')
			#保存设置	
			print("保存设置")
			print(self.mhModel.printStr)
			self.mhModel.isSave = True	
			self.mhV.printTextLab.SetLabel(self.mhModel.printStr)



		#弹框提示保存
		def showLog():
			wx.MessageBox("请选择任务", "Message" ,wx.OK | wx.ICON_INFORMATION)
			
			
		#移动游戏窗口
		def moveHandle():
			print('调整窗口')
			
		def runMission():
			print('开始执行')
			
			
			
		#-开始执行
		def beginClick(event):
			
			if self.mhModel.isSave == True:
				#开始执行
				moveHandle()
				
				runMission()
				
	
			else:  		
				showLog()
			


		#绑定点击事件，保存按钮
		self.frame.Bind(wx.EVT_BUTTON,saveClick,self.mhV.saveBtn)
		#绑定点击事件，开始按钮
		self.frame.Bind(wx.EVT_BUTTON,beginClick,self.mhV.beginBtn)

		self.app.MainLoop()		



	


