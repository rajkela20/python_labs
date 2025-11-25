from pathlib import Path
from typing import Union, List, Tuple
import csv


def read_text(path: Union[str, Path], encoding: str = "utf-8") -> str:
    path = Path(path)
    with open(path, 'r', encoding=encoding) as file:
        content = file.read()
    
    return content


def write_csv(rows: List[Union[Tuple, List]], path: Union[str, Path], 
              header: Tuple[str, ...] = None) -> None:
    path = Path(path)
    ensure_parent_dir(path)
    
    with open(path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if header is not None:
            writer.writerow(header)
        if rows:
            first_row_length = len(rows[0])
            for i, row in enumerate(rows):
                if len(row) != first_row_length:
                    raise ValueError(
                        f"All rows must have the same length. "
                        f"Row {i} has length {len(row)}, expected {first_row_length}"
                    )
        
        writer.writerows(rows)


def ensure_parent_dir(path: Union[str, Path]) -> None:
    path = Path(path)
    parent_dir = path.parent
    if not parent_dir.exists():
        parent_dir.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    print("Testing io_txt_csv functions...")
    print("\n1. Testing read_text...")
    test_file = Path("test_input.txt")
    try:
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write("Hello, World!\nThis is a test.\nLine 3.")
        
        content = read_text(test_file)
        print(f"Read content: {repr(content)}")
        
        empty_file = Path("empty_test.txt")
        with open(empty_file, 'w', encoding='utf-8') as f:
            pass 
        
        empty_content = read_text(empty_file)
        print(f"Empty file returns: {repr(empty_content)}")
        
        empty_file.unlink()
        
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n2. Testing write_csv...")
    try:
        data = [
            ("hello", 2),
            ("world", 1),
            ("test", 1)
        ]
        write_csv(data, "test_output.csv", header=("Word", "Count"))
        print("Created CSV with header and data")
        
        write_csv([], "header_only.csv", header=("Name", "Age"))
        print("Created CSV with only header")
        
        write_csv([], "empty.csv")
        print("Created empty CSV")
        
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n3. Testing ensure_parent_dir...")
    try:
        ensure_parent_dir("deep/nested/folder/file.txt")
        print("Created nested directories")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n4. Cleaning up...")
    test_files = [
        "test_input.txt", "test_output.csv", 
        "header_only.csv", "empty.csv"
    ]
    
    for file in test_files:
        file_path = Path(file)
        if file_path.exists():
            file_path.unlink()
            print(f"Removed {file}")

    test_dir = Path("deep")
    if test_dir.exists():
        import shutil
        shutil.rmtree(test_dir)
        print("Removed test directories")
    
    print("\nAll tests completed!")