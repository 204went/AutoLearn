# -- coding: UTF-8 --
import wx

#相关尺寸定义
def appWidth():
	return 480

def appHeigth():
	return 320

print('开始创建窗口')
#实例化
app=wx.App(False)
frame = wx.Frame(None, wx.ID_ANY,"MH辅助软件",size=(appWidth(),appHeigth()))
# frame.SetValue())
frame.Show(True)


#保存设置按钮	
saveBtn = wx.Button(frame, -1, '保存设置',pos=(120,16),size=(88,40))
#开始运行按钮	
beginBtn=wx.Button(frame, -1, '开始运行',pos=(120, 16+32),size=(88,40))
#添加标签
teachBtn=wx.RadioButton(frame,label='师门任务',pos=(16,16),style=wx.RB_GROUP,size=(88,40))
demonBtn=wx.RadioButton(frame,label='秘境降妖',pos=(16,16+32),size=(88,40),style=wx.RB_GROUP)
demonBtn=wx.RadioButton(frame,label='宝图任务',pos=(16,16+32*2),size=(88,40),style=wx.RB_GROUP)
demonBtn=wx.RadioButton(frame,label='运镖活动',pos=(16,16+32*3),size=(88,40),style=wx.RB_GROUP)

#添加文本框显示输出内容
# printText = wx.StaticText(frame,-1, label='输出显示',pos=(appWidth()-100,16),size=(100,200))
#显示窗口
print('显示窗口')
app.MainLoop()		



	










