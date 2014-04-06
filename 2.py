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

		self.panel.SetBackgroundColour(wx.GREEN)
		
		button=wx.Button(self.panel,
								label="Push Me",
								pos=(50,50))
		self.btnId=button.GetId()
		self.Bind(wx.EVT_BUTTON, self.OnButton, button)
		
	
	def OnButton(self,event):
		"""called when the button is clicked"""
		print "\nFrame GetChildren:"
		for child in self.GetChildren():
			print "%s" % repr(child)
		
		print "\nPanel FindWindowById:"
		button=self.panel.FindWindowById(self.btnId)
		print "%s" % repr(button)
		button.SetLabel("Changed Label")
		
		print "\nButton GetParent:"
		panel=button.GetParent()
		print "%s" % repr(panel)
		
		print "\nGet the application object:"
		app=wx.GetApp()
		print "%s" % repr(app)
		
		print "\nGet the Frame from the App:"
		frame=app.GetTopWindow()
		print "%s" % repr(frame)

if __name__=="__main__":
	app=MyApp(False)
	app.MainLoop()
		
