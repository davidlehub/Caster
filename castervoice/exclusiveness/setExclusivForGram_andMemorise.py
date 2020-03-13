from castervoice.exclusiveness.globalVariable.Data_Manager import data
from castervoice.exclusiveness.enableR import enableR


def setExclusivForGram_andMemorise(aGram):
	"""	aGram: LIST of not merged gramar object	
		"""
	enableR(aGram)
	data.memoriseAppExclusiveness(aGram)
