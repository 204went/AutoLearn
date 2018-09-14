# -- coding: UTF-8 --
# 控制器
import wx
from mhView import *


#实例化
app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY,"MH辅助软件",pos=(800+4,600-320) ,size=(480,320))
frame.SetBackgroundColour((255,255,255))
frame.Show(True)

# 初始化控件view
mhV = mhView(frame)


#点击保存按钮,输出保存设置
def saveCLick(event):
	# tea = mhV.teachChe.GetValue()
	ChoseText = ('当前已选择任务：\n')
	if mhV.teachChe.GetValue() == True:
		ChoseText = ChoseText + ('自动师门\n')
	if mhV.demonChe.GetValue() == True:
		ChoseText = ChoseText + ('秘境降妖\n')
	if mhV.mapChe.GetValue() == True:
		ChoseText = ChoseText + ('自动宝图\n')
	if mhV.moveChe.GetValue() == True:
		ChoseText = ChoseText + ('自动运镖\n')
	mhV.printTextLab.SetLabel(ChoseText)

#绑定点击事件
frame.Bind(wx.EVT_BUTTON,saveCLick,mhV.saveBtn)



app.MainLoop()		



	










