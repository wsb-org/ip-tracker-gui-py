"""
IP Tracker [GUI, Python3]

This is the graphical version of the IP Tracker tool, the features provided by this tool are same as its original version.

Dependencies :
1. tkinter - A python3 module / framework used to create GUI widgets and windows.

Usage :
1. First clone the repository from github mirror of it, using the command 'git clone https://github.com/wsb-org/ip-tracker-gui-py' [Type these commands in the terminal].
2. Use this command to install the dependencies (Take a look at the README file for more info).
3. Run the script using these commands - 'python3 main.py'

Author : Rishav Das (https://github.com/rdofficial/)
Created on : May 16, 2021

Last modified by : Rishav Das (https://github.com/rdofficial/)
Last modified on : May 16, 2021

Changes made in last modification :
1. Added the features of menubars, and their respective sub-menus but not added the commands for the menus.

Authors contributed to this script (Add your name below if you have contributed) :
1. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

# Importing the required functions and modules
try:
	from requests import get
	from tkinter import *
	from tkinter import messagebox as mb
except Exception as e:
	# If there are any errors while the importing of modules, then we display the error message on the console screen

	input(f'\n[ Error : {e} ]\nPress enter key to continue...')
	exit()

# The main script starts here

def fetchIp(ipAddress):
	""" The function that fetches the required information about the IP address mentioned in the arguments while calling the information and the result (the fetched information about the IP address) is displayed in a new tkinter window. """

	try:
		# Checking the user entered IP address before proceeding
		if len(ipAddress) < 5:
			# If the user entered IP address is less than 5 characters, then we raise the error

			raise SyntaxError(f'Please enter proper IP address for proper search.')

		# Fetching the information about the user entered IP address from the server
		# Sending the POST HTTP request
		response = get(f'http://ipinfo.io/{ipAddress}')

		# Checking the response from the server
		if response.status_code == 200:
			# If the response from the server states no error, then we continue the process

			response = response.json()
			text = ''

			# Arranging the output text to be displayed
			for key, value in response.items():
				text += '[#] %-20s   :   %-30s\n' %(str(key).upper(), str(value))

			# Creating the tkinter window to display the result
			outputWin = Tk()
			outputWin.title('Output - IP Tracker (Python3)')
			outputWin.config(background = 'black')
			outputWin.resizable(0, 0)  # Making the tkinter window's size to remain fixed, i.e., it cannot change.

			# Definining the heading label and the output label
			Label(
				outputWin,
				text = 'Information fetched',
				foreground = 'white',
				background = 'black',
				font = ('', 13, 'bold', 'italic'),
				justify = 'left',
				).pack(padx = 5, pady = 5)
			Label(
				outputWin,
				text = text,
				foreground = 'white',
				background = 'black',
				font = ('', 11, ''),
				justify = 'left',
				).pack(padx = 5, pady = 5)

			# Defining the close button on the output window. This button will destroy / close the output window, when the user clicks it.
			Button(
				outputWin,
				text = 'Close',
				font = ('', 12, 'bold'),
				foreground = 'black',
				background = 'white',
				activeforeground = 'white',
				activebackground = 'black',
				relief = GROOVE,
				command = outputWin.destroy,
				).pack(padx = 5, pady = 10)

			mainloop()
		else:
			# If the response fromthe server states error, then we display the error message to the user

			mb.showerror(f'{response.json()["error"]["title"]}', f'{response.json()["error"]["message"]}')
			return 0

	except Exception as e:
		# If there are any errors encountered during the process, then we display the error message to the user

		mb.showerror('Error!', f'{e}')
		return 0

def main():
	# Defining the main tkinter window
	win = Tk()
	win.title('IP Tracker (Python3)')
	# win.geometry('400x400')
	win.resizable(0, 0)
	win.config(background = 'black')

	# Defining the heading label
	Label(
		win,
		text = 'IP Tracker',
		foreground = 'white',
		background = 'black',
		font = ('', 15, 'bold', 'italic'),
		).pack(padx = 5, pady = (10, 20))

	# Defining the input box form for the user to enter the IP address
	# ----
	# 1. We will inlcude the form inside a tkinter Frame widget with variable name 'frame'.
	# 2. We will define a label asking the user to enter the IP address of the target, and an Entrybox widget for the user to enter the value of IP address.
	# 3. We will use a textvariable 'ipAddress' with String type to store the user entered input.
	# 4. The continue button will be placed outside the frame.
	# ----
	ipAddress = StringVar(win)

	# Defining the frame to contain the form elements
	frame = Frame(win, background = 'black')
	frame.pack(expand = True, fill = X, padx = 5, pady = 10)

	# Defining the inner contents of the frame, i.e., the form elements (Label, and entry box)
	Label(
		frame,
		text = 'Enter the IP address of target',
		foreground = 'white',
		background = 'black',
		font = ('', 12),
		).pack(side = LEFT, padx = 5, pady = 5)
	Entry(
		frame,
		textvariable = ipAddress,
		font = ('', 12),
		).pack(side = RIGHT, padx = 5, pady = 5)

	# Defining the continue button widget
	Button(
		win,
		text = 'Continue',
		font = ('', 12, 'bold'),
		foreground = 'black',
		background = 'white',
		activeforeground = 'white',
		activebackground = 'black',
		relief = GROOVE,
		command = lambda : fetchIp(ipAddress.get())
		).pack(padx = 5, pady = 10)
	# ----

	# Defining the menubar of the tkitner window
	# ----
	# 1. We will define a main menubar, which will contain all the sub-menus like toolsmenu, helpmenu, etc.
	# 2. Further more we will separate commands in each menu using the separator.
	# 3. Also there will be another sub-menus in each menu for making the commands more grouped. Like colorsmenu.
	# ----
	menubar = Menu(win)
	win.config(menu = menubar)  # Configuring the main tkinter window to use the menubar

	# Defining the toolsmenu
	toolsmenu = Menu(menubar, font = ('', 10), tearoff = 0)
	menubar.add_cascade(label = 'Tools', menu = toolsmenu)  # Configuring the toolsmenu with the main menubar
	toolsmenu.add_command(label = 'History', command = None)
	toolsmenu.add_command(label = 'Clear history', command = None)
	toolsmenu.add_separator()
	#
	# Defining the colors sub-menu for the toolsmenu (This menu will show as a side menu in the tools menu and displays the list of the colors themes available for the tkinter window).
	colorsmenu = Menu(toolsmenu, font = ('', 10), tearoff = 0)
	toolsmenu.add_cascade(label = 'Color Themes', menu = colorsmenu)  # Configuring the colorsmenu with the toolsmenu
	colorsmenu.add_command(label = 'Default', command = None)
	colorsmenu.add_command(label = 'Tkinter Original', command = None)
	colorsmenu.add_command(label = 'Black-White', command = None)
	colorsmenu.add_command(label = 'Green-Black', command = None)
	colorsmenu.add_command(label = 'Red-Black', command = None)

	# Defining the helpmenu
	helpmenu = Menu(menubar, font = ('', 10), tearoff = 0)
	menubar.add_cascade(label = 'Help', menu = helpmenu)  # Configuring the colorsmenu with the toolsmenu
	helpmenu.add_command(label = 'Documentation', command = None)
	helpmenu.add_command(label = 'About the author', command = None)
	helpmenu.add_command(label = 'Report a bug', command = None)
	helpmenu.add_separator()
	helpmenu.add_command(label = 'About IP Tracker', command = None)
	helpmenu.add_command(label = 'Help', command = None)
	# ----

	mainloop()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		# If the user presses CTRL+C key combo, then we exit

		exit()
	except Exception as e:
		# If any errors encountered during the process, then we display the error message on the console screen

		input(f'\n[ Error : {e} ]\nPress enter key to continue...')