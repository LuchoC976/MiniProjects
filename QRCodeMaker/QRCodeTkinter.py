import tkinter as tk
from tkinter import *
import qrcode
import validators

'''
QRCode Maker Python implementation using qrcode module
and TKinter as the GUI
'''

# Tkinter main window
window = tk.Tk()
window.geometry("300x200")
window.title("QRCode Maker")

window.configure(background = "blue")

# Default URL -> Google.com
defaultURL = "https://www.google.com/"

# getURL function -> validates URL
def getURL():
	url = urlBox.get()
	if len(url) == 0:
		url = defaultURL
	if not validators.url(url):
		url = defaultURL

	# makeQR function called
	makeQR(url)

# makeQR function -> uses qrcode module to make qrcode for a URL
def makeQR(url):
	imgQR = qrcode.make(url)
	imgQR.show()

	# Save IMG checkbox **NOTE: Saving a new img will overwrite the last one**
	if saveImg.get() == 1:
		imgQR.save("MyQRCode")

# Title (Bold, 18px size)
title = tk.Label(window, text = "Convert URL into QRCode:", bg = "blue", 
	fg = "white", pady = 10)
title.configure(font="helvetica 18 bold")
title.pack()

# Prompt
prompt = tk.Label(window, text = "Enter URL:", bg = "blue", 
	fg = "white", pady = 10)
prompt.pack()

# URL string box
urlBox = tk.Entry(window, bg = "blue", fg = "white")
urlBox.pack()

# saveImg -> Checkbutton status validator (selected or not selected)
saveImg = IntVar()
tk.Checkbutton(window, text="Save QRCode", variable = saveImg, pady = 10, bg = "blue", 
	fg = "white", onvalue = 1, offvalue = 0).pack()

# Saves URL and calls getURL function
makeQRBtn = tk.Button(window, text = "Show URL", command = getURL, 
	highlightbackground = "blue", pady = 30)
makeQRBtn.pack()

# Starts tk
window.mainloop()

