import os
import yaml

def analyze_playbook(file_path):
    with open(file_path, 'r') as file:
        try:
            content = yaml.safe_load(file)
            if not content:
                return []
            
            issues = []
            for task in content:
                if isinstance(task, dict) and 'tasks' in task:
                    for subtask in task['tasks']:
                        if 'yum' in subtask:
                            issues.append(f"Potential issue: 'yum' module used in {file_path}")
                        if 'pip' in subtask:
                            issues.append(f"Potential issue: 'pip' module used in {file_path}")
                        if 'include' in subtask:
                            issues.append(f"Potential issue: 'include' directive used in {file_path}")
            return issues
        except yaml.YAMLError as e:
            return [f"Error parsing {file_path}: {str(e)}"]

def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.yml', '.yaml')):
                file_path = os.path.join(root, file)
                issues = analyze_playbook(file_path)
                for issue in issues:
                    print(issue)

# Usage
scan_directory('/home/ehl25977/git/elasticluster/elasticluster/share/playbooks')
