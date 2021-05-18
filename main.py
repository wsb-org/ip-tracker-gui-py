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
Last modified on : May 17, 2021

Changes made in last modification :
1. Changing the font configs for every tkinter widgets like the about window, labels, menubar labels, etc.

Authors contributed to this script (Add your name below if you have contributed) :
1. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

# Importing the required functions and modules
try:
	from json import loads, dumps
	from datetime import datetime
	from urllib import request
	from tkinter import *
	from tkinter import messagebox as mb
except Exception as e:
	# If there are any errors while the importing of modules, then we display the error message on the console screen

	input(f'\n[ Error : {e} ]\nPress enter key to continue...')
	exit()

# The main script starts here

# Defining some properties for the application (tkinter window as well as the entire tool). These properties are declared as a variable with global scope.
# ----
# The list variable which will hold the history logs of all the searches done using the application in the current session. As obvious, the list will be reseted on relaunching this main script. [ Therefore, we need to store the session history to an external file / database in order to store the overall application history ].
session_history = []

# Defining the color scheme property for the tkinter window.
# The color_theme dict currently holds the foreground and background colors for the labels and buttons only. The foreground and background color theme of the buttons are interchanged in the case of active (when cursor is over the button widget, or the button is simply clicked).
color_theme = {
	"foreground" : "white",
	"background" : "black",
	"button_foreground" : "black",
	"button_background" : "white",
}
# ----

# Defining the functions which serves as the commands in the menubar of the tkinter application
# ----
# 1. All the functions are contained inside a class named 'MenubarFunctions' for the sake of collectivity and readablity.
# 2. Each functions may or may not serve multiple tasks (commands). The functions which serves multiple tasks (commands), their tasks are specified through the arguments.
# ----
class MenubarFunctions:
	""" This class contains all the functions which serves the commands at the menubar of the tkinter application. """

	def history(fetch = False, clear = False, session = True):
		""" The function which serves the history related commands in the tools menu of the tkinter application. This function currently serves the tasks : (1) Fetch the current session history, (2) Fetch the overall history, (3) Clear the session history, (4) Clear the overall history. The tasks are specified using the arguments of the function. Below are given proper instructions on how to call the function in order to execute a particular task :

		* To fetch the current session history -> MenubarFunctions.history(fetch = True, session = True)
		* To clear the current session history -> MenubarFunctions.history(clear = True, session = True)
		* To fetch the overall history -> MenubarFunctions.history(fetch = True, session = False)
		* To clear the overall history -> MenubarFunctions.history(clear = True, session = False) 

		Currently, we are displaying the fetch history details on the console screen. """

		# Accessing and configuring the globally accessible variables
		global session_history

		if fetch:
			# If the argument is specified for fetching the history, then we continue to check whether for current session or overall

			if session:
				# If the argument is specified for fetching the history for the current session, then we continue to do so

				print('\n==========[ SESSION HISTORY ]==========')
				if len(session_history) == 0:
					# If the session history data is empty, then we print the empty message

					print('\nThere are no history recorded for the current session.\n')
				else:
					# If the session history data is not empty, then we print the history items (logs) in a loop
				
					for item in session_history:
						# Iterating through each history items

						print(f'[1] IP : {item["ip"]} | Datetime : {datetime.fromtimestamp(item["timestamp"]).ctime()}')
				print('==========[       END       ]==========')
			else:
				# If the argument is specified for fetching the overall history, then we continue to do so

				try:
					# Reading the overall history data from the data.json file
					data = loads(open('data.json', 'r').read())
				except FileNotFoundError:
					# If the data.json file is not found in the project directory, then we continue with a blank file

					data = []
				except Exception as e:
					# If there are any errors encountered during the process, then we display the error to the user

					mb.showerror('Error!', f'{e}')
					return 0

				# If there are no any errors (except FileNotFoundError), then we continue the process
				print('\n==========[ OVERALL HISTORY ]==========')
				if len(data) == 0:
					# If the overall history data is empty, then we print the empty message

					print('\nThere are no history recorded.\n')
				else:
					# If the overall history data is not empty, then we print the history items (logs) in a loop

					for item in data:
						# Iterating through each history items

						print(f'[1] IP : {item["ip"]} | Datetime : {datetime.fromtimestamp(item["timestamp"]).ctime()}')
				print('==========[       END       ]==========')
		elif clear:
			# If the argument is specified for clearing the history, then we continue to check whether for current session or overall

			if session:
				# If the argument is specified for clearing the history for the current session, then we continue to do so

				# Re-declaring the session_history lists as an empty list
				session_history = []
				mb.showinfo('Session history cleared!', 'The session history has been cleared.')
				return 0
			else:
				# If the argument is specified for clearing the overall history, then we continue to do so

				try:
					# Reading the overall history data from the data.json file
					data = loads(open('data.json', 'r').read())

					# Re-defining the overall history as blank and then saving it back to the data.json file
					open('data.json', 'w+').write(dumps([]))
					mb.showinfo('Overall history cleared!', 'The overall history has been cleared.')
					return 0
				except FileNotFoundError:
					# If the data.json file is not found in the project directory, then we continue with a blank file

					data = []
				except Exception as e:
					# If there are any errors encountered during the process, then we display the error to the user

					mb.showerror('Error!', f'{e}')
					return 0
		else:
			# If the argument(s) specfieid does not clarifies whether to fetch history or clear history, then we leave it blank over here

			return 0

	def setColorTheme(foreground = 'white', background = 'black', button_foreground = 'black', button_background = 'white'):
		""" The function which serves the command of changing the color theme of the tkinter application (window and widgets). The user can specify the color formats using the arguments that are taken by this function :
		* foreground -> The foreground color of the widgets like Label, etc.
		* background -> The background color of the widgets like Label, Frame, etc and also the background color of the tkinter windows.
		* button_foreground -> The foreground color for the Button widget. This color swaps for the active background color of the button when active (mouse cursor over the button).
		* button_background -> The background color for the Button widget. This color swaps for the active foreground color of the button when active (mouse cursor over the button).

		The user is provided pre-set color themes by the script, as well as options to custom enter the colors.
		"""

		# Defining the color_theme dictionary (the color property of this tkinter application)
		global color_theme
		color_theme = {
		"foreground" : foreground,
		"background" : background,
		"button_foreground" : button_foreground,
		"button_background" : button_background,
		}

		# Destroying the tkinter windows if they exists
		try:
			win.destroy()
			outputWin.destroy()
		except:
			# If there are errors encountered during the process of destroying the tkinter windows, then we pass it as it may signal that some of the tkinter windows does not exist.

			pass

		# Re-launching the application by recalling the main function
		main()

	def about(tool = False, author = False):
		""" """

		# Declaring an empty variable for storing the contents of the tkinter window as well as another variable for the heading
		text = """"""
		heading = ''

		# Checking the task specified
		if tool:
			# If the function was called to display the about information of the tool, then we continue

			heading = 'About IP-Tracker'
			text = """
This tool serves the feature of fetching information about any public server or computer
device connected to the internet. The tool requires the public IP address of that device.
In order to properly fetch all the required information, the tool needs some of the below
mentioned requirements :
[!] Internet connection
[!] Valid and a public IP address

The tool fetches the information from an external API at the website "http://ipinfo.io/".
Thus, all backend credits goes to the creators and developer of that API, and this tool
just provides an interface to fetch and read the information properly with an ease. The
tool is developed in Python3 programming language. The tool also requires tkinter library
to be installed. Thus, this makes this tool as a GUI application. This tool is also the
GUI adaptation of the CLI tool with same name. For more info check out the docs.
			"""
		elif author:
			# If the function was called to display the about information of the author, then we continue

			heading = 'About the author'
			text = """
This tool is created by Rishav Das (https://github.com/rdofficial/). When the project
was first initialized by the author, means me, I was in high school and the time was
of the lockdown due to COVID-19. Thus, I created many small tools with different
programming languages, and each of the tools serving different features, like this tool
serves the feature of fetching information of an public IP address. I created serveral
command line tools as well as several other graphical versions of those cli tools. The
command line version of the tools are generally stable, light, and can be easily handled
by the user as they do not contain extra functions like color themes or any upper GUI
layer. The projects do not have my own complete credits, many contributions are made by
other developers across the globe. Below are some of my contact details, for further
information or reaching me :
[*] Mail : rdofficial192@gmail.com
[*] Github : rdofficial (http://github.com/rdofficial/)
			"""

		# Defining the tkinter window to display the about information
		aboutWin = Tk()
		aboutWin.title('About - IP-Tracker (Python3)')
		aboutWin.resizable(0, 0)
		aboutWin.config(background = color_theme["background"])

		# Defining the labels for the heading and the content of the tkinter window
		Label(
			aboutWin,
			text = heading,
			font = ('Arial', 15, 'bold', 'italic'),
			foreground = color_theme["foreground"],
			background = color_theme["background"],
			).pack(padx = 5, pady = 5)
		Label(
			aboutWin,
			text = text,
			font = ('Arial', 11,),
			justify = 'left',
			foreground = color_theme["foreground"],
			background = color_theme["background"],
			).pack(padx = 5, pady = 5)

		# Defining the close button for the about window
		Button(
			aboutWin,
			text = 'Close',
			font = ('Arial', 12, 'bold'),
			foreground = color_theme["button_foreground"],
			background = color_theme["button_background"],
			activeforeground = color_theme["button_background"],
			activebackground = color_theme["button_foreground"],
			relief = GROOVE,
			command = aboutWin.destroy,
			).pack(padx = 5, pady = 5)

		mainloop()

	def help(usage = True, documentation = False, report = False):
		pass
# ----

# Re-defining the exit function with some additions
def exit():
	""" The function which serves the command to exit the application and end the script execution. It replaces the built-in function of python i.e., exit(). The function carries the below mentioned changes :
	1. Fetches all the current session history logs and then saves it to the data.json file.
	2. Ends the script execution which eventually closes all the active tkinter windows. This is done as the function calls another built-in python function 'quit()' to end the script execution.

	To use this function, just directly call it. Like : exit. The function does not intakes any arguments. """

	# Saving the current session logs to the overall history logs (data.json file)
	try:
		# First reading the existing contents of the data.json file (the older history logs)
		data = loads(open('data.json', 'r').read())
	except FileNotFoundError:
		# If the data.json file is not found in the current working directory, then we declare the data as a blank list and continue the process

		data = []
	except Exception as e:
		# If there are any other errors encountered during the process, then we display the error to the user

		mb.showerror('Error!', f'{e}')
	finally:
		try:
			# Appending the current session history to the data list object
			for item in session_history:
				data.append(item)

			# Saving the new history data back to the data.json file
			open('data.json', 'w+').write(dumps(data))
		except Exception as e:
			# If there are any other errors encountered during the process, then we display the error to the user

			mb.showerror('Error!', f'{e}')
		finally:
			# After all the steps, wheter errors faced or not. We exit the script
			quit()

def fetchIp(ipAddress):
	""" The function that fetches the required information about the IP address mentioned in the arguments while calling the information and the result (the fetched information about the IP address) is displayed in a new tkinter window. """

	# Making some variables defined inside this function have global access
	global outputWin

	try:
		# Checking the user entered IP address before proceeding
		if len(ipAddress) < 5:
			# If the user entered IP address is less than 5 characters, then we raise the error

			raise SyntaxError(f'Please enter proper IP address for proper search.')

		# Fetching the information about the user entered IP address from the server
		# Sending the POST HTTP request
		response = request.urlopen(f'http://ipinfo.io/{ipAddress}')

		# Checking the response from the server
		if response.status == 200:
			# If the response from the server states no error, then we continue the process

			# Decoding the response from the server and then parsing from JSON format to python object format
			response = response.read().decode()
			response = loads(response)
			text = ''

			# Arranging the output text to be displayed
			for key, value in response.items():
				text += '[#] %-20s   :   %-30s\n' %(str(key).upper(), str(value))

			# Saving the current search to the session history
			session_history.append({
				"ip" : ipAddress,
				"timestamp" : datetime.now().timestamp(),
				})

			# Creating the tkinter window to display the result
			outputWin = Tk()
			outputWin.title('Output - IP Tracker (Python3)')
			outputWin.config(background = color_theme["background"])
			outputWin.resizable(0, 0)  # Making the tkinter window's size to remain fixed, i.e., it cannot change.

			# Definining the heading label and the output label
			Label(
				outputWin,
				text = 'Information fetched',
				foreground = color_theme["foreground"],
				background = color_theme["background"],
				font = ('Arial', 13, 'bold', 'italic'),
				justify = 'left',
				).pack(padx = 5, pady = 5)
			Label(
				outputWin,
				text = text,
				foreground = color_theme["foreground"],
				background = color_theme["background"],
				font = ('Arial', 11, ''),
				justify = 'left',
				).pack(padx = 5, pady = 5)

			# Defining the close button on the output window. This button will destroy / close the output window, when the user clicks it.
			Button(
				outputWin,
				text = 'Close',
				font = ('Arial', 12, 'bold'),
				foreground = color_theme["button_foreground"],
				background = color_theme["button_background"],
				activeforeground = color_theme["button_background"],
				activebackground = color_theme["button_foreground"],
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
	# Making some variables defined inside this function have global access
	global win

	# Defining the main tkinter window
	win = Tk()
	win.title('IP Tracker (Python3)')
	win.resizable(0, 0)
	win.config(background = color_theme["background"])

	# Defining the heading label
	Label(
		win,
		text = 'IP Tracker',
		foreground = color_theme["foreground"],
		background = color_theme["background"],
		font = ('Arial', 15, 'bold', 'italic'),
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
	frame = Frame(win, background = color_theme["background"])
	frame.pack(expand = True, fill = X, padx = 5, pady = 10)

	# Defining the inner contents of the frame, i.e., the form elements (Label, and entry box)
	Label(
		frame,
		text = 'Enter the IP address of target',
		foreground = color_theme["foreground"],
		background = color_theme["background"],
		font = ('Arial', 12),
		).pack(side = LEFT, padx = 5, pady = 5)
	Entry(
		frame,
		textvariable = ipAddress,
		font = ('Arial', 12),
		).pack(side = RIGHT, padx = 5, pady = 5)

	# Defining the continue button widget
	Button(
		win,
		text = 'Continue',
		font = ('Arial', 12, 'bold'),
		foreground = color_theme["button_foreground"],
		background = color_theme["button_background"],
		activeforeground = color_theme["button_background"],
		activebackground = color_theme["button_foreground"],
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
	toolsmenu = Menu(menubar, font = ('Arial', 11), tearoff = 0)
	menubar.add_cascade(label = 'Tools', font = ('Arial', 11), menu = toolsmenu)  # Configuring the toolsmenu with the main menubar
	toolsmenu.add_command(label = 'Session history', command = lambda : MenubarFunctions.history(fetch = True, session = True))
	toolsmenu.add_command(label = 'Clear session history', command = lambda : MenubarFunctions.history(clear = True, session = True))
	toolsmenu.add_command(label = 'Overall history', command = lambda : MenubarFunctions.history(fetch = True, session = False))
	toolsmenu.add_command(label = 'Clear Overall history', command = lambda : MenubarFunctions.history(clear = True, session = False))
	toolsmenu.add_separator()
	#
	# Defining the colors sub-menu for the toolsmenu (This menu will show as a side menu in the tools menu and displays the list of the colors themes available for the tkinter window).
	colorsmenu = Menu(toolsmenu, font = ('Arial', 11), tearoff = 0)
	toolsmenu.add_cascade(label = 'Color Themes', menu = colorsmenu)  # Configuring the colorsmenu with the toolsmenu
	colorsmenu.add_command(label = 'Default', command = lambda : MenubarFunctions.setColorTheme(foreground = 'white', background = 'black', button_foreground = 'black', button_background = 'white'))
	colorsmenu.add_command(label = 'Tkinter Original', command = lambda : MenubarFunctions.setColorTheme(foreground = 'black', background = None, button_foreground = None, button_background = None))
	colorsmenu.add_command(label = 'Black-White', command = lambda : MenubarFunctions.setColorTheme(foreground = 'black', background = 'white', button_foreground = 'white', button_background = 'black'))
	colorsmenu.add_command(label = 'Green-Black', command = lambda : MenubarFunctions.setColorTheme(foreground = 'green', background = 'black', button_foreground = 'black', button_background = 'green'))
	colorsmenu.add_command(label = 'Red-Black', command = lambda : MenubarFunctions.setColorTheme(foreground = 'red', background = 'black', button_foreground = 'black', button_background = 'red'))

	# Defining the helpmenu
	helpmenu = Menu(menubar, font = ('Arial', 11), tearoff = 0)
	menubar.add_cascade(label = 'Help', font = ('Arial', 11), menu = helpmenu)  # Configuring the colorsmenu with the toolsmenu
	helpmenu.add_command(label = 'Documentation', command = None)
	helpmenu.add_command(label = 'About the author', command = lambda : MenubarFunctions.about(author = True))
	helpmenu.add_command(label = 'Report a bug', command = None)
	helpmenu.add_separator()
	helpmenu.add_command(label = 'About IP Tracker', command = lambda : MenubarFunctions.about(tool = True))
	helpmenu.add_command(label = 'Usage', command = None)

	# Defining the exit command on the menubar
	menubar.add_command(label = 'Exit', font = ('Arial', 11), command = exit)
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