```python
def analyze_department_demand(departments):
    results = []
    processed_count = 0

    for dept in departments:
        name = dept['name']
        visits = dept['visits']
        capacity = dept['capacity']
        utilization = visits / capacity

        if utilization > 1.0:
            status = "Overloaded"
        elif utilization >= 0.85:
            status = "Near Capacity"
        else:
            status = "Normal"

        results.append({
            'department': name,
            'utilization': round(utilization, 2),
            'status': status,
        })

        processed_count += 1

    print(f"Departments processed: {processed_count}")
    return results
```
