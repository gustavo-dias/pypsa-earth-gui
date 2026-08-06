"""App's UI folder selector's helpers.

Functions
---------
folder_selector(title: str) -> Path | None
"""

from pathlib import Path
from tkinter import filedialog, Tk
from os.path import expanduser


def folder_selector(title: str) -> Path | None:
   """Get a folder selector with title.
   
   The folder selector is a tkinter window. Returns None in case no folder is
   selected.

   Parameters
   ----------
   title: str
      The title to be displayed in the top of the Tk window.
   
   Returns
   -------
   Path
      The selected folder path.
   None
   """
   root = Tk()
   root.withdraw()
   folder_path = filedialog.askdirectory(
      parent=root,
      title=title,
      mustexist=True,
      initialdir=f'{expanduser("~")}/Documents',  # carefull nested strings
   )
   root.destroy()
   if isinstance(folder_path, str):
      # user selected a folder
      return Path(folder_path)
   else:
      # user did not select a folder and filedialog.askdirectory returned an
      # empty tuple; returning None is this case
      return None
