schedule = {}

def add_shift(employee_id, shift):
    if employee_id in schedule:
        print('Employee already has a shift scheduled')
    else:
        schedule[employee_id] = shift
        print('Shift added successfully')

def remove_shift(employee_id):
    if employee_id not in schedule:
        print('Employee does not have a shift scheduled')
    else:
        del schedule[employee_id]
        print('Shift removed successfully')

def update_shift(employee_id, new_shift):
    if employee_id not in schedule:
        print('Employee does not have a shift scheduled')
    else:
        schedule[employee_id] = new_shift
        print('Shift updated successfully')