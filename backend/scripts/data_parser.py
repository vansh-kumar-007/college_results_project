import pandas as pd

def parse_data_to_csv(raw_text, output_csv):
    """
    Parse raw text into structured CSV.
    """
    data = []
    for line in raw_text.split("\n"):
        if line.strip():
            data.append(line.split())

    df = pd.DataFrame(data)
    df.to_csv(output_csv, index=False)
    print(f"Data saved to {output_csv}")
