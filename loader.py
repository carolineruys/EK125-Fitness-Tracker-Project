"""loader.py, creating loader file, Caroline Uys. WORKING VERSION."""
def load_tracker_data(filename):
    """Reads the data from the fitness tracker data file and then returns the data as a dictionary of lists.
    Parameters:
        filename ('fitness_data.csv'): 

    Returns:
        A dictionary of the data with the keys being the
        type of data and the values being the data points
        taken each day.

        Example: {
        "day": [1, 2],
        "steps": [8478, 9430],
        "resting_hr": [61, 67],
        "sleep_hours": [8.1, 7.8],
        "active_minutes": [50, 34]
        }
    Side effects: 
    none (does not print or change anything)
    Assumptions and messy cases: 
    Each dictionary key has a value that corresponds to it.
    Days where tracker wasn't worn/working aren't included in 
    the data.
    """
    with open(filename, 'r') as file:
        data_rows = file.readlines()

    keys = data_rows[0].strip().split(',')

    result = {}
    for key in keys:
        result[key] = []

    for line in data_rows[1:]:
        if not line.strip():
            continue
        row = [val.strip() for val in line.strip().split(',')]

        if len(row) != len(keys) or any(val == '' for val in row):
            continue

        for i in range(len(keys)):
            key = keys[i]
            val = row[i]
            result[key].append(val)
    return result

