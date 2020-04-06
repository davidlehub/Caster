from castervoice.lib import printer
from castervoice.lib.merge.ccrmerging2.hooks.base_hook import BaseHook
from castervoice.lib.merge.ccrmerging2.hooks.events.event_types import EventType

#region--- (david)
from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.exclusiveness.globalVariable import GlobalV as gl

def Update_RbeenExclusive(rule_className, active):

	# print "\n", "dbg20200323124506| in Update_RbeenExclusive() | rule_className, active:", rule_className, active, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	if active and (rule_className not in gl.RbeenActive):
		gl.RbeenActive.append(rule_className)
		print "\t", "dbg20200319191943| rule added to 'gl.RbeenActive':", rule_className, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

	else:
		try:
			# print "\t", "dbg20200319191944a|Before gl.RbeenActive:", gl.RbeenActive, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
			gl.RbeenActive.remove(rule_className) #not sure about this line. It got exception?
			print "\t", "dbg20200319191944| rule remove from 'gl.RbeenActive':", rule_className, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
			# print "\t", "dbg20200319191944b|After gl.RbeenActive:", gl.RbeenActive, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		except :
			pass
#endregion (david)

class PrinterHook(BaseHook):

	def __init__(self):
		super(PrinterHook, self).__init__(EventType.ACTIVATION)

	def get_pronunciation(self):
		return "printer"

	def run(self, event):
		state = "active" if event.active else "inactive"
		printer.out("The rule {} was set to {}.".format(event.rule_class_name, state))

		#region--- (david)
		""" The reason of adding this: bcz, for example, when user say 'enable/disble python',
  			we want the 'gl.RbeenActive' to be uptodate. 
		"""  
		Update_RbeenExclusive(event.rule_class_name, event.active)
		# detect_SpeechEngineVocabulary_activation(event.rule_class_name, event.active) 
		#endregion (david)
		

def get_hook():
	return PrinterHook
