import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) < 3:
    print("Usage: python combine_text_files.py <output_file> <input_file1> <input_file2> ...")
    sys.exit(1)

# Get the output file path from the command line
output_file = sys.argv[1]

# Open the output file for appending
with open(output_file, 'a') as output:
    # Iterate over input files starting from the third command-line argument
    for input_file in sys.argv[2:]:
        try:
            with open(input_file, 'r') as input:
                content = input.read()
                # Append the content to the output file
                output.write(content)
                print(f"Appended '{input_file}' to '{output_file}'")
        except FileNotFoundError:
            print(f"File '{input_file}' not found.")
        except Exception as e:
            print(f"An error occurred while processing '{input_file}': {e}")

print(f"Combined contents of input files into '{output_file}'.")
