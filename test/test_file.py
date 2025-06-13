import os

def extract_error_lines(log_dir, output_file='error_report.txt'):
    with open(output_file, 'w') as outfile:
        for root, _, files in os.walk(log_dir):
            for filename in files:
                if filename.endswith('.log'):
                    log_path = os.path.join(root, filename)
                with open(log_path, 'r') as infile:
                    for line in infile:
                        if 'Error' in line:
                            outfile.write(f"{filename}: {line}")
                            
                            
extract_error_lines('path/to/file')