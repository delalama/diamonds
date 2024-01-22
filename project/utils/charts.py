import os
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

exported_chart_size = (10, 6)

# Ensure the 'generated_charts' directory exists
output_dir = os.path.join("generated_charts", datetime.now().strftime("%Y%m%d_%H%M"))
os.makedirs(output_dir, exist_ok=True)

def do_charts_new(df):
    sns.set_palette("Pastel1")

    # Assuming 'df' is your DataFrame
    plt.figure(figsize=(10, 6))

    # Using Seaborn to create a pair plot with the specified color palette
    sns.pairplot(df.head(10))

    plt.suptitle('Pair Plot for DataFrame')
    plt.show()

def save_chart(chart_type, filename, format="png"):
    fig = plt.figure(figsize=exported_chart_size)
    # ... (rest of the code)

    plt.savefig(os.path.join(output_dir, f"{filename}.{format}"))
    plt.close()

