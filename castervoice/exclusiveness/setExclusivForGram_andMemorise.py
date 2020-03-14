from castervoice.exclusiveness.globalVariable.Data_Manager import data
from castervoice.exclusiveness.enableR import enableR


# def setExclusivForGram_andMemorise(aGram):
def setExclusivForGram_andMemorise(aRules):
	"""	aRules: LIST 
		"""
	enableR(aRules)
	# data.memoriseAppExclusiveness(aRules) #replaced by 'gl.RbeenExclusive.append()'
