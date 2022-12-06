from tkinter import *

# Program name:       Average MPG and Total Gas Cost Calculator
# Author:             Charles Phillips
# Version:            version 1.0
# Last revision date: 12/5/2022
# The objective of this program is to prompt a user to enter the demographics of a car such as year, make and model,
# and then generate the calculated average MPG of a car to determine the amount of gas money spent.
# Finally, it records the results to a file.


class UIWindow:  # This launches the instance of the program window
    def __init__(self, window):  # This function initializes the program window.
        self.lbl1 = Label(window, text='Please enter the year, make and model of a car. ')
        self.lbl1.place(x=0, y=50)
        self.carInfo = Entry(bd=3)   # This creates an entry field for the car demographics
        self.carInfo.place(x=260, y=50)    # This is the coordinate to place the input box
        self.lbl2 = Label(window, text='How many miles did you drive? ')
        self.lbl2.place(x=0, y=100)
        self.milesDriven = Entry(bd=3)   # bd=3 creates a 3d border outline around the input box
        self.milesDriven.place(x=180, y=100)
        self.lbl3 = Label(window, text='What is the current price of gas per gallon? ')
        self.lbl3.place(x=0, y=150)
        self.gasPrice = Entry(bd=3)
        self.gasPrice.place(x=230, y=150)
        self.lbl4 = Label(window, text='How many gallons of gas were used? ')  # Used as a user prompt
        self.lbl4.place(x=0, y=200)
        self.resultHeader = Label(window, text='Program results:')   # Header for outputted program results
        self.resultHeader.place(x=225, y=300)
        self.gasUsed = Entry(bd=3)
        self.gasUsed.place(x=200, y=200)

        self.avgMpgLbl = Label(window, text=f'Avg Mpg: ')   # Holder for describing the received output results
        self.avgMpgLbl.place(x=380, y=325)
        self.totalAvgMpg = Entry(bd=3)
        self.totalAvgMpg.place(x=450, y=325)

        self.gasPaidLbl = Label(window, text=f'Total cost in gas $: ')
        self.gasPaidLbl.place(x=340, y=375)
        self.totalGasPaid = Entry(bd=3)
        self.totalGasPaid.place(x=450, y=375)
# Button for calculating the total average mpg and the amount of money spent in gas for a trip.
        self.btn1 = Button(window, text='Calculate Avg Mpg and amount gas spent for this trip', command=self.calc_data)
        self.btn1.place(x=100, y=250)

    # This function is used to calculate the total average mpg and the amount of money spent in gas.
    def calc_data(self):
        self.totalAvgMpg.delete(0, 'end')  # This clears previous input
        self.totalGasPaid.delete(0, 'end')
        milesDriven = int(self.milesDriven.get())   # This grabs the variables needed for the program to run
        gasPrice = int(self.gasPrice.get())
        gasUsed = int(self.gasUsed.get())
        avgMpg = int(milesDriven / gasUsed)  # Mathematical formula for calculating average MPG
        amountSpent = int(milesDriven / avgMpg) * gasPrice   # This plugs in the previous avgMpg to calculate how
        # much money in gas was spent.
        self.totalAvgMpg.insert(END, str(avgMpg))
        self.totalGasPaid.insert(END, str(amountSpent))


window_container = Tk()  # This creates a tkinter program window instance
window_instance = UIWindow(window_container)  # Creates a new window
window_container.title('Average MPG and Total Gas Cost Calculator')
window_container.geometry("600x400+20+20")  # Sets the total size of the program window
window_container.mainloop()
