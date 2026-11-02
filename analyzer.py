"""Analyzer module. Report Writer. Isabella Rodriguez."""
def analyze_metric(data, metric, goal, higher_is_better=True):
    """Calculates statistics for one metric and returns them in a dictionary.

    Parameters:
        data (dict of lists): the dictionary returned by load_tracker_data.
            Keys are "day", "steps", "resting_hr", "sleep_hours",
            "active_minutes"; each value is a list with one number per day.
            Example: {"day": [1, 2], "steps": [8478, 9430], ...}
        metric (str): the column to analyze: "steps", "resting_hr",
            "sleep_hours", or "active_minutes"
        goal (int or float): the daily target for this metric, in the
            metric's units (steps, bpm, hours, or minutes). Example: 8000
        higher_is_better (bool): True if a value at or above the goal is
            good (steps, sleep, active minutes). False if a value at or
            below the goal is good (resting heart rate). Default True.

    Returns:
        dict with ONE key, chosen from the metric:
            "steps" -> "steps_stats", "resting_hr" -> "rest_stats",
            "sleep_hours" -> "sleep_stats", "active_minutes" -> "active_stats"
        Its value is a dictionary with these keys:
            "goal" (float): the goal that was passed in
            "weekly_averages" (list of 4 floats): average for days 1-7,
                8-14, 15-21, and 22-28 (None if a week has no data)
            "monthly_average" (float): average of every day with data
            "goal_met" (bool): True if the monthly average meets the goal
            "best_days" (list of ints): day number(s) with the best value;
                ties are all included
            "best_value" (float): the value on the best day(s)

        Example (Days 1-5, steps, goal 8000):
            {"steps_stats": {"goal": 8000.0,
                             "weekly_averages": [8327.8, None, None, None],
                             "monthly_average": 8327.8,
                             "goal_met": True,
                             "best_days": [5],
                             "best_value": 12192.0}}

    Side effects:
        none (does not print or change anything)

    Assumptions and messy cases:
        Days where the tracker was not worn or died are not included in the
        analysis. If a value is still blank (None, "" or 0), that day is
        skipped for this metric so it does not skew the averages.
        All numbers are floats rounded to 1 decimal place.
        If a metric has no valid days, the averages and best_value are None,
        best_days is [], and goal_met is False.
    """
    # Result key names agreed on in the Decision Log
    key_names = {"steps": "steps_stats", "resting_hr": "rest_stats",
                 "sleep_hours": "sleep_stats", "active_minutes": "active_stats"}

    days = data["day"]
    values = data[metric]

    # Collect valid values for the month, for each week, and their day numbers
    valid_days = []
    valid_values = []
    week_values = [[], [], [], []]

    for i in range(len(values)):
        value = values[i]
        if value is not None and value != "" and value != 0:
            day = int(days[i])
            valid_days.append(day)
            valid_values.append(float(value))
            week_number = (day - 1) // 7  # days 1-7 -> 0, 8-14 -> 1, ...
            if 0 <= week_number < 4:
                week_values[week_number].append(float(value))

    # Weekly averages
    weekly_averages = []
    for week in week_values:
        if len(week) > 0:
            weekly_averages.append(round(sum(week) / len(week), 1))
        else:
            weekly_averages.append(None)

    # Monthly average, goal check, and best day
    if len(valid_values) > 0:
        monthly_average = round(sum(valid_values) / len(valid_values), 1)

        if higher_is_better:
            goal_met = monthly_average >= goal
            best_value = max(valid_values)
        else:
            goal_met = monthly_average <= goal
            best_value = min(valid_values)

        # Every day that ties for the best value is included
        best_days = []
        for i in range(len(valid_values)):
            if valid_values[i] == best_value:
                best_days.append(valid_days[i])
        best_value = round(best_value, 1)
    else:
        monthly_average = None
        goal_met = False
        best_value = None
        best_days = []

    stats = {
        "goal": round(float(goal), 1),
        "weekly_averages": weekly_averages,
        "monthly_average": monthly_average,
        "goal_met": goal_met,
        "best_days": best_days,
        "best_value": best_value,
    }
    return {key_names[metric]: stats}
