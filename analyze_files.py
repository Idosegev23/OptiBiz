# Importing the os module
import os

# Defining the directory paths
paths = [
    '/Users/idosegev/Downloads/AutoGPT/Auto-GPT/autogpt/auto_gpt_workspace',
    '/Users/idosegev/Downloads/How2Save',
    '/Users/idosegev/Downloads/OptiBiz'
]

# Defining the project names and types
projects = {
    'How2Save': 'web',
    'Optibiz': 'data'
}

# Defining the log file
log_file = open('log.txt', 'w')

# Defining the summary file
summary_file = open('/Users/idosegev/Downloads/AutoGPT/Auto-GPT/autogpt/auto_gpt_workspace/Allfiles.txt', 'w')

# Looping through the directory paths
for path in paths:
    # Looping through the directory
    for root, dirs, files in os.walk(path):
        # Looping through the files
        for file in files:
            # Looping through the projects
            for project, project_type in projects.items():
                # Checking if the project name is in the file name
                if project in file:
                    # Creating the project directory if it does not exist
                    if not os.path.exists(os.path.join(root, project)):
                        os.mkdir(os.path.join(root, project))
                    # Creating the project type directory if it does not exist
                    if not os.path.exists(os.path.join(root, project, project_type)):
                        os.mkdir(os.path.join(root, project, project_type))
                    # Moving the file to the project type directory
                    os.rename(os.path.join(root, file), os.path.join(root, project, project_type, file))
                    # Writing to the log file
                    log_file.write(f'[{project}]{{{file}}} - summary\n')
                    # Reading the file
                    with open(os.path.join(root, project, project_type, file), 'r') as f:
                        code = f.read()
                    # Writing to the summary file
                    summary_file.write(f'[{project}]{{{file}}} - {code[:50]}...\n')

# Closing the log file
log_file.close()

# Closing the summary file
summary_file.close()