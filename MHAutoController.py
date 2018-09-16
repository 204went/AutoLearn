# -- coding: UTF-8 --
# 控制器
import wx
from mhView import *
from mhModel import * 

#实例化
app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY,"MH辅助软件",pos=(800+4,600-320) ,size=(480,320))
frame.SetBackgroundColour((255,255,255))
frame.Show(True)

# 初始化控件view
mhV = mhView(frame)
 #初始化模型
mhModel = mhModel()

#点击保存按钮,输出保存设置
def saveClick(event):
	# tea = mhV.teachChe.GetValue()
	mhModel.printStr = ('当前已选择任务：\n')
	if mhV.teachChe.GetValue() == True:
		mhModel.printStr = mhModel.printStr + ('自动师门\n')
		mhModel.isTeach = True
	if mhV.demonChe.GetValue() == True:
		mhModel.printStr = mhModel.printStr + ('秘境降妖\n')
		mhModel.isDemon = True
	if mhV.mapChe.GetValue() == True:
		mhModel.isMap = True
		mhModel.printStr = mhModel.printStr + ('自动宝图\n')
	if mhV.moveChe.GetValue() == True:
		mhModel.isMove = True
		mhModel.printStr = mhModel.printStr + ('自动运镖\n')
	#保存设置
	mhModel.isSave = True	
	mhV.printTextLab.SetLabel(mhModel.printStr)


#----------------------------------------------------------------------
def beginClick():
	if mhModel.isSave == True:
		#开始执行
		pass
	
	else:  		
		pass
		#提示进行保存
	
		


#绑定点击事件，保存按钮
frame.Bind(wx.EVT_BUTTON,saveClick,mhV.saveBtn)
#绑定点击事件，开始按钮
frame.Bind(wx.EVT_BUTTON,saveClick,mhV.beginBtn)


app.MainLoop()		



	


