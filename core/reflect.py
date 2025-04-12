def analyze_log_history(log_path="logs/replicant.log"):
    try:
        with open(log_path, "r") as logfile:
            lines = logfile.readlines()
    except FileNotFoundError:
        return "No log file found."

    efficiencies = []
    method_counts = {}

    for line in lines:
        parts = line.strip().split(" | ")
        method = None
        efficiency = None

        for part in parts:
            if part.startswith("Method:"):
                method = part.split(": ")[1]
            elif part.startswith("Efficiency:"):
                try:
                    efficiency = float(part.split(": ")[1].replace("%", ""))
                except (IndexError, ValueError):
                    continue

        if method and efficiency is not None:
            efficiencies.append(efficiency)
            method_counts[method] = method_counts.get(method, 0) + 1

    if not efficiencies:
        return "No valid log entries found."

    summary = {
        "average_efficiency": round(sum(efficiencies) / len(efficiencies), 2),
        "best_efficiency": max(efficiencies),
        "worst_efficiency": min(efficiencies),
        "total_runs": len(efficiencies),
        "most_used_method": max(method_counts, key=method_counts.get)
    }
    return summary


def analyze_user_feedback(path="logs/user_feedback.log"):
    try:
        with open(path, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        return {}

    feedback_data = {"good": {}, "bad": {}}

    for line in lines:
        parts = line.strip().split(" | ")
        method, sentiment = None, None

        for part in parts:
            if part.startswith("Method:"):
                method = part.split(": ")[1]
            elif part.startswith("Feedback:"):
                sentiment = part.split(": ")[1]

        if method and sentiment in feedback_data:
            feedback_data[sentiment][method] = feedback_data[sentiment].get(method, 0) + 1

    return feedback_data


def check_recent_efficiency(log_path="logs/replicant.log", threshold=20, alert_level=40):
    try:
        with open(log_path, "r") as logfile:
            lines = logfile.readlines()[-threshold:]
    except FileNotFoundError:
        return False

    efficiencies = []

    for line in lines:
        parts = line.strip().split(" | ")
        for part in parts:
            if part.startswith("Efficiency:"):
                try:
                    efficiency = float(part.split(": ")[1].replace("%", ""))
                    efficiencies.append(efficiency)
                except (IndexError, ValueError):
                    continue

    if not efficiencies:
        return False

    return sum(efficiencies) / len(efficiencies) < alert_level


def get_best_performing_method(log_path="logs/replicant.log"):
    try:
        with open(log_path, "r") as logfile:
            lines = logfile.readlines()
    except FileNotFoundError:
        return "basic"

    method_scores = {}

    for line in lines:
        parts = line.strip().split(" | ")
        method, efficiency = None, None

        for part in parts:
            if part.startswith("Method:"):
                method = part.split(": ")[1]
            elif part.startswith("Efficiency:"):
                try:
                    efficiency = float(part.split(": ")[1].replace("%", ""))
                except:
                    continue

        if method and efficiency is not None:
            method_scores.setdefault(method, []).append(efficiency)

    best_method = "basic"
    best_avg = 0.0

    for method, scores in method_scores.items():
        avg = sum(scores) / len(scores)
        if avg > best_avg:
            best_avg = avg
            best_method = method

    return best_method if best_method in ["basic", "reverse"] else "basic"


def suggest_method():
    method_by_eff = get_best_performing_method()
    feedback = analyze_user_feedback()


