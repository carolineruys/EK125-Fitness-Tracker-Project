"""loader.py, creating loader file, Caroline Uys. WORKING VERSION."""
def load_tracker_data(filename):
    """Reads the data from the fitness tracker data file and then returns the data as a dictionary of lists."""
    data_rows = filename.readlines()
    keys = data_rows[0]
    rows = data_rows[1:]
    result = {}
    for key in keys:
        result[key] = []
    for row in rows:
        for i in range(len(keys)):
            key = keys[i]
            val = row[i]
            result[key].append(val)
    return result
def test_loader(tester):
    """Tests the loader function."""
    print(type(tester))
    print(tester.keys())

result = load_tracker_data()
test_loader(result)
