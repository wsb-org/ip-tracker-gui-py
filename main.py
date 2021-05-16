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

Last modified by : -
Last modified on : -

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
		# Fetching the information about the user entered IP address from the server
		# Sending the POST HTTP request
		response = get(f'http://ipinfo.io/{ipAddress}')
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

		mainloop()

	except Exception as e:
		# If there are any errors encountered during the process, then we display the error message to the user

		mb.showerror('Error!', f'{e}')
		return 0