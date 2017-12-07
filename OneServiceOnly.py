
import time
import win32event, pywintypes, win32api

ERROR_ALREADY_EXISTS = 183
sz_mutex = "test_mutex"


hmutex = win32event.CreateMutex(None, pywintypes.FALSE,sz_mutex)
if (win32api.GetLastError() == ERROR_ALREADY_EXISTS):
    print"running..."
    exit(0)
else:
	while 1:
	    time.sleep(1)
	    print "start pppp"