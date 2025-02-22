universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    students = [uni[1] for uni in universities]
    tuition_fees = [uni[2] for uni in universities]
    return students, tuition_fees

def mean(values):
    return sum(values) / len(values)

def median(values):
    sorted_vals = sorted(values)
    mid = len(sorted_vals) // 2
    if len(sorted_vals) % 2 == 0:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
    return sorted_vals[mid]

students, tuition_fees = enrollment_stats(universities)

print("******")
print(f"Total students: {sum(students):,}")
print(f"Total tuition: $ {sum(tuition_fees):,}")
print(f"Student mean: {mean(students):.2f}")
print(f"Student median: {median(students):,.0f}")
print(f"Tuition mean: $ {mean(tuition_fees):.2f}")
print(f"Tuition median: $ {median(tuition_fees):,.0f}")
print("******")