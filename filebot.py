# Import necessary libraries
import os

# Define function to create folder hierarchy

def create_folder_hierarchy(project_name, project_type):
    # Define root directory
    root_dir = os.getcwd()
    
    # Define project directory
    project_dir = os.path.join(root_dir, project_name)
    
    # Create project directory if it does not exist
    if not os.path.exists(project_dir):
        os.mkdir(project_dir)
    
    # Define project type directory
    project_type_dir = os.path.join(project_dir, project_type)
    
    # Create project type directory if it does not exist
    if not os.path.exists(project_type_dir):
        os.mkdir(project_type_dir)
    
    # Define subdirectories
    subdirs = ['data', 'docs', 'src', 'tests']
    
    # Create subdirectories if they do not exist
    for subdir in subdirs:
        subdir_path = os.path.join(project_type_dir, subdir)
        if not os.path.exists(subdir_path):
            os.mkdir(subdir_path)
    
    # Print success message
    print(f'Folder hierarchy created for {project_name} {project_type} project.')

# Define main function

def main():
    # Define projects
    projects = [
        {'name': 'How2Save', 'type': 'web'},
        {'name': 'Optibiz', 'type': 'data'}
    ]
    
    # Loop through projects and create folder hierarchy
    for project in projects:
        create_folder_hierarchy(project['name'], project['type'])

# Call main function
if __name__ == '__main__':
    main()