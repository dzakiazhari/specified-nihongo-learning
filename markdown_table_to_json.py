import pandas as pd

def markdown_table_to_json(input_file, output_file):
    # Read the markdown table into a DataFrame
    df = pd.read_table(input_file, sep="|", header=1, skiprows=[2, -1], engine='python', names=["No.", "Word (JP)", "Hiragana Reading", "Translation (EN)"])
    
    # Convert the DataFrame to a JSON file
    df.to_json(output_file, orient='records', indent=2)
