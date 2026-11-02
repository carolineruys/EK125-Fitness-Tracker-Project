from loader import load_tracker_data
from analyzer import analyze_metric
from reporter import write_report

def main():
    data = load_tracker_data("fitness_data.csv")
    print(type(data), data.keys, len(data[0]), len(data[2]))

    plan = [("steps", 8000, True),
            ("resting_hr", 62, False)]

    results_list = []
    for metric, goal, higher_is_better in plan:
        results = analyze_metric(data, metric, goal, higher_is_better)
        print(type(results), results.keys)
        results_list.append(results)
        
    print(len(results_list))
    write_report(results_list, "fitness_report.txt")

if __name__ == "__main__":
    main()
