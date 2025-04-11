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
