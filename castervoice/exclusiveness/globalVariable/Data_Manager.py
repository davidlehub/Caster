from castervoice.lib.ctrl.mgr.rules_config import RulesConfig


# from operator import attrgetter
from inspect import getframeinfo, stack, getframeinfo, currentframe
from dragonfly.engines import get_engine
# from dragonfly.grammar.grammar_base import Grammar
from castervoice.lib.control import _NEXUS
# from rules.lib import TamFunction as TamFc
from dragonfly.engines import (_default_engine)

from castervoice.exclusiveness.globalVariable import GlobalV as gl
from castervoice.exclusiveness.get_AllActiveRules import get_AllActiveRules


def init():
	global data
	data = data_manager()

class data_manager(object):
	# currWindHndl = None
	# prevWindHndl = None
	# _GramName_byGramobj = {} # for the normal grammars (not the CCR merged one, that are autogenerated by caster), the content will be populate at begening, and will remain the same.  # update 20191118233437: instead of using 'Gid_x_Gobj'
	#-- in witch grammar (obect) a rule is in
	""" RuleString could be:
			- a rule name.
			- a rule name class name
			- a rule pronunciation
		"""
	_RuleStringOrObj_byGramobj = {}
	appGramAndRules = {}
	# appExclusiveness = {}
	""" - key  	: @self.currWindHndl
		- value	: instance of class Exclusiveness()
 	 """
	_NotMergedGram_ofCurrAppContext = set() 

	#--- 


	def __init__(self):
		self.currWindHndl = None
		self.prevWindHndl = None
		self._GramName_byGramobj = {} # for the normal grammars (not the CCR merged one, that are autogenerated by caster), the content will be populate at begening, and will remain the same.  # update 20191118233437: instead of using 'Gid_x_Gobj'
		self.appExclusiveness = {}
		

	# @property
	# def appExclusiveness(self):
	# 	"""I'm the 'appExclusiveness' property."""
	# 	print "\n", "dbg20200322145344| getter:", self._appExclusiveness, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

	# 	return self._appExclusiveness

	# @appExclusiveness.setter
	# def appExclusiveness(self, value):
	# 	print "\n", "dbg20200322145345| setter  value :", value, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 	self._appExclusiveness = value

	# @appExclusiveness.deleter
	# def appExclusiveness(self):
	# 	print "\n", "dbg20200322145346| deleter :", self._appExclusiveness, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 	del self._appExclusiveness


	def get_appExclusiveness(self, aWindHndl):
		# print("Getting value")
		# return self.appExclusiveness

		# print "\n", "dbg20200322150522| get |self.appExclusiveness[aWindHndl]:", self.appExclusiveness[aWindHndl], " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		return self.appExclusiveness[aWindHndl]

	# def set_appExclusiveness(self, value):
	def set_appExclusiveness(self, aWindHndl):
		# if value < -273:
		# 	raise ValueError("Temperature below -273 is not possible")
		# print("Setting value")
		# self._appExclusiveness = value

		# print "\n", "dbg20200322150523| set_appExclusiveness.",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		self.appExclusiveness[aWindHndl] = Exclusiveness()

	def del_appExclusiveness(self, aWindHndl):
		# if value < -273:
		# 	raise ValueError("Temperature below -273 is not possible")
		# print("Setting value")
		# self._appExclusiveness = value

		# print "\n", "dbg20200322150523| del_appExclusiveness",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		del self.appExclusiveness[aWindHndl]			


	# appExclusiveness = property(get_appExclusiveness,set_appExclusiveness)

	def populate(self):
		
		for iG in get_engine().grammars:
			self.populate_GramName_byGramobj(iG)
			self.populate_RuleStringOrObj_byGramobj(iG)

	#region--- make a copy of grammars and rules for an App
	# def store_default
	# def makeAcopyOf_NexusMergerRules(self):
	def makeAcopy_engineGrammars(self, aWindHndl):
		#--- (before vers 20200109170619)
		self.appGramAndRules[aWindHndl]._engine_grammars = get_engine().grammars[:]
		# if self.appGramAndRules.has_key(aWindHndl): # (vers 20200109170619)
		# 	self.appGramAndRules[aWindHndl]._engine_grammars = get_engine().grammars[:]
	def putBack_engineGrammars(self, aWindHndl):
		#---add back missing grammar
		engineGramToPutBack = self.appGramAndRules[aWindHndl]._engine_grammars
		self.restore_engineGrammars(engineGramToPutBack)

	#endregion

	def makeAcopy_AllEnabledRule(self, aWindHndl):
		""" reverse of: 'def putBack_AllEnabledRule' """

		if not self.appGramAndRules.has_key(aWindHndl):
			self.appGramAndRules[aWindHndl] = GramAndRules()

		# self.appGramAndRules[aWindHndl]._AllEnabledRule = _NEXUS._grammar_manager._config._config.get_enabled_rcns_ordered()[:]
		# self.appGramAndRules[aWindHndl]._AllEnabledRule = list(_NEXUS._grammar_manager._config._config[RulesConfig._ENABLED_ORDERED])
		self.appGramAndRules[aWindHndl]._AllEnabledRule = gl.RbeenExclusive
		# self.appGramAndRules[aWindHndl]._AllEnabledRule = list(get_AllActiveRules())

		
	def putBack_AllEnabledRule(self, aWindHndl):
		""" reverse of: 'def makeAcopy_AllEnabledRule' """
		print "\n", "20200322125831| TODO: to modif", " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
  		_NEXUS._grammar_manager._config._config[RulesConfig._ENABLED_ORDERED] = list(self.appGramAndRules[aWindHndl]._AllEnabledRule)
		# _NEXUS._grammar_manager._managed_rules = self.appGramAndRules[aWindHndl]._AllEnabledRule.copy()	

	#--- 
	def populate_GramName_byGramobj(self,aGram):
		# return gl.Gid_x_Gobj[Gid[0]]
		# for iG in get_engine().grammars:
		#     print "\n|~20191118231833|aP:", aP, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		
		#-- store >> name
		k = aGram.name if hasattr(aGram,"name") and not aGram.name is None else aGram.__class__.__base__.__name__
		# print "\n|~ici 20191207162421| aGram:", aGram, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		# print "\t|~ici 20191207162421| k:", k, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		self._GramName_byGramobj[k] = aGram
		# print "\n|~ici 20191119092326|self._GramName_byGramobj:", self._GramName_byGramobj, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

		# return 
		# if iG.name == aP:
		#     return iG
		# elif iG.__class__.__base__.__name__ == aP:
		#     return iG
	def populate_RuleStringOrObj_byGramobj(self,aGram):
		# print "\n|~ ici 20191122094851|aGram:", aGram, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

		for iR in aGram.rules:
			# print "\t|~ ici 20191122094852|iR:", iR, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
			
			#-- store >> name
			k = iR.name if hasattr(iR,"name") and not iR.name is None else iR.__class__.__base__.__name__
			self._RuleStringOrObj_byGramobj[k] = aGram
			#-- store >> pronunciation
			k = iR.pronunciation if hasattr(iR, "pronunciation") else None
			if k:
				self._RuleStringOrObj_byGramobj[k] = aGram
			#-- store >> string of Obj
			self._RuleStringOrObj_byGramobj[str(iR)] = aGram
			
	def getGramObjFrmGramStr(self, aGramName):
		""" 
		- aGramName: could be a list or a set, of str of grammar obj.
		"""
		ret = []
		for iGramName in aGramName:
			try:
				ret.append(self._GramName_byGramobj[iGramName])
			except :
				pass
		return ret

	def get_GramObjOf_Rule(self, aRuleString_orObj=[]):
		ret = []
		for iRuleString in aRuleString_orObj:
			# iG = self._RuleStringOrObj_byGramobj[iRuleString]
			try:
				ret.append(self._RuleStringOrObj_byGramobj[iRuleString])
			except:
				print "\n|~!20191121093048|Can Not get the grammar Object. Tips: big chance that the grammar of that rule is not loaded. see vid 20191122093314.",   " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
				print "\t|~!20191121093048a| iRuleString:", iRuleString,   " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
				print "\t|~!20191121093048b| self._RuleStringOrObj_byGramobj:", self._RuleStringOrObj_byGramobj,   " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

				# pass    
			#-- (Tried)            
				# try:
				#     iG = self._RuleStringOrObj_byGramobj[iRuleString]
				#     ret.append(iG)                
				# except:
				#     # from rules.lib import TamFunction as TamFc
				#     from rules.lib.TamFunction import getMergedRules_obj
				#     # retAllCompositeMergedRules, retGrmAndRule = TamFc.getMergedRules_obj()                    
				#     retAllCompositeMergedRules, retGrmAndRule = getMergedRules_obj()                    
				#     # for iR in retGrmAndRule["rule"]:
				#     for iR in retAllCompositeMergedRules:
				#         print "\n|~ici 20191120054313|iRuleString:",iRuleString, "|str(iR):",str(iR), "|iR._get_grammar():",iR._get_grammar() , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

				#         # if iRuleString == iR:
				#         #     iG = iR.grammar
				#         if iRuleString == str(iR):
				#             # MergeRule._get_grammar()
				#             # iG = iR.grammar
				#             # retGrmAndRule["RuleToString_ByGram"][str(iR)]
				#             ret.append(retGrmAndRule["RuleToString_ByGram"][str(iR)])
				#             print "\n|~ici 20191120054313v| in: if iRuleString == str(iR)","|ret:",ret, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
				#             break                      
				#         elif hasattr(iR,"pronunciation") and iRuleString == iR.pronunciation:
				#             # iG = iR.grammar                        
				#             # ret.append(iR.grammar)
				#             ret.append(retGrmAndRule["RuleToString_ByGram"][str(iR)])
				#             break                          
				#         elif hasattr(iR,"name") and iRuleString == iR.name:
				#             # iG = iR.grammar
				#             # ret.append(iR.grammar)
				#             ret.append(retGrmAndRule["RuleToString_ByGram"][str(iR)])
				#             break                       
				#         elif iRuleString == iR.__class__.__name__:
				#             # iG = iR.grammar
				#             # ret.append(iR.grammar)
				#             ret.append(retGrmAndRule["RuleToString_ByGram"][str(iR)])
				#             break                        


			# if not val:
			#     print "\n|~!!!20191204133552|Can Not get the grammar Object.| iRuleString:", iRuleString, "| val:", val,  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
			#     raise ValueError("see 2019120433555")
			# else:
			#     ret.append(val)
			# if iG:
			#     ret.append(iG)
			# else:
			if not ret:
				print "\n|~!!20191120050048|Some Thing wrong? Enable to get the grammar from rule string. |aRuleString_orObj:",aRuleString_orObj , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
				raise ValueError("see 20191120050048")                

		return ret
		
	def checkForNovalide_GramStr(self, aGramStr):
		# type: (list(str)) -> list(str)
		""" return list of bad one """
		# from rules import GlobalV as gl
		ret = []
		# for GramName in gl.gramName_AlwayExclusi:
		for GramName in aGramStr:
			# GramName = iG.name if iG.name else str( iG )
			# FavoriteFolderNonCcr(FavoriteFolderNonCcr)
			# if not self.getGramObjFrmGramStr([GramName]):
			if not self.getGramObjFrmGramStr([GramName, GramName + "(" + GramName + ")"]):
				ret.append(GramName)
				# print "\n|~ The grammar name in the folowing varibale is not valide. Tips: make sure that string is matching with the grammar name (or class name)." , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
				# print "\t|~ Variable name: 'gl.gramName_AlwayExclusi' | GramName: ", GramName , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
				# print "\t|~ get_engine().grammars:", get_engine().grammars , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
				# print "\t|~ _GramName_byGramobj:", self._GramName_byGramobj, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

				# import winsound
				# winsound.PlaySound("C:\\- To Burn\\- Project My\\Sound My\\Alarm09.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
				# # tx = "- The grammar name in the folowing varibale is not valide. Tips: make sure that string is matching with the grammar name (or class name). \
				# #     \n\t- Variable name: 'gl.gramName_AlwayExclusi' | GramName: " + GramName \
				# #     + "\n\t| get_engine().grammars: " + strget_engine().grammars \
				# #     + " \n\t| _GramName_byGramobj: " + self._GramName_byGramobj
				# raise ValueError("(see Print above)")
				# raise ValueError("The grammar name in the folowing varibale is not valide. Tips: make sure that string is matching with the grammar name (or class name) \
				#                  \r\tVariable: gl.gramName_AlwayExclusi| grammar name:", "test")
		return ret

	#--==
	def addNotMergedGram_ofCurrAppContext(self,aGram):
		self._NotMergedGram_ofCurrAppContext.add(aGram)
		
	def getAll_NotMergedGram_ofCurrAppContext(self):
		return self._NotMergedGram_ofCurrAppContext

	#--==
	# def memoriseAppExclusiveness(self,aGram, self.currWindHndl, gl.currAppContext):
	def memoriseAppExclusiveness(self,aGram):
		# from rules import GlobalV as gl
		# from rules.lib import TamFunction as TamFc
		from castervoice.exclusiveness.isMergedGram import isMergedGram

		for iG in aGram:
			#-- Reject/skeep Merged Grammar
			# if TamFc.isMergedGram(iG):
			if isMergedGram(iG):
				continue
	
			# keyAsTup = (gl.currAppContext._executable, gl.currAppContext._title, gl.currAppContext._exclude)
			# if not self.appExclusiveness.has_key(keyAsTup):
			if not self.appExclusiveness.has_key(self.currWindHndl):
				# self.appExclusiveness[keyAsTup] = Exclusiveness(str(iG))
				self.appExclusiveness[self.currWindHndl] = Exclusiveness()
				self.appExclusiveness[self.currWindHndl].addGram(iG)
			else:
				# self.appExclusiveness[(gl.currAppContext._exclude, gl.currAppContext._title, gl.currAppContext._exclude)] = Exclusiveness().addGram(str(aGram))
				self.appExclusiveness[self.currWindHndl].addGram(iG)

		#-- Test:
		# print "\n|~20191204182746| in memoriseAppExclusiveness:", self.appExclusiveness[self.currWindHndl].normalGram, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

	# def unmemoriseAppExclusiveness(self,aGram):
	def unmemoriseAppExclusiveness(self,aGram, aWindHndl = None):
		""" For Curr App """
		if aWindHndl is None:
			WindHndl = self.currWindHndl
		else:
			WindHndl = aWindHndl
		# from rules import GlobalV as gl

		for iG in aGram:

			# #-- if empty add/instatiate 'Exclusiveness' class
		
			# # keyAsTup = (gl.currAppContext._executable, gl.currAppContext._title, gl.currAppContext._exclude)
			# # if not self.appExclusiveness.has_key(keyAsTup):
			# if not self.appExclusiveness.has_key(self.currWindHndl):
			# 	# self.appExclusiveness[keyAsTup] = Exclusiveness(str(aGram))
			# 	self.appExclusiveness[self.currWindHndl] = Exclusiveness(aGram)
			# else:
			# 	# self.appExclusiveness[(gl.currAppContext._exclude, gl.currAppContext._title, gl.currAppContext._exclude)] = Exclusiveness().addGram(str(aGram))
			# 	self.appExclusiveness[self.currWindHndl].addGram(aGram)
			self.appExclusiveness[WindHndl].removeGram(iG)
				# data.appExclusiveness[self.currWindHndl].discard(str(iGram))

		# #-- Test:
		# print "\n|~20191204182746| self.appExclusiveness:", self.appExclusiveness[self.currWindHndl].normalGram, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

	# def memorise_CcrNonGram(self,aGram):
	def memorise_CcrNonGram(self):
		""" For Curr App """
		# self.appExclusiveness[self.currWindHndl].add_CcrNonGram(aGram)
		self.appExclusiveness[self.currWindHndl].add_CcrNonGram()

	def getFrmMemory_CcrNonGram(self, aWindHndl):
		""" return: set(Grammar) """
		return self.appExclusiveness[aWindHndl].CcrNonGram

	#region--- (new caster
	def store_enablebRules_associatedWithApp(self,aWindHndl):
		if not self.appExclusiveness.has_key(self.currWindHndl):
			self.appExclusiveness[self.currWindHndl] = Exclusiveness()
		# 	self.appExclusiveness[aWindHndl].enablebRules_associatedWithApp = list(_NEXUS._grammar_manager._config._config[RulesConfig._ENABLED_ORDERED])
	
		# else:
		#--- TODO: not sure about 'list(_NEXUS._grammar_manager._config._config[RulesConfig._ENABLED_ORDERED])'
		self.appExclusiveness[aWindHndl].enablebRules_associatedWithApp = list(_NEXUS._grammar_manager._config._config[RulesConfig._ENABLED_ORDERED])

	def restore_enablebRules_associatedWithApp(self,aWindHndl):
		if self.appExclusiveness.has_key(aWindHndl):
			return self.appExclusiveness[aWindHndl].enablebRules_associatedWithApp
		else:
			return []
	#endregion (new caster)

	def getAll_normalGram_BeenExclusiv_ofApp(self,aWindHndl):
		if self.appExclusiveness.has_key(aWindHndl):
			return self.appExclusiveness[aWindHndl].normalGram
		else:
			return ()

	def getAll_CcrNonGram_BeenExclusiv_ofApp(self,aWindHndl):
		return self.appExclusiveness[aWindHndl].CcrNonGram

	def getAll_mergedGram_BeenExclusiv_ofApp(self,aWindHndl):
		return self.appExclusiveness[aWindHndl].mergedGram

	def getAll_MergedRule_zip_ofApp(self,aWindHndl):
		""" -> 	{"zipMergedRbyType_z1": MergedRule}
				{"zipMergedRbyType_z2": gl.CcrType}
			"""		
		return self.appExclusiveness[aWindHndl].getAll_MergedRule()

	#--- UML (Uniq Mode Layer)
	def getTop_UML_ofApp(self, aWindHndl):
		return self.appExclusiveness[aWindHndl].getTop_UML()
		# x = []
		# x.
		
	def count_UML_ofApp(self,aWindHndl):
		assert aWindHndl, "param 'aWindHndl' can not be None"
		if self.appExclusiveness.has_key(aWindHndl):
			# print "\n|~ici 20191207172844| self.appExclusiveness[aWindHndl].count_UML():", self.appExclusiveness[aWindHndl].count_UML(), " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
			return self.appExclusiveness[aWindHndl].count_UML()	
		else:
			return 0

	#--== UniqMode history
	def append_UML_ofCurrApp(self,aLayer):
		# from rules import GlobalV as gl

		# if not self.appExclusiveness.has_key(self.currWindHndl):
		# 	self.appExclusiveness[self.currWindHndl] = Exclusiveness()
		# 	self.appExclusiveness[self.currWindHndl].append_UML(aLayer)
		# else:
		# 	self.appExclusiveness[self.currWindHndl].append_UML(aLayer)
		self.appExclusiveness[self.currWindHndl].append_UML(aLayer)

		#-- Test:
		# print "\n|~20191204182746| def append_UML_ofCurrApp| self.appExclusiveness:", self.appExclusiveness[self.currWindHndl], " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

	def pop_UML_ofCurrApp(self):
		# from rules import GlobalV as gl

		return self.appExclusiveness[self.currWindHndl].pop_UML()

	def getAll_UML_ofCurrApp(self):
		# from rules import GlobalV as gl
		# if self.appExclusiveness.has_key(self.currWindHndl)
		return self.appExclusiveness[self.currWindHndl].getAll_UML()
		# else:
		# 	return []

	def restore_engineGrammars(self, aEngineGramToPutBack):
			s1 = set(aEngineGramToPutBack).difference(set(get_engine().grammars))
			# print "\n|~ici 20191216175523| s1:", s1, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
			for iG in s1:
				# print "\n|~ici 20191216180422| adding iG:", iG, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
				get_engine().grammars.append(iG)
			#---remove grammar that wasnt there
			s2 = set(get_engine().grammars).difference(set(aEngineGramToPutBack))
			# print "|~ici 20191216175523b| s2:", s2, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
			for iG in s2:
				# print "\n|~ici 20191216180422b| removing iG:", iG, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
				get_engine().grammars.remove(iG)		
			# return
			# get_engine().grammars = self.appGramAndRules[aWindHndl]._engine_grammars[:] #AttributeError: can't set attribute
		# _default_engine.grammars = self.appGramAndRules[aWindHndl]._engine_grammars[:] #AttributeError: can't set attribute

	# def set_appExclusiveness(data.currWindHndl):
		


	#region--- (No more needed with new Caster)
	# def makeAcopy_NexusMergerGrammars(self, aWindHndl):
	# 	self.appGramAndRules[aWindHndl]._NexusMerger_grammars = _NEXUS.merger._grammars[:]
	# def putBack_NexusMergerGrammars(self, aWindHndl):
	# 	_NEXUS.merger._grammars = self.appGramAndRules[aWindHndl]._NexusMerger_grammars[:]

	# def makeAcopy_NexusMergerConfigs(self, aWindHndl):
	# 	self.appGramAndRules[aWindHndl]._NexusMerger_Configs = _NEXUS.merger._config.copy()	

	# def makeAcopy_NexusMergerRules(self, aWindHndl):
	# 	""" reverse of: 'def putBack_NexusMergerRules' """

	# 	self.appGramAndRules[aWindHndl]._NexusMerger_global_rules = _NEXUS.merger._global_rules.copy()
	# 	self.appGramAndRules[aWindHndl]._NexusMerger_app_rules = _NEXUS.merger._app_rules.copy()
	# 	self.appGramAndRules[aWindHndl]._NexusMerger_self_modifying_rule = _NEXUS.merger._self_modifying_rules.copy()
	# 	# self._NexusMerger_global_with_apps_ = _NEXUS.merger._global_with_apps.copy()	

	# def putBack_NexusMergerRules(self, aWindHndl):
	# 	""" reverse of: 'def makeAcopy_NexusMergerRules' """
	# 	_NEXUS.merger._global_rules = self.appGramAndRules[aWindHndl]._NexusMerger_global_rules.copy()
	# 	_NEXUS.merger._app_rules = self.appGramAndRules[aWindHndl]._NexusMerger_app_rules.copy()
	# 	_NEXUS.merger._self_modifying_rules = self.appGramAndRules[aWindHndl]._NexusMerger_self_modifying_rule.copy()	

	# def putBack_NexusMergerConfigs(self, aWindHndl):
	# 	# if self.appGramAndRules[aWindHndl] != None:
	# 	_NEXUS.merger._config = self.appGramAndRules[aWindHndl]._NexusMerger_Configs.copy()			

	# def memorise_mergedGram_BeenExclusiv(self):
	# 	""" For Curr App """
	# 	from rules.lib import TamFunction as TamFc
	# 	retAllCompositeMergedRules, retGrmAndRule, currMergedCcRule_inf = TamFc.getMergedRules_obj()

	# 	self.appExclusiveness[self.currWindHndl].mergedGram = retGrmAndRule['grammar'].copy()

	# def memorise_MergedRule_zip(self):
	# 	""" For Curr App. 
	# 		Memorise the dictionnary containing those 2 key:value :
	# 	 	{"zipMergedRbyType_z1": MergedRule}
	# 		{"zipMergedRbyType_z2": gl.CcrType}
  	# 	"""		
	# 	from rules.lib import TamFunction as TamFc

	# 	# self.appExclusiveness[self.currWindHndl].add_MergedRule()
	# 	#-- (from 201912-09-02 we dcide to change the way to access varible, after reader some theory about python).
	# 	# self.appExclusiveness[self.currWindHndl]. # type: Exclusiveness
	# 	retAllCompositeMergedRules, retGrmAndRule, currMergedCcRule_inf = TamFc.getMergedRules_obj()
	# 	# Exclusiveness.MergedRule
	# 	self.appExclusiveness[self.currWindHndl].MergedRule = currMergedCcRule_inf.copy() #type: Exclusiveness

	# # def getFrmMemory_MergedRule_zip(self):
	# def getFrmMemory_MergedRule_zip(self, aWindHndl):
	# 	""" For Curr App. 
	# 		Return the dictionnary containing those 2 key:value :
	# 	 	{"zipMergedRbyType_z1": MergedRule}
	# 		{"zipMergedRbyType_z2": gl.CcrType}
  	# 	"""			
	# 	return self.appExclusiveness[aWindHndl].MergedRule

	#endregion (No more needed with new Caster)



class GramAndRules():

	def __init__(self, aGram=None):	
		#--- (new caster)
		self._AllEnabledRule = None

		#--- (old caster)
		self._engine_grammars = None
		self._NexusMerger_grammars = None
		self._NexusMerger_app_rules = None
		self._NexusMerger_global_rules = None
		self._NexusMerger_self_modifying_rule = None
		self._NexusMerger_Configs = None

class Exclusiveness():
	# GramBeenExclusiv = set()
	# GramBeenExclusiv_Merged = set() #Nedd?    
	# def __init__(self, name, description=None, context=None, engine=None):
	
	# GramBeenExclusiv = property(lambda self: self.normalGram, doc="blabla 20191204174517.")
	
	# normalGram = {}
	# normalGram = set()
	""" set of Grammar object  of NO merged Grammar (inOtheWords, doesn't include Grammars in _Nexus.merger._grammars"""
	# _UniqModLayer = []
	# _UniqModLayer = []
	# CcrNonGram = set()
	# mergedGram = set()
	# MergedRule = {}
	""" {"zipMergedRbyType_z1": MergedRule}
		{"zipMergedRbyType_z2": gl.CcrType}
  		"""

	def __init__(self, aGram=None):
		#--- (New Caster)
		self.enablebRules_associatedWithApp = []
  
		#--- (old caster)
		self.normalGram = set()
		self._UniqModLayer = [] #content list of dictionary of uniqMode layer
		self.CcrNonGram = set()
		self.mergedGram = set()
		self.MergedRule = {}		
		# pass
		# if aGram:
		# 	self.addGram(aGram)

	#region --=== history of Uniq Mode
	def append_UML(self, aLayer):
		self._UniqModLayer.append(aLayer)

	def pop_UML(self):
		return self._UniqModLayer.pop()

	def getAll_UML(self):
		return self._UniqModLayer

	def count_UML(self):
		# print "\n|~ici 20191207003726| len(self._UniqModLayer):", len(self._UniqModLayer), " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		return len(self._UniqModLayer)

	def getTop_UML(self):
		if len(self._UniqModLayer) > 0:
			return self._UniqModLayer[len(self._UniqModLayer) - 1]
		else:
			return None

	#--- 
		
	def getAll_MergedRule(self):
		# type: () -> dic
		"""  """
		return self.MergedRule

	# def getAll_CcrNonGram(self):
		# # type: () -> set
		# return self.CcrNonGram
	# # This is how you annotate a function definition
	# def stringify(self, num):
		# # type: (int) -> str
		# """type: (int) -> str 
  		# 	Your function docstring goes here after the type definition."""
		# return str(num)
	#endregion

	#region--- (No more needed with new Caster)
	# #region --=== Merged Grammar
	# def addGram(self, aGram):
	# 	# self.normalGram.append(str(aGram))
	# 	# self.normalGram.add(str(aGram))
	# 	if aGram not in _NEXUS.merger._grammars:
	# 		self.normalGram.add(aGram)

	# def removeGram(self, aGram):
	# 	if aGram not in _NEXUS.merger._grammars:
	# 		self.normalGram.discard(aGram)

	# # def getAllGram(self):
	# 	# return self.normalGram
	# #endregion 		

	# # def add_CcrNonGram(self,aGram):
	# def add_CcrNonGram(self):
	# 	# type: (list[Grammar]) -> None
	# 	# self.CcrNonGram = {s for s in aGram}
	# 	self.CcrNonGram = {s for s in _NEXUS.merger._grammars}	

	# def add_MergedRule(self):
		# from rules.lib import TamFunction as TamFc

		# retAllCompositeMergedRules, retGrmAndRule, currMergedCcRule_inf = TamFc.getMergedRules_obj()
		# self._MergedRule = currMergedCcRule_inf.copy()	
	#endregion (No more needed with new Caster)
