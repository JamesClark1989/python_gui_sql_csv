#--------------------------------------------------------------------#
#
# Staff Directory Front-End
#
# This is the front-end of the staff directory application. It
# creates a Graphical User Interface which can be used with any
# of the back-end functions.
#
# To complete this exercise you need to work with your teammates
# to decide who will implement the front-end GUI and who will
# implement the back-end look-up function. You need to agree on
# the signature of this function so that both teams can work
# independently, i.e., what parameter(s) does the function accept
# and what format does it return the search results in?
#
# Below is some skeletal code to help you get started on the
# front-end, but feel free to design whatever GUI you want to
# do the job.  
#

# Import the Tkinter functions
from tkinter import *

# Import the back-end function developed by the other team
import backend_function


#--------------------------------------------------------------------#
# Define a function here to serve as the "command" when the user
# initiates a search.  It should:
#
# 1) get the employee name entered by the user;
# 2) call the back-end function to get the search results; and
# 3) display the results in the GUI.
#
def search_name():
    results_window.delete('1.0', END)
    search_term = name_entry.get()
    if search_term == '':
        results_window.insert(END, "Please type a name")
    else:        
        results = backend_function.find_employee(search_term)
        for re in range(len(results)):
            num = results[re][0]
            first = results[re][1]
            last = results[re][2]
            dob = results[re][3]
            results_window.insert(END, "{}: {} {} ({})\n".format(num,first,last,dob))

def search_name_csv():
    results_window.delete('1.0', END)
    search_term = name_entry.get()
    if search_term == '':
        results_window.insert(END, "Please type a name")
    else:  
        employee_data = backend_function.find_employee_csv(search_term)
        for employee in employee_data:
            num = employee[0]
            first = employee[2]
            last = employee[3]
            dob = employee[1]
            results_window.insert(END, "{}: {} {} ({})\n".format(num,first,last,dob))
            

        
#----------------------------------------------------------------#
# The GUI front end
#

# Create a window
staff_window = Tk()

# Give the window a title
staff_window.title('Staff Directory')

# Create a Text widget to display the results
results_window = Text(staff_window, width = 50)
results_window.grid(column = 0, row = 1)

# Create a text Entry widget for entering the employee name
name_entry = Entry(staff_window,width = 30)
name_entry.grid(column = 0, row = 2)

# Create a Button widget to start the search
search_button = Button(staff_window, text = "Find Employees", width = 20,
                       command = search_name)
search_button.grid(column = 0, row = 3)

search_button_csv = Button(staff_window, text = "Find Employees CSV", width = 20,
                       command = search_name_csv)
search_button_csv.grid(column = 0, row = 4)

# Optional: Create any other widgets you want to make
# the GUI look nice, such as Labels for instructions or
# to display an image
label = Label(staff_window, text = "Find employees", font=('Arial', 20))
label.grid(column=0, row=0)

choices = {'poo', 'wee', 'bum'}
tkvar = StringVar(staff_window)
tkvar.set('poo')
popup = OptionMenu(staff_window, tkvar, *choices)
popup.grid(column = 0, row = 5)

# Start the event loop
staff_window.mainloop()

#
#--------------------------------------------------------------------#

