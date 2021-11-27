import sys

class OsPlatformMixin:
    OS_X = ['os2', 'darwin', 'os2emx']
    LINUX = ['linux', 'linux2']
    WINDOWS = ['win32', 'cygwin', 'msys']

    def get_correct_slash(self):
        if sys.platform in self.OS_X or sys.platform in self.LINUX:
            return '/'
        elif sys.platform in self.WINDOWS:
            return '\\'
        else:
            print('файловая система не обнаружена, может быть проблема с путями')
            sys.exit(0)
