def analyze_department_demand(departments):
    results = []
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
    return results                                  
