#! python2.7
'''
main Caster module
Created on Jun 29, 2014
'''
import six

if six.PY2:
	import logging
	logging.basicConfig()

from castervoice.lib.ctrl.dependencies import DependencyMan  # requires nothing
DependencyMan().initialize()

from castervoice.lib import settings  
settings.initialize()

from castervoice.lib.ctrl.updatecheck import UpdateChecker # requires settings/dependencies
UpdateChecker().initialize()

from dragonfly import get_engine

_NEXUS = None

if get_engine()._name in ["sapi5shared", "sapi5", "sapi5inproc"]:
	settings.WSR = True
	from castervoice.rules.ccr.standard import SymbolSpecs
	SymbolSpecs.set_cancel_word("escape")

from castervoice.lib import control

if control.nexus() is None:
	from castervoice.lib.ctrl.mgr.loading.load.content_loader import ContentLoader
	from castervoice.lib.ctrl.mgr.loading.load.content_request_generator import ContentRequestGenerator
	_crg = ContentRequestGenerator()
	_content_loader = ContentLoader(_crg)
	control.init_nexus(_content_loader)

if settings.SETTINGS["sikuli"]["enabled"]:
	from castervoice.asynch.sikuli import sikuli_controller
	sikuli_controller.get_instance().bootstrap_start_server_proxy()

print("\n*- Starting " + settings.SOFTWARE_NAME + " -*")


#region---=== David
from castervoice.exclusiveness.globalVariable import Data_Manager
from castervoice.exclusiveness import Constant as ct

#--- init
Data_Manager.init()
from castervoice.exclusiveness.store_AllEnabledRule_ofApp import store_AllEnabledRule_ofApp
store_AllEnabledRule_ofApp(ct.default, True)
# from castervoice.exclusiveness.globalVariable.Data_Manager import data,GramAndRules
# data.appGramAndRules[ct.default] = GramAndRules()



#region--- test OnFocusedWindowChanged
# from inspect import getframeinfo, stack, getframeinfo, currentframe
# from castervoice.lib._tests.GUI.OnFocusedWindowChanged import OnFocusedWindowChanged
# OnFocusedWindowChanged()
#endregion test OnFocusedWindowChanged

#region--- GUI
# print "\n", "20200311205425| show GUI for test simulation.",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
# import wx 
# class Mywin(wx.Frame): 
# 	def __init__(self, parent, title): 
# 		super(Mywin, self).__init__(parent, title = title,size = (200,150))  
# 		panel = wx.Panel(self) 
# 		vbox = wx.BoxSizer(wx.VERTICAL) 
			
# 		self.btn = wx.Button(panel,-1,"Simulate NewAppDetected") 
# 		vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
# 		self.btn.Bind(wx.EVT_BUTTON,self.NewAppDetected) 
# 		# self.btn.Bind(wx.EVT_BUTTON,self.SimulateFocusedWIndowsChanged) 
			
# 		self.tbtn = wx.ToggleButton(panel , -1, "click to on") 
# 		vbox.Add(self.tbtn,0,wx.EXPAND|wx.ALIGN_CENTER) 
# 		self.tbtn.Bind(wx.EVT_TOGGLEBUTTON,self.OnToggle) 
			
# 		hbox = wx.BoxSizer(wx.HORIZONTAL) 
			
# 		bmp = wx.Bitmap("NEW.BMP", wx.BITMAP_TYPE_BMP) 
# 		self.bmpbtn = wx.BitmapButton(panel, id = wx.ID_ANY, bitmap = bmp,
# 		 	size = (bmp.GetWidth()+10, bmp.GetHeight()+10)) 
			
# 		# hbox.Add(self.bmpbtn,0,wx.ALIGN_CENTER) 
# 		# self.bmpbtn.Bind(wx.EVT_BUTTON,self.NewAppDetected) 
# 		# self.bmpbtn.SetLabel("NEW") 
			
# 		bmp1 = wx.Bitmap("OPEN.BMP", wx.BITMAP_TYPE_BMP) 
# 		self.bmpbtn1 = wx.BitmapButton(panel, id = wx.ID_ANY, bitmap = bmp1,
# 		 	size = (bmp.GetWidth()+10, bmp.GetHeight()+10)) 
			
# 		# hbox.Add(self.bmpbtn1,0,wx.ALIGN_CENTER) 
# 		# self.bmpbtn1.Bind(wx.EVT_BUTTON,self.NewAppDetected) 
# 		# self.bmpbtn1.SetLabel("OPEN") 
			
# 		bmp2 = wx.Bitmap("SAVE.BMP", wx.BITMAP_TYPE_BMP) 
# 		self.bmpbtn2 = wx.BitmapButton(panel, id = wx.ID_ANY, bitmap = bmp2,
# 		 	size = (bmp.GetWidth()+10, bmp.GetHeight()+10))
			
# 		# hbox.Add(self.bmpbtn2,0,wx.ALIGN_CENTER) 
# 		# self.bmpbtn2.Bind(wx.EVT_BUTTON,self.NewAppDetected)
# 		# self.bmpbtn2.SetLabel("SAVE") 
			
# 		vbox.Add(hbox,1,wx.ALIGN_CENTER) 
# 		panel.SetSizer(vbox) 
			
# 		self.Centre() 
# 		self.Show() 
# 		self.Fit()  
		
# 	# def SimulateFocusedWIndowsChanged(self, event): #id20200108135455
# 	def NewAppDetected(self, event_data): #id20200108135454
# 		pass
# 		# print "\n", "Gui button 'Simulate NewAppDetected' pressed.",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
# 		# OnFocusedWindowChanged()
# 		#region--- (old)
# 		# #--- (not True) !! carefull: when, for example, the Dictaion Box is been forground, the button will NOT respond.
# 		# # gl.dbgInd["childs"] = gl.dbgInd["childs"] + "--|"
		
# 		# # print "\n", gl.dbgInd["childs"],"20200108204206| in 'def NewAppDetected'"

# 		# btn = event.GetEventObject().GetLabel()
# 		# TamFc.Notify_enter_context(None,None)
# 		# # TamFc.handle_forgroundAppChanged()

# 		# # data.currWindHndl =  Window.get_foreground().handle
# 		# # TamFc.processExclusivForNewApp(None,None)

# 		# # gl.dbgInd["childs"] = gl.dbgInd["childs"].replace('--|', '', 1)
# 		#endregion 
		
		
# 	def OnToggle(self,event): 
# 		state = event.GetEventObject().GetValue() 
		
# 		if state == True: 
# 			print "Toggle button state off" 
# 			event.GetEventObject().SetLabel("click to off") 
# 		else: 
# 			print " Toggle button state on" 
# 			event.GetEventObject().SetLabel("click to on") 
				
# app = wx.App() 
# Mywin(None,  'Button demo') 


# # Mywin.Show(,)
# # frm.Show()
# # app.MainLoop()

#endregion--- GUI

#endregion David. Tests
