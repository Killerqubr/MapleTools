from PyQt5.QtWidgets import QMessageBox
import sys

class MtMessageBox:

    @staticmethod
    def Critical(parent, version:str, title="MapleTools Fatal Error", ErrorMsg=None, Preset=None, info=None):
        if Preset != None:
            try:
                ErrorMsg = {FileNotFoundError: f'The following Missing files/folders are Program Required: {info}'}[Preset]
            except KeyError:
                pass

        QMessageBox.critical(parent, title,
f"""Maple Tools has Crashed.
You can check the Log files for the Exact Error or Report it on Project's Github Pages.
Maple Tools Version:  {version}

Error Type:  {Preset.__qualname__}
Error Message:
        {ErrorMsg}""")
        return sys.exit()