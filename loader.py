"""loader.py, creating loader file, Caroline Uys. STUB VERSION."""
def load_tracker_data():
    """Reads the data from the fitness tracker data file and then returns the data as a dictionary of lists."""
    #data_rows = reads the csv file line by line and puts them into lists - will use the readlines() function
    #using indexing and for loops to sort the elements of data_rows into the new lists for the dictionary
    result = {"day": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
            "steps": [8478, 9430, 6970, 4569, 121992, 7640, 9060, 5310, 0, 7419, 5917, 5068, 12101, 9837, 8477, 8354, 8962, 9423, 5274, 8935, 8727, 10409, 0, 7373, 12139, 10483, 14773, 12726],
            "resting_hr": [61, 67, 67, 59, 66, 62, 65, 62, 0, 60, 64, 65, 67, 58, 62, 63, 64, 65, 63, 64, 61, 62, 0, 60, 66, 61, 62, 63],
            "sleep_hours": [8.1, 7.8, 6.4, 7.7, 7.6, 6.9, 8.9, 7.7, 7.6, 6.9, 8.9, 7.7, 5.6, 5.7, 6.9, 6.1, 8, 7.3, 7.5, 7.4, 0, 6.6, 6.3, 7.1, 6.3, 8.4, 7.8, 7.3, 6.3, 8.4, 6.7],
            "active_minutes": [50, 34, 52, 21, 38, 43, 69, 52, 0, 39, 45, 19, 60, 46, 61, 44, 65, 18, 41, 38, 27, 49, 0, 16, 29, 54, 41, 48]
            }
    return result
def test_loader(tester):
    """Tests the loader function."""
    print(type(tester))
    print(tester.keys())

result = load_tracker_data()
test_loader(result)