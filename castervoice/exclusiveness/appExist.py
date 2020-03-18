from inspect import getframeinfo, stack, getframeinfo, currentframe
import win32gui


def appExist(aWindHndl):
		try:
			x = win32gui.GetClassName(aWindHndl)
			print "\n|~ici 20191207213032| x:", x, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
			return True
		except: #-- (app doesn't exist anymore)
			return False
