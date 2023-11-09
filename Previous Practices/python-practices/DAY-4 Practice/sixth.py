import sys
import os

def process_files(input_file_path, output_file_path):
    try:
        # Check if both input and output file paths are provided
        if not input_file_path or not output_file_path:
            raise ValueError("Both input and output file paths are required.")
        
        # Check if the input file exists
        if not os.path.exists('source.txt'):
            raise FileNotFoundError(f"Input file '{source.txt}' does not exist.")

        # Read data from the input file and process it
        with open('source.txt', 'r') as input_file, open('om.txt', 'w') as output_file:
            for line in input_file:
                # Your processing logic can go here
                # For this example, we'll just copy the lines from input to output
                output_file.write(line)

        print("File processing completed successfully.")
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python program.py input_file output_file")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    process_files(input_file_path, output_file_path)
