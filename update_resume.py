'''
This script updates my resume by prompting the user to select the new resume, then copied it to the files/ directory.
Finally, it adds, commits, and pushes the changes.
'''

import tkinter as tk
from tkinter import filedialog
import os
    
# Select new resume with file explorer dialog 
root = tk.Tk()
root.withdraw()
resume_path = filedialog.askopenfilename(initialdir="~/OneDrive/Documents/Career/Resumes") # Ask user to select data
print('\n\nPath to resume: %s\n' % resume_path)
root.destroy()

# Copy the file to the files/ directory, then add, commit, and push
os.system("cp {} ./files".format(resume_path))
os.system("git add --all && git commit -a -m'update resume' && git push")