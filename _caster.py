#! python2.7
'''
main Caster module
Created on Jun 29, 2014
'''
import six

#region--- (david)
from castervoice.exclusiveness.globalVariable import Data_Manager
#--- init
Data_Manager.init()
#endregion (david)

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
from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.exclusiveness.store_AllEnabledRule_ofApp import store_AllEnabledRule_ofApp
from castervoice.exclusiveness import Constant as ct
from castervoice.exclusiveness.Notify_on_begin_fromDragonFly import Notify_on_begin_fromDragonFly
from castervoice.exclusiveness.cls.DragonVocabulary_cls import DragonVocabulary

# #--- init
# Data_Manager.init()
store_AllEnabledRule_ofApp(ct.default, True)

#__ Lets say that user want to start with exclusive mode (= disable DNS vocabulary)
DragonVocabulary.disable()

#__
Notify_on_begin_fromDragonFly() # To make it start into exclusive mode (if user wanted).



# from castervoice.exclusiveness.globalVariable.Data_Manager import data,GramAndRules
# data.appGramAndRules[ct.default] = GramAndRules()


#region--- (turn of exclusive esystem)
# from castervoice.exclusiveness.ExclusivMode_class import ExclusivMode
# #--- Don't forget: 'ExclusiveHook = false' in hooks.toml
# ExclusivMode.set_enabled(False)
# from inspect import getframeinfo, stack, getframeinfo, currentframe
# print "\n", "20200322105039| ExclusivMode is setted to False",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
#endregion (turn of exclusive esystem)

 

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
			
# 		self.btn = wx.Button(panel,-1,"Simulate bt1") 
# 		vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
# 		self.btn.Bind(wx.EVT_BUTTON,self.bt1) 
# 		# self.btn.Bind(wx.EVT_BUTTON,self.SimulateFocusedWIndowsChanged) 
			
# 		self.tbtn = wx.ToggleButton(panel , -1, "click to on") 
# 		vbox.Add(self.tbtn,0,wx.EXPAND|wx.ALIGN_CENTER) 
# 		self.tbtn.Bind(wx.EVT_TOGGLEBUTTON,self.OnToggle) 
			
# 		hbox = wx.BoxSizer(wx.HORIZONTAL) 
			
# 		bmp = wx.Bitmap("NEW.BMP", wx.BITMAP_TYPE_BMP) 
# 		self.bmpbtn = wx.BitmapButton(panel, id = wx.ID_ANY, bitmap = bmp,
# 		 	size = (bmp.GetWidth()+10, bmp.GetHeight()+10)) 
			
# 		# hbox.Add(self.bmpbtn,0,wx.ALIGN_CENTER) 
# 		# self.bmpbtn.Bind(wx.EVT_BUTTON,self.bt1) 
# 		# self.bmpbtn.SetLabel("NEW") 
			
# 		bmp1 = wx.Bitmap("OPEN.BMP", wx.BITMAP_TYPE_BMP) 
# 		self.bmpbtn1 = wx.BitmapButton(panel, id = wx.ID_ANY, bitmap = bmp1,
# 		 	size = (bmp.GetWidth()+10, bmp.GetHeight()+10)) 
			
# 		# hbox.Add(self.bmpbtn1,0,wx.ALIGN_CENTER) 
# 		# self.bmpbtn1.Bind(wx.EVT_BUTTON,self.bt1) 
# 		# self.bmpbtn1.SetLabel("OPEN") 
			
# 		bmp2 = wx.Bitmap("SAVE.BMP", wx.BITMAP_TYPE_BMP) 
# 		self.bmpbtn2 = wx.BitmapButton(panel, id = wx.ID_ANY, bitmap = bmp2,
# 		 	size = (bmp.GetWidth()+10, bmp.GetHeight()+10))
			
# 		# hbox.Add(self.bmpbtn2,0,wx.ALIGN_CENTER) 
# 		# self.bmpbtn2.Bind(wx.EVT_BUTTON,self.bt1)
# 		# self.bmpbtn2.SetLabel("SAVE") 
			
# 		vbox.Add(hbox,1,wx.ALIGN_CENTER) 
# 		panel.SetSizer(vbox) 
			
# 		self.Centre() 
# 		self.Show() 
# 		self.Fit()  
		
# 	def bt1(self, event_data): 
# 		from castervoice.exclusiveness.globalVariable import GlobalV as gl
# 		from castervoice.lib.actions import Text
# 		from castervoice.lib.merge.state.short import R
# 		from castervoice.exclusiveness.Set_Exclusiveness_ForRules import Set_Exclusiveness_ForRules


# 		for RegisteredR in gl.allRegisteredRule:
# 			if RegisteredR.className == 'UniqMode_NonCCR':
# 				ruleClass = RegisteredR.rule_class
# 				ruleClass.mapping = {"(done | finished)": R(Text("coucou 20200324113924"), rdescript="test test")} 
# 				Set_Exclusiveness_ForRules(['UniqMode_NonCCR'])
 
# 				print "\n", "ici20200324113228| :", ruleClass.mapping, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

# 				break
		
# 	# def SimulateFocusedWIndowsChanged(self, event): #id20200108135455

	
# 	# def bt1(self, event_data): 
# 	# 	# pass
# 	# 	from castervoice.exclusiveness.exclusiveness_OnOff import exclusiveness_OnOff

# 	# 	exclusiveness_OnOff()


# 	# 	# print "\n", "Gui button 'Simulate bt1' pressed.",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
# 	# 	# OnFocusedWindowChanged()
# 	# 	#region--- (old)
# 	# 	# #--- (not True) !! carefull: when, for example, the Dictaion Box is been forground, the button will NOT respond.
# 	# 	# # gl.dbgInd["childs"] = gl.dbgInd["childs"] + "--|"
		
# 	# 	# # print "\n", gl.dbgInd["childs"],"20200108204206| in 'def bt1'"

# 	# 	# btn = event.GetEventObject().GetLabel()
# 	# 	# TamFc.Notify_enter_context(None,None)
# 	# 	# # TamFc.handle_forgroundAppChanged()

# 	# 	# # data.currWindHndl =  Window.get_foreground().handle
# 	# 	# # TamFc.processExclusivForNewApp(None,None)

# 	# 	# # gl.dbgInd["childs"] = gl.dbgInd["childs"].replace('--|', '', 1)
# 	# 	#endregion 
		
		
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
