
from matplotlib import pyplot as plt


class Running_Data:

    class Race: # A class for each race 

        def __int__(self, date, distance, units, time, place, name):
            self.date = date
            self.distance = distance
            self.units = units
            self.time = time
            self.place = place
            self.name = name


    def __init__(self):
        """Initializes the filename as 'None.'"""
        self.filename = None # Filename initialized as 'None'
        self.race_data = [] # Initializes a list of all of the races


    def get_file_data(self):
        """ Reads the file and saves the data into lists that are saved as attributes. These lists include:

            dates (list): A list of the dates of all of the races.
            distances (list): A list of the distances of each race.
            times (list): A list of the chip times of each race.
            places (list): A list of the finishing place of each race.
            races (list): A list of the name of each race.
        """
        while True:
            try:
                self.filename = input("Please enter the filename of the file containing your race data: ")
                with open(self.filename, "r") as file:
                    data = file.readlines() # Read the file and get the data
                    break
            except(OSError): # If the filename is invalid, catch the exception and ask for another one
                print(f"{self.filename} is an invalid filename.")

        # Adds the data from the file to each list
        for line in data:
            data_points = line.split(",")
            date, distance, time, place, name = data_points
            number, units = distance.split()
            new_race = self.Race(date, number, units, time, place, name)
            self.race_data.append(new_race)


    def race_plot(self):
        """
        Plots the race data from recent races.
        """
        if self.filename is None:
            self.get_file_data()
        print("I can plot several different kinds of graphs. Which one would you like to do?")
        print("1. A graph of all of my PRs plotted against the distances.")
        print("2. A graph of all of my races plotted against the distances.")
        print("3. A graph of all times from a certain distance of race plotted against the date.")



if __name__ == "__main__":
    # Initializes the running data class
    user_running_data = Running_Data()
    # Greets the user and lists the things that can be done
    print("Hello! My name is Laney! I can help you analyze different running data! Here are some of the things I can do:")
    print("1. Plot your recent races and show you your trajectory.")
    print("What would you like to do today? Please enter 'exit' to exit.")

    # Gets the action choice from the user
    action = None
    while action != "exit":
        action = input("Please enter the number of the action you would like me to perform: ")
        if action == "1" or action == "1.":
            user_running_data.race_plot()