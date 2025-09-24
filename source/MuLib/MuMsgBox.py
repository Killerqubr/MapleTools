from PyQt5.QtWidgets import QMessageBox
import sys

class MuMessageBox:

    @staticmethod
    def Critical(parent, version:str, title="MapleUI Fatal Error", ErrorMsg=None, Preset=None, info=None):
        if Preset != None:
            try:
                ErrorMsg = {FileNotFoundError: f'The following Missing files/folders are Program required: \n       {info}'}[Preset]
            except KeyError:
                pass
        QMessageBox.critical(parent, title,
f"""MapleUI has Crashed.
You can report the issues on offical Github Page with accurate description and screen-shots:
https://github.com/Killerqubr/MapleUI

Internal Version:  {version}
{"-"*(len(ErrorMsg)//4)} Error Message {"-"*(len(ErrorMsg)//4)}
{ErrorMsg}""")
        return sys.exit()