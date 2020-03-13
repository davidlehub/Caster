import re # regular expression.


def isMergedGram(pGram):
	# if re.match( r'^MergeRule\(Merge', pGram.name):
	if re.match( r'^MergeRule\(Merge', pGram.name if hasattr(pGram, "name") else str(pGram)):
		return True
	else:
		return False
