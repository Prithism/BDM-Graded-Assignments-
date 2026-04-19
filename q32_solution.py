import csv

def calculate_score():
    """
    Calculates the best candidate using Method 1 (Equal Weights).
    Criteria: Year of experience, Appraisals, Duration in role, Bench duration,
    Skills count, and Key projects count.
    """
    data_file = "dataset_4_196.xlsx - D1.csv"
    candidates = []
    
    with open(data_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Parse numerical and count criteria
            candidates.append({
                "name": row["Employee name"],
                "exp": float(row["Year of experience"]),
                "a1": float(row["Appraisal 1"]),
                "a2": float(row["Appraisal 2"]),
                "a3": float(row["Appraisal 3"]),
                "skills": len(row["Skills"].split(',')),
                "projects": len(row["Key projects"].split(',')),
                "duration": float(row["Duration in the current role"]),
                "bench": float(row["Bench duration"])
            })

    if not candidates:
        return

    # Define criteria types (True for benefit, False for cost)
    criteria_keys = ["exp", "a1", "a2", "a3", "duration", "bench"]
    is_benefit = [True, True, True, True, True, False]
    
    # Normalize and score
    scores = {}
    for key, benefit in zip(criteria_keys, is_benefit):
        vals = [c[key] for c in candidates]
        v_min, v_max = min(vals), max(vals)
        
        for c in candidates:
            score_acc = scores.get(c["name"], 0)
            if v_max == v_min:
                norm_val = 1.0
            elif benefit:
                norm_val = (c[key] - v_min) / (v_max - v_min)
            else:
                norm_val = (v_max - c[key]) / (v_max - v_min)
            
            scores[c["name"]] = score_acc + norm_val

    # Find candidate with max total score
    best_candidate = max(scores, key=scores.get)
    print(best_candidate)

if __name__ == "__main__":
    calculate_score()
