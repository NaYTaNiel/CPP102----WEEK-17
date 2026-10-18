"""
Simulated Device Monitoring and Alert System
CPP102 Week 17 Integrative Programming Project
Student: Nathaniel Sios-e Panganiban
"""

def get_initial_readings():
    """Return the initial list of device temperature readings."""
    return [28, 31, 35, 37, 29]


def view_readings(readings):
    """Display every value currently in the list with its position number."""
    print("\nCURRENT READINGS")
    print("----------------")
    for index, value in enumerate(readings, start=1):
        print(f"Reading {index}: {value} °C")


def is_whole_number(text):
    """Return True if text is a valid non-negative whole number string."""
    if len(text) == 0:
        return False
    for char in text:
        if char not in "0123456789":
            return False
    return True


def add_reading(readings):
    """Prompt user for a new reading and add it to the list if valid (0 to 100)."""
    text = input("Enter new reading: ")
    
    if len(text) == 0:
        print("\nInvalid input. The reading cannot be empty.")
        return
    
    if not is_whole_number(text):
        print("\nInvalid input. Enter a whole number only.")
        return
        
    value = int(text)
    if value < 0 or value > 100:
        print("\nInvalid reading. Enter a value from 0 to 100.")
        return
        
    readings.append(value)
    print("\nReading added successfully.")


def classify_reading(value):
    """Classify a single temperature reading based on lab rules."""
    if value < 30:
        return "NORMAL"
    elif value <= 35:
        return "WARNING"
    else:
        return "CRITICAL"


def classify_all_readings(readings):
    """Classify every reading in the list and print the results."""
    print("\nREADING CLASSIFICATION")
    print("----------------------")
    for value in readings:
        print(f"{value} °C -> {classify_reading(value)}")


def compute_total(readings):
    """Return the sum of all readings without using sum()."""
    total = 0
    for value in readings:
        total += value
    return total


def compute_average(readings):
    """Return the average temperature computed from total and length."""
    if len(readings) == 0:
        return 0.0
    return compute_total(readings) / len(readings)


def find_minimum(readings):
    """Return the minimum temperature without using min()."""
    if len(readings) == 0:
        return 0
    minimum = readings[0]
    for value in readings:
        if value < minimum:
            minimum = value
    return minimum


def find_maximum(readings):
    """Return the maximum temperature without using max()."""
    if len(readings) == 0:
        return 0
    maximum = readings[0]
    for value in readings:
        if value > maximum:
            maximum = value
    return maximum


def count_category(readings, category_name):
    """Count how many readings fall into a specific classification category."""
    count = 0
    for value in readings:
        if classify_reading(value) == category_name:
            count += 1
    return count


def determine_overall_status(warning_count, critical_count):
    """Determine the device operational status based on warning/critical counts."""
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"


def display_summary(readings):
    """Compute and display numerical summary, category percentages, and overall status."""
    total_count = len(readings)
    total_sum = compute_total(readings)
    avg_val = compute_average(readings)
    min_val = find_minimum(readings)
    max_val = find_maximum(readings)
    
    norm_count = count_category(readings, "NORMAL")
    warn_count = count_category(readings, "WARNING")
    crit_count = count_category(readings, "CRITICAL")
    
    norm_pct = (norm_count / total_count) * 100 if total_count > 0 else 0.0
    warn_pct = (warn_count / total_count) * 100 if total_count > 0 else 0.0
    crit_pct = (crit_count / total_count) * 100 if total_count > 0 else 0.0
    
    overall_status = determine_overall_status(warn_count, crit_count)
    
    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings  : {total_count}")
    print(f"Total of readings   : {total_sum}")
    print(f"Average temperature : {avg_val:.2f} °C")
    print(f"Minimum temperature : {min_val} °C")
    print(f"Maximum temperature : {max_val} °C\n")
    
    print(f"NORMAL   : {norm_count} ({norm_pct:.2f}%)")
    print(f"WARNING  : {warn_count} ({warn_pct:.2f}%)")
    print(f"CRITICAL : {crit_count} ({crit_pct:.2f}%)\n")
    print(f"Overall Status: {overall_status}")


def main():
    """Control the main program execution loop and menu selection."""
    readings = get_initial_readings()
    
    while True:
        print("\nSIMULATED DEVICE MONITORING SYSTEM")
        print("----------------------------------")
        print("[1] View Readings")
        print("[2] Add Reading")
        print("[3] Classify Readings")
        print("[4] Generate Summary")
        print("[5] Exit")
        
        choice = input("\nEnter choice: ")
        
        if choice == "1":
            view_readings(readings)
        elif choice == "2":
            add_reading(readings)
        elif choice == "3":
            classify_all_readings(readings)
        elif choice == "4":
            display_summary(readings)
        elif choice == "5":
            print("\nThank you for using the Device Monitoring System.")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
