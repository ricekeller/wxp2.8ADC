import wx
class MyApp(wx.App):
    """docstring for MyApp"""
    def OnInit(self):
        self.frame=MyFrame1(None)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True
    
class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "lalala", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
        
        self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_panel4 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_notebook1.AddPage( self.m_panel4, u"a page", False )
        self.m_panel5 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_notebook1.AddPage( self.m_panel5, u"a page", False )
        self.m_panel6 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_notebook1.AddPage( self.m_panel6, u"a page", False )
        self.m_panel7 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_notebook1.AddPage( self.m_panel7, u"a page", False )
        
        gSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_button4 = wx.Button( self.m_panel3, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_button4, 0, wx.ALL, 5 )
        
        self.m_button5 = wx.Button( self.m_panel3, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_button5, 0, wx.ALL, 5 )
        
        self.m_button6 = wx.Button( self.m_panel3, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_button6, 0, wx.ALL, 5 )
        
        self.m_button7 = wx.Button( self.m_panel3, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_button7, 0, wx.ALL, 5 )
        
        self.m_button8 = wx.Button( self.m_panel3, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_button8, 0, wx.ALL, 5 )
        
        
        self.m_panel3.SetSizer( bSizer1 )
        self.m_panel3.Layout()
        bSizer1.Fit( self.m_panel3 )
        gSizer1.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( gSizer1 )
        self.Layout()
        self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
        self.m_menu11 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu11.AppendItem( self.m_menuItem1 )
        
        self.m_menuItem2 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu11.AppendItem( self.m_menuItem2 )
        
        self.m_menu1.AppendSubMenu( self.m_menu11, u"MyMenu" )
        
        self.m_menubar1.Append( self.m_menu1, u"MyMenu" ) 
        
        self.m_menu2 = wx.Menu()
        self.m_menubar1.Append( self.m_menu2, u"MyMenu" ) 
        
        self.m_menu3 = wx.Menu()
        self.m_menubar1.Append( self.m_menu3, u"MyMenu" ) 
        
        self.SetMenuBar( self.m_menubar1 )
        
        self.m_toolBar1 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
        self.m_toolBar1.Realize() 
        
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_button4.Bind( wx.EVT_BUTTON, self.m_button4OnButtonClick )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def m_button4OnButtonClick( self, event ):
        event.Skip()
        
if __name__=="__main__":
    app=MyApp(False)
    app.MainLoop()