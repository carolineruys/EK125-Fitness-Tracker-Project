"""loader.py, creating loader file, Caroline Uys. WORKING VERSION."""
def load_tracker_data(filename):
    """Reads the data from the fitness tracker data file and then returns the data as a dictionary of lists."""
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

def test_loader(tester):
    """Tests the loader function."""
    print(type(tester))
    print(tester.keys())
    print(tester)
    for value in tester.values():
        print(len(value))

result = load_tracker_data('fitness_data.csv')
test_loader(result)
