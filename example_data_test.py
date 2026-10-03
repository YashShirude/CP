import subprocess
import os
import sys
import glob

# --- Configuration ---
rating = "1200"
qu_no = "7"

path = f"{rating}"
file_prefix = f"Qu{qu_no}"

# Paste your sample data here (keep 'input' and 'output' labels)
sample_data = """
input
3
3 5
1 4 2 8 5
7 9 2 1 4
3 8 5 3 1
1 4
4 15 1 10
4 3
1 2 3
3 2 1
1 2 1
4 2 7
"""

def parse_sample_data(data_str):
    """Splits the sample data into input and expected output blocks."""
    lines = [line.strip() for line in data_str.strip().splitlines() if line.strip()]
    
    input_lines = []
    output_lines = []
    current_section = None
    
    for line in lines:
        if line.lower() == "input":
            current_section = "input"
            continue
        elif line.lower() == "output":
            current_section = "output"
            continue
        
        if current_section == "input":
            input_lines.append(line)
        elif current_section == "output":
            output_lines.append(line)
            
    return "\n".join(input_lines), "\n".join(output_lines)

def run_checker():
    # 1. Parse sample inputs and outputs
    sample_input = parse_sample_data(sample_data)
    if not sample_input:
        print("❌ Error: Sample data must contain both 'input' header.")
        sys.exit(1)

    # 2. Find the Python file using glob matching
    search_pattern = os.path.join(path, f"{file_prefix}*.py")
    matching_files = glob.glob(search_pattern)

    if not matching_files:
        print(f"❌ Error: No Python file found starting with '{file_prefix}' in directory '{path}'")
        sys.exit(1)
    elif len(matching_files) > 1:
        print(f"⚠️ Warning: Found multiple matching files. Using the first one:")
        for f in matching_files:
            print(f"  - {f}")
    
    py_file = matching_files[0]
    print(f"🚀 Running solution: {py_file}")

    # 3. Run the Python solution with the sample input
    try:
        process_res = subprocess.run(
            [sys.executable, py_file], 
            input=sample_input, 
            capture_output=True, 
            text=True, 
            timeout=5  # 5 seconds safety timeout
        )
    except subprocess.TimeoutExpired:
        print("❌ Time Limit Exceeded (TLE) on sample data!")
        sys.exit(1)

    # 4. Check for Runtime Errors
    if process_res.returncode != 0:
        print("❌ Runtime Error (RE):")
        print(process_res.stderr)
        sys.exit(1)

    # 5. Compare outputs (stripped of trailing whitespaces/newlines)
    your_output = process_res.stdout.strip()
    print("\n📥 [Your Output]:")
    print(your_output)

if __name__ == "__main__":
    run_checker()
