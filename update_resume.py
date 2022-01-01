import tkinter as tk
from tkinter import filedialog
import os
    
# Import flight data
root = tk.Tk()
root.withdraw()
resume_path = filedialog.askopenfilename(initialdir="~/OneDrive/Documents/Career/Resumes") # Ask user to select data
print('\n\nPath to resume: %s\n' % resume_path)
root.destroy()

os.system("cp {} ./files".format(resume_path))
os.system("git add --all && git commit -a -m'update resume' && git push")