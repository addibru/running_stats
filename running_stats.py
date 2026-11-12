

def get_file_data(filename):
    """ Reads the file and saves 

        Parameters:
        filename (str): The name of the file to read
    """
    with open(filename) as file:
        data = file.readlines() # Read the file and get the data
    dates = []
    distances = []
    times = []
    places = []
    races = []
    for line in data:
        data_points = line.split(",")
        date, distance, time, place, race = data_points
        dates.append(date)
        distances.append(distance)
        times.append(time)
        places.append(place)
        races.append(race)



if __name__ == "__main__":
    pass