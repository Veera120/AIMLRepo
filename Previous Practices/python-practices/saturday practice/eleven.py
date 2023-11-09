import sys

def count_file_stats(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            lines = content.split('\n')
            words = content.split()
            character_count = len(content)

            print(f"Number of lines: {len(lines)}")
            print(f"Number of words: {len(words)}")
            print(f"Number of characters: {character_count}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_file_stats.py <file_path>")
    else:
        file_path = sys.argv[1]
        count_file_stats(file_path)
