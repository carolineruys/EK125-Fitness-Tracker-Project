from loader import load_tracker_data
from analyzer import analyze_metric
from reporter import write_report

def main():
    data = load_tracker_data("fitness_data.csv")

    plan = [("steps", 8000, True),
            ("resting_hr", 62, False)]

    results_list = []
    for metric, goal, higher_is_better in plan:
        results = analyze_metric(data, metric, goal, higher_is_better)
        results_list[metric] = results
    
    write_report(results_list, "fitness_report.txt")

if __name__ == "__main__":
    main()
