# -- coding: UTF-8 --
# 控制器
import wx
from mhView import *
from mhModel import * 
from mhMissionState import * 
import win32api
import win32gui
import win32con


class MHAutoController(object):

	def __init__(self):
		#实例化
		self.app = wx.App(False)
		self.frame = wx.Frame(None, wx.ID_ANY,"MH辅助软件",pos=(800+4,600-320) ,size=(480,320))
		self.frame.SetBackgroundColour((255,255,255))
		self.frame.Show(True)

		# 初始化控件view
		self.mhV = mhView(self.frame)
		# 初始化模型
		self.mhModel = mhModel()		

		#移动游戏窗口
		def moveHandle():
						
			wdname = '《梦幻西游》手游'
			handle = win32gui.FindWindow(0,wdname)			
			if handle == 0:
				print("没有找到窗口")
			else:
				print('调整窗口')
				print(win32gui.GetWindowRect(handle))	
				#调整窗口到左上角
				win32gui.MoveWindow(handle,0,0,800,600,False)
				#重新获取窗口大小
				handle = win32gui.FindWindow(0,wdname)		
				handleList = win32gui.GetWindowRect(handle)
				print(handleList)
				#鼠标移动到右下角
				win32api.SetCursorPos((handleList[2]-1,handleList[3]-1))
				# 点击鼠标左键
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
			    #调整大小
				win32api.SetCursorPos((800,600)) 
				#放开鼠标
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)			


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
			moveHandle()


		#弹框提示保存
		def showLog():
			wx.MessageBox("请选择任务", "Message" ,wx.OK | wx.ICON_INFORMATION)
			
			
		def runMission():
			
			mhState = mhMissionState()
			
			if mhState.stateStr == mhState.STATE_TEACH:
				print('开始师门')	
			if mhState.stateStr == mhState.STATE_DEON:
				print('开始秘境')
			if mhState.stateStr == mhState.STATE_MAP:
				print('开始宝图')	
			if mhState.stateStr == mhState.STATE_MOVE:
				print('开始押镖')				
			
			
			
		#-开始执行
		def beginClick(event):
			
			if self.mhModel.isSave == True:
				#开始执行

				runMission()
				
	
			else:  		
				showLog()
			


		#绑定点击事件，保存按钮
		self.frame.Bind(wx.EVT_BUTTON,saveClick,self.mhV.saveBtn)
		#绑定点击事件，开始按钮
		self.frame.Bind(wx.EVT_BUTTON,beginClick,self.mhV.beginBtn)

		self.app.MainLoop()		



	


