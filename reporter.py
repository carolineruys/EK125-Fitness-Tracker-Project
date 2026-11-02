"""Reporter module. Report Writer. Nalani Acevedo. STUB VERSION."""

def write_report(results_list, filename):
    """Writes a formatted report to a text file.

    Parameters:
        results_list ([[weekly trends],
        [average for whole month]]):
        filename ('fitness_report.py'):

    Returns:
        None
    Side effects:
        Creates the file filename
        Caution: could overwrite a file if the file has the same name as a pre-existing file

    Example:
        You reached your goal in x/4 of your target areas. Your goals
        were _____, ______, _____, _____. You met these goals: _____,
        _____. Your weekly trends showed ______, _____, ______, ____.
        Your monthly averages were _____, _____, _____, _____.


    Assumptions and messy cases:
    Parameters are given as a dictionary and the filename is different from any other files
    """
    with open(filename, 'w') as report:
        report.write('Fitness Report:\n')
        report.write(
            f'Your goals were {results_list[0]["steps"]["goal"]} steps/day, '
            f'7.5 hours of sleep/night, and 30 active minutes/day.\n'
        )
        report.write(
            f'Your weekly trends showed '
            f'{results_list[0]["step_stats"]["weekly_averages"]}\n'
        )
        report.write(
            f'Your monthly step average was '
            f'{results_list[0]["step_stats"]["monthly_averages"]}\n'
        )
        report.write('Fitness report completed.\n')
