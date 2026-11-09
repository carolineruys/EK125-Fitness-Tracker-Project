"""Reporter module. Report Writer. Nalani Acevedo."""

def write_report(results_list, filename):
    """Writes a formatted report to a text file.

    Parameters:
        results_list (list): List of dictionaries returned by analyze_metric.
        filename (str): Name of the output text file.

    Returns:
        None

    Side effects:
        Creates the file filename.
    """

    # Combine the dictionaries into one dictionary for easier access
    all_stats = {}
    for result in results_list:
        if isinstance(result, list):
            for item in result:
                all_stats.update(item)
        else:
            all_stats.update(result)

    with open(filename, 'w') as report:
        report.write('Fitness Report:\n')
        report.write('--------------------------\n')

        report.write(
            f'Your goals were {all_stats["steps_stats"]["goal"]} steps/day, '
            f'{all_stats["rest_stats"]["goal"]} bpm resting heart rate, '
            f'{all_stats["sleep_stats"]["goal"]} hours of sleep/night, and '
            f'{all_stats["active_stats"]["goal"]} active minutes/day.\n\n'
        )

        report.write('Weekly Trends:\n')

        report.write(
            f'Weekly step averages: '
            f'{all_stats["steps_stats"]["weekly_averages"]}\n'
        )

        report.write(
            f'Weekly resting heart rate averages: '
            f'{all_stats["rest_stats"]["weekly_averages"]}\n'
        )

        report.write(
            f'Weekly sleep averages: '
            f'{all_stats["sleep_stats"]["weekly_averages"]}\n'
        )

        report.write(
            f'Weekly active minute averages: '
            f'{all_stats["active_stats"]["weekly_averages"]}\n\n'
        )

        report.write('Monthly Averages:\n')

        report.write(
            f'Monthly step average: '
            f'{all_stats["steps_stats"]["monthly_average"]}\n'
        )

        report.write(
            f'Monthly resting heart rate average: '
            f'{all_stats["rest_stats"]["monthly_average"]}\n'
        )

        report.write(
            f'Monthly sleep average: '
            f'{all_stats["sleep_stats"]["monthly_average"]}\n'
        )

        report.write(
            f'Monthly active minute average: '
            f'{all_stats["active_stats"]["monthly_average"]}\n\n'
        )

        report.write('Best Days:\n')

        report.write(
            f'Best step day(s): {all_stats["steps_stats"]["best_days"]} '
            f'({all_stats["steps_stats"]["best_value"]} steps)\n'
        )

        report.write(
            f'Best resting heart rate day(s): {all_stats["rest_stats"]["best_days"]} '
            f'({all_stats["rest_stats"]["best_value"]} bpm)\n'
        )

        report.write(
            f'Best sleep day(s): {all_stats["sleep_stats"]["best_days"]} '
            f'({all_stats["sleep_stats"]["best_value"]} hours)\n'
        )

        report.write(
            f'Best active minute day(s): {all_stats["active_stats"]["best_days"]} '
            f'({all_stats["active_stats"]["best_value"]} minutes)\n\n'
        )

        report.write('Goal Progress:\n')

        for metric, name in [
            ("steps_stats", "Steps"),
            ("rest_stats", "Resting heart rate"),
            ("sleep_stats", "Sleep"),
            ("active_stats", "Active minutes")
        ]:
            if all_stats[metric]["goal_met"]:
                report.write(f'{name}: Goal met!\n')
            else:
                report.write(f'{name}: Goal not met.\n')

        report.write('\nFitness report completed.\n')
