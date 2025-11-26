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


def analyze_wine_data():
    """Analyze the wine quality dataset using your CSV functions"""
    print("=== Wine Quality Data Analysis ===\n")
    
    # 1. Read the CSV file using read_text
    print("1. Reading CSV file...")
    csv_content = read_text("winequality-red.csv")
    print(f"   ✓ Read {len(csv_content)} characters\n")
    
    # 2. Parse the CSV content
    lines = csv_content.strip().split('\n')
    reader = csv.reader(lines)
    header = tuple(next(reader))  # Get column names
    data_rows = [tuple(row) for row in reader]  # Convert each row to tuple
    
    print("2. Dataset Overview:")
    print(f"   - Number of wines: {len(data_rows)}")
    print(f"   - Number of attributes: {len(header)}")
    print(f"   - Attributes: {', '.join(header)}\n")
    
    # 3. Show some sample data
    print("3. Sample Data (first 3 wines):")
    for i, row in enumerate(data_rows[:3]):
        print(f"   Wine {i+1}: {row}")
    print()
    
    # 4. Calculate basic statistics
    print("4. Basic Statistics:")
    quality_idx = header.index('quality')
    alcohol_idx = header.index('alcohol')
    
    qualities = [float(row[quality_idx]) for row in data_rows]
    alcohols = [float(row[alcohol_idx]) for row in data_rows]
    
    avg_quality = sum(qualities) / len(qualities)
    avg_alcohol = sum(alcohols) / len(alcohols)
    
    print(f"   - Average quality: {avg_quality:.2f}/10")
    print(f"   - Average alcohol: {avg_alcohol:.2f}%")
    print(f"   - Quality range: {min(qualities)} to {max(qualities)}")
    print(f"   - Alcohol range: {min(alcohols):.1f}% to {max(alcohols):.1f}%\n")
    
    # 5. Create a filtered dataset (high quality wines)
    print("5. Creating filtered dataset...")
    high_quality_wines = []
    for row in data_rows:
        if float(row[quality_idx]) >= 6:  # Quality 6 or higher
            high_quality_wines.append(row)
    
    print(f"   - Found {len(high_quality_wines)} high quality wines (quality ≥ 6)")
    
    # 6. Write filtered data to new CSV using write_csv
    write_csv(high_quality_wines, "results/high_quality_wines.csv", header=header)
    print("   ✓ Saved to 'results/high_quality_wines.csv'\n")
    
    # 7. Create a summary dataset
    print("6. Creating summary dataset...")
    summary_data = []
    for quality in range(3, 9):  # Quality scores from 3 to 8
        wines_of_quality = [row for row in data_rows if float(row[quality_idx]) == quality]
        if wines_of_quality:
            avg_alc = sum(float(row[alcohol_idx]) for row in wines_of_quality) / len(wines_of_quality)
            count = len(wines_of_quality)
            summary_data.append((quality, count, round(avg_alc, 2)))
    
    # Write summary using write_csv
    summary_header = ("Quality", "Count", "Avg_Alcohol")
    write_csv(summary_data, "results/quality_summary.csv", header=summary_header)
    print("   ✓ Saved to 'results/quality_summary.csv'\n")
    
    # 8. Show summary
    print("7. Quality Summary:")
    for quality, count, avg_alc in summary_data:
        print(f"   - Quality {quality}: {count} wines, {avg_alc}% avg alcohol")


def test_csv_functions():
    """Test the CSV reading and writing functions"""
    print("\n" + "="*50)
    print("Testing CSV Functions")
    print("="*50)
    
    # Test 1: Read the original file
    print("\nTest 1: Reading original CSV")
    content = read_text("winequality-red.csv")
    lines = content.strip().split('\n')
    print(f"✓ File contains {len(lines)} lines")
    
    # Test 2: Create a small sample file
    print("\nTest 2: Creating sample file")
    sample_data = [lines[0].split(',')] + [line.split(',') for line in lines[1:6]]  # Header + 5 wines
    write_csv(sample_data[1:], "wine_sample.csv", header=tuple(sample_data[0]))
    print("✓ Created 'wine_sample.csv' with 5 wines")
    
    # Test 3: Test ensure_parent_dir
    print("\nTest 3: Testing directory creation")
    ensure_parent_dir("deep/nested/folder/test_file.csv")
    print("✓ Directory structure created")


if __name__ == "__main__":
    # Run the main analysis
    analyze_wine_data()
    
    # Test the CSV functions
    test_csv_functions()
    
    print("\n" + "="*50)
    print("Analysis Complete!")
    print("Created files:")
    print("- results/high_quality_wines.csv")
    print("- results/quality_summary.csv") 
    print("- wine_sample.csv")
    print("="*50)