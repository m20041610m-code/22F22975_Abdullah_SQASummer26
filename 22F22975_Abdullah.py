OVERLOAD_THRESHOLD = 1.0
NEAR_CAPACITY_THRESHOLD = 0.85


def analyze_department_demand(departments):
    results = []

    for dept in departments:
        name = dept['name']
        visits = dept['visits']
        capacity = dept['capacity']
        utilization = visits / capacity

        if utilization > OVERLOAD_THRESHOLD:
            status = "Overloaded"
        elif utilization >= NEAR_CAPACITY_THRESHOLD:
            status = "Near Capacity"
        else:
            status = "Normal"

        results.append({
            'department': name,
            'utilization': round(utilization, 2),
            'status': status,
        })

    return results
