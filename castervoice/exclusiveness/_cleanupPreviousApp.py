from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.exclusiveness.globalVariable.Data_Manager import data
from castervoice.exclusiveness.appExist import appExist


def _cleanupPreviousApp():
	""" Cleanup/purge exclusiveness for previous app, IF needed """
	if not data.prevWindHndl or not data.appExclusiveness.has_key(data.prevWindHndl):
		# print "\n|~icici20191219125222| cancel function '_cleanupPreviousApp', bcz in 'if not data.prevWindHndl' " , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno) #checked 20200322131735
		# print "\b|~icici20191219125222b| or , bcz in 'if not data.appExclusiveness.has_key(data.prevWindHndl)' " , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		return	

	#---- delete data.appExclusiveness if thre is no any UML layer... ANd when detec app (the handle) is no more exist.
	if data.count_UML_ofApp(data.prevWindHndl) <= 0:
		# print "\n\t|~ici 20191208115134| delete data.appExclusiveness of previous app, bcz it has is no any UML layer.",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno) #checked 20200322131735
		del data.appExclusiveness[data.prevWindHndl]			

	#---- Also delete data.appExclusiveness if that app doesn't exist anymore.
	elif not appExist(data.prevWindHndl):
		print "\n\t|~ici 20191208115135| delete data.appExclusiveness of previous app, bcz that app doesn't exist anymore (closed).",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		#---- delete data.appExclusiveness
		del data.appExclusiveness[data.prevWindHndl]		

	
	
	#region--- (old caster)
	# """ Cleanup/purge exclusiveness for previous app, IF needed """
	# if not data.prevWindHndl or not data.appExclusiveness.has_key(data.prevWindHndl):
	# 	# print "\n|~icici20191219125222| cancel function '_cleanupPreviousApp', bcz in 'if not data.prevWindHndl' " , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 	# print "\b|~icici20191219125222b| or , bcz in 'if not data.appExclusiveness.has_key(data.prevWindHndl)' " , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 	return

	# #---- flush/purge/rest exclusiveness for prev app. (bcz gonna have different set for the new app.)
	# 	#-- (Do this step before, possibly, deleting data, in farther step belpw).
	# #-- remove/delete all _NEXUS.merger_grammars
	# #region--- (TD: To upgrade for new Caster)
	# print "\n", "TD 20200111180545| To upgrade for new Caster:",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)	
	# # _NEXUS.merger.wipe()
	# #endregion 

	
	# retAllCompositeMergedRules, retGrmAndRule, currMergedCcRule_inf = getMergedRules_obj() 
	# # print "\n\t|~ici 20191214222124| cleanup, unmergeCcRules.|currMergedCcRule_inf:", currMergedCcRule_inf, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# unmergeCcRules(currMergedCcRule_inf)

	# # print "\n\t|~ici 20191214222124b| cleanup, unSetAll_GramzBeenExclusi.", " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)		
	# unSetAll_GramzBeenExclusi([], "", data.prevWindHndl) # works
	
	# #---- delete data.appExclusiveness if thre is no any UML layer... ANd when detec app (the handle) is no more exist
	# if data.count_UML_ofApp(data.prevWindHndl) <= 0:
	# 	# print "\n\t|~ici 20191208115134| delete data.appExclusiveness of previous app, bcz it has is no any UML layer.",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 	del data.appExclusiveness[data.prevWindHndl]			

	# #---- Also delete data.appExclusiveness if that app doesn't exist anymore.
	# elif not appExist(data.prevWindHndl):
	# 	print "\n\t|~ici 20191208115135| delete data.appExclusiveness of previous app, bcz that app doesn't exist anymore (closed).",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 	#---- delete data.appExclusiveness
	# 	del data.appExclusiveness[data.prevWindHndl]		

	# 	#--- old			
	# 	# try:
	# 	# 	# print "\n|~ici 20191207213032| gl._PrevAppHwn:", data.prevWindHndl, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 	# 	x = win32gui.GetClassName(data.prevWindHndl)
	# 	# except: #-- (app doesn't exist anymore)
	# 	# 	#---- delete data.appExclusiveness
	# 	# 	print "\n\t|~ici 20191208115135| delete data.appExclusiveness of previous app, bcz that app doesn't exist anymore (closed).",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 	# 	del data.appExclusiveness[data.prevWindHndl]			

	#endregion 	
