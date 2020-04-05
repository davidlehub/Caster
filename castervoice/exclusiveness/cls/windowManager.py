from operator import attrgetter
import re # regular expresinn.
import win32gui


class windowManager_cls(object):


    def __init__(self):
        # self.previous = {}
        self.previousTitle = None
        self.Hnd_theOneBeforeDragonDictBox = None
        # self._handle = None
    def currentIs_DragonDictBox(self,activeWinHnd):
        '''
            <-bool.
        '''
        activeWinClassName = win32gui.GetClassName(activeWinHnd)
        if activeWinClassName == "DgnDictationBoxCls": #(becarefull aout active wintitle and active process name: see vid 20181202150450)
            self.Hnd_theOneBeforeDragonDictBox = activeWinHnd
            return True
        else:
            return False

    # def previousWas_DragonDictBox(self,activeWinHnd):
    def CurrentIs_theOneBeforeDragonDictBox(self,activeWinHnd):
        '''
            <-bool.
        '''
        # elif activeWinHnd == gl.ForgrnWind_BforeCalng_DgnDictationBox:

        # if win32gui.GetClassName(previousWinHnd) == "DgnDictationBoxCls":
        # if self.previousClass == "DgnDictationBoxCls":
        if activeWinHnd == self.Hnd_theOneBeforeDragonDictBox:
            return True #(becarefull aout active wintitle and active process name: see vid 20181202150450)
        else:
            return False

    #-----
    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        # self._handle = win32gui.FindWindow(class_name, window_name)
        return win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            # self._handle = hwnd
            return hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        # self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    # def set_foreground(self):
    def set_foreground(self, WinHnd):
        """put the window in the foreground"""
        # win32gui.SetForegroundWindow(self._handle)
        win32gui.SetForegroundWindow(WinHnd)

    #-----

win = windowManager_cls()
