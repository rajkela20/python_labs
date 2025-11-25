import sys
import os
from pathlib import Path

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
lib_dir = os.path.join(parent_dir, 'lib')
src_dir = os.path.join(parent_dir, 'src')

sys.path.insert(0, lib_dir)
sys.path.insert(0, src_dir)

from text import normalize, tokenize, count_freq, top_n
from io_txt_csv import read_text, write_csv


def generate_report(input_path: str = "data/input.txt", output_path: str = "report.csv"):
    try:
        input_path = os.path.join(parent_dir, input_path)
        output_path = os.path.join(parent_dir, output_path)
        
        print(f"Looking for input file: {input_path}")
        
        text = read_text(input_path)
        
        if not text.strip():
            print("Всего слов: 0")
            print("Уникальных слов: 0")
            print("Топ-5:")
            write_csv([], output_path, header=("word", "count"))
            print(f"Empty input - created {output_path} with header only")
            return
    
        normalized_text = normalize(text)
        tokens = tokenize(normalized_text)
        freq_dict = count_freq(tokens)
        
        total_words = len(tokens)
        unique_words = len(freq_dict)
        top_words = top_n(freq_dict, 5)
        
        print(f"Всего слов: {total_words}")
        print(f"Уникальных слов: {unique_words}")
        print("Топ-5:")
        
        for word, count in top_words:
            print(f"{word}:{count}")
        
        csv_data = []
        for word, count in top_n(freq_dict): 
            csv_data.append((word, count))
        
        write_csv(csv_data, output_path, header=("word", "count"))
        print(f"Report saved to {output_path}")
        
    except FileNotFoundError:
        print(f"Error: Input file {input_path} not found")
        print("Please create data/input.txt in the project root folder")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Main function to run the text analysis report."""
    input_file = "data/input.txt"
    output_file = "report.csv"
    
    generate_report(input_file, output_file)


if __name__ == "__main__":
    main()