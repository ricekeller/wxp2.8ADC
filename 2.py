import wx
class MyApp(wx.App):
	"""docstring for MyApp"""
	def OnInit(self):
		self.frame=MyFrame(None,title="The Main Frame")
		self.SetTopWindow(self.frame)
		self.frame.Show()
		return True

class MyFrame(wx.Frame):
	"""docstring for MyFrame"""
	def __init__(self, parent,id=wx.ID_ANY,title="",
					pos=wx.DefaultPosition,size=wx.DefaultSize,
					style=wx.DEFAULT_FRAME_STYLE,name="MyFrame"):
		super(MyFrame, self).__init__(parent,id,title,
										pos,size,style,name)
		self.panel=wx.Panel(self)

		self.panel.SetBackgroundColour(wx.BLUE)

		self.button=wx.Button(self.panel,
								label="Push Me",
								pos=(50,50))

if __name__=="__main__":
	app=MyApp(False)
	app.MainLoop()
		
