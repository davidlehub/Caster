from operator import attrgetter


class ExclusivMode_cls(object):

    def __init__(self):
        # self.enabled = True
        self._enabled = True
        # self.disabled = True
        self.enabledApplicant = None

    enabled = property(attrgetter("_enabled")) #read only, use 'set_enabled' to write.

    def set_enabled(self,b, apl):
        if b:
            self._enabled = True
            # self.enabledApplicant = apl
        else:
            self._enabled = False
            # self.disabled = True
            # self.disabledApplicant = apl
        self.enabledApplicant = apl

ExclusivMode = ExclusivMode_cls()
