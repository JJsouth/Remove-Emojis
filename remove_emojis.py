import pandas as pd
import re
import os

def remove_emojis(text):
    #Checks if text is a string, If it's not (e.g., it’s NaN or another type), the function skips emoji removal and just returns it as-is.
    if isinstance(text, str):
        emoji_pattern = re.compile(
            "["
            "\U0001F600-\U0001F64F" # emoticons
            "\U0001F300-\U0001F5FF" # symbols & pictographs
            "\U0001F680-\U0001F6FF" # transport & map symbols
            "\U0001F1E0-\U0001F1FF" # flags (iOS)
            "\U00002500-\U00002BEF" # chinese char
            "\U00002702-\U000027B0"
            "\U000024C2-\U0001F251"
            "\U0001f926-\U0001f937"
            "\U00010000-\U0010ffff"
            "\u2640-\u2642"
            "\u2600-\u2B55"
            "\u200d"
            "\u23cf"
            "\u23e9"
            "\u231a"
            "\ufe0f" # dingbats
            "\u3030"
            "]+", flags=re.UNICODE
        )
        return emoji_pattern.sub(r'', text)
    return text


if __name__ == "__main__":
    input_file = "sms_data_to_add.csv"  # <-- Replace with your actual file name
    base, ext = os.path.splitext(input_file)

    column_to_clean = "Reply Content"

    df = pd.read_csv(input_file)
    # Applies the remove_emojis function to the data field column
    df[column_to_clean] = df[column_to_clean].apply(remove_emojis)

    #create new file and append _cleaned to the original file name
    output_file = f"{base}_cleaned{ext}"
    df.to_csv(output_file, index=False)