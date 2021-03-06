# -- coding: UTF-8 --
# 控件的view
import wx

class mhView(object):

	def __init__(self, frame):

		#相关尺寸定义
		appWidth = 480
		appHeigth = 320

		#保存设置按钮	
		self.saveBtn = wx.Button(frame, -1, '保存设置',pos=(120,16),size=(88,40))
		#开始运行按钮	
		self.beginBtn = wx.Button(frame, -1, '开始运行',pos=(120, 16+32+16),size=(88,40))
		#添加标签
		self.teachChe = wx.CheckBox(frame,label='师门任务',pos=(16,16),style=wx.RB_GROUP,size=(88,40))
		self.demonChe = wx.CheckBox(frame,label='秘境降妖',pos=(16,16+32),size=(88,40),style=wx.RB_GROUP)
		self.mapChe = wx.CheckBox(frame,label='宝图任务',pos=(16,16+32*2),size=(88,40),style=wx.RB_GROUP)
		self.moveChe = wx.CheckBox(frame,label='运镖活动',pos=(16,16+32*3),size=(88,40),style=wx.RB_GROUP)

		#添加文本框标签内容
		self.printLab = wx.StaticText(frame,-1, label='输出显示:',pos=(appWidth/2,4),size=(100,26))
		printLabFont = wx.Font(16, wx.ROMAN, wx.NORMAL, wx.FONTWEIGHT_BOLD)
		self.printLab.SetFont(printLabFont)

		#添加输出框
		self.printTextLab = wx.StaticText(frame,pos=(appWidth/2,4+26),size=(appWidth/2-32,appHeigth-88),style=wx.TE_MULTILINE)
		self.printTextLab.SetBackgroundColour((220,220,220))





