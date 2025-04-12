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
            try:
                if part.startswith("Method:"):
                    method = part.split(": ")[1]
                elif part.startswith("Efficiency:"):
                    efficiency = float(part.split(": ")[1].replace("%", ""))
            except (IndexError, ValueError):
                continue

        if method and efficiency is not None:
            efficiencies.append(efficiency)
            if method not in method_counts:
                method_counts[method] = 1
            else:
                method_counts[method] += 1

    if not efficiencies:
        return "No valid log entries found."

    avg_eff = sum(efficiencies) / len(efficiencies)
    max_eff = max(efficiencies)
    min_eff = min(efficiencies)
    most_used = max(method_counts, key=method_counts.get)

    summary = {
        "average_efficiency": round(avg_eff, 2),
        "best_efficiency": max_eff,
        "worst_efficiency": min_eff,
        "total_runs": len(efficiencies),
        "most_used_method": most_used
    }

    return summary


def check_recent_efficiency(log_path="logs/replicant.log", threshold=25.0, window=3):
    try:
        with open(log_path, "r") as logfile:
            lines = logfile.readlines()
    except FileNotFoundError:
        return False  # No data to judge

    efficiencies = []

    for line in reversed(lines):  # Start from most recent
        if "Efficiency:" in line:
            try:
                parts = line.strip().split(" | ")
                for part in parts:
                    if part.startswith("Efficiency:"):
                        eff = float(part.split(": ")[1].replace("%", ""))
                        efficiencies.append(eff)
                        if len(efficiencies) == window:
                            break
            except (IndexError, ValueError):
                continue

    if len(efficiencies) < window:
        return False  # Not enough data to decide

    return all(e < threshold for e in efficiencies)

def analyze_user_feedback(feedback_path="logs/user_feedback.log"):
    try:
        with open(feedback_path, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return {}

    counts = {"good": {}, "bad":{}}

    for line in lines:
        parts = line.strip().split(" | ")
        method = None
        feedback = None
        for part in parts:
            if part.startswith("Method:"):
                method = part.split(": ")[1]
            elif part.startswith("Feedback:"):
                feedback = part.split(": ")[1]
        if method and feedback in counts:
            if method not in counts[feedback]:
                counts[feedback][method] = 1
            else:
                counts[feedback][method] += 1

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
                    eff = float(part.split(": ")[1].replace("%", ""))
                    efficiencies.append(eff)
                except (IndexError, ValueError):
                    continue

    if not efficiencies:
        return False

    avg_eff = sum(efficiencies) / len(efficiencies)
    return avg_eff < alert_level

def get_best_performing_method(log_path="logs/replicant.log"):
    try:
        with open(log_path, "r") as logfile:
            lines = logfile.readlines()
    except FileNotFoundError:
        return "basic"

    method_efficiencies = {}

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
                except:
                    continue
        if method and efficiency is not None:
            if method not in method_efficiencies:
                method_efficiencies[method] = []
            method_efficiencies[method].append(efficiency)

    best_method = "basic"
    best_avg = 0.0
    for method, scores in method_efficiencies.items():
        avg = sum(scores) / len(scores)
        if avg > best_avg:
            best_avg = avg
            best_method = method

    if best_method == "basic_compress":
        return "basic"
    elif best_method == "reverse_compress":
        return "reverse"
    else:
        return best_method


    return counts
