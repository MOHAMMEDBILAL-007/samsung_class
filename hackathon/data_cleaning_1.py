import pandas as pd
import matplotlib.pyplot as plt

# global DataFrame
df = None

# load and prepare the dataset
def load_data(file_path):
    global df
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip().str.lower()  # Normalize column names
    print("Data loaded and cleaned successfully.\n")

# show all available roads in the database
def display_available_roads():
    print("Available Roads and Their Areas:\n")
    unique_roads = df[['area name', 'road/intersection name']].drop_duplicates()
    print(unique_roads.to_string(index=False))

# show statistics for selected road
def analyze_selected_road(road_name):
    road_name = road_name.strip().lower()
    filtered = df[df['road/intersection name'].str.lower() == road_name]

    if filtered.empty:
        print("\nNo data found for the selected road. Please check the spelling.\n")
        return

    table_columns = [
        'traffic volume', 'average speed', 'travel time index', 'congestion level',
        'road capacity utilization', 'incident reports', 'environmental impact',
        'public transport usage', 'traffic signal compliance', 'parking usage',
        'pedestrian and cyclist count'
    ]

    graph_columns = table_columns[1:]  # exclude traffic volume from graphs because it is too high
    # adding units for good structure output
    units = {
        'traffic volume': 'vehicles/day',
        'average speed': 'km/h',
        'travel time index': '',
        'congestion level': '%',
        'road capacity utilization': '%',
        'incident reports': 'reports',
        'environmental impact': 'index',
        'public transport usage': '%',
        'traffic signal compliance': '%',
        'parking usage': '%',
        'pedestrian and cyclist count': 'people'
    }

    averages = filtered[table_columns].mean().round(2)# roundoff the decimals

    weather = filtered['weather conditions'].mode()[0] if not filtered['weather conditions'].mode().empty else "Unknown"
    construction = filtered['roadwork and construction activity'].mode()[0] if not filtered['roadwork and construction activity'].mode().empty else "Unknown"

    print(f"\nBased on 2.5 years of data on : {road_name.title()} we have analysed")
    print("-" * 60)
    print(f"{'Metric':40} {'Value':>10}  Unit")
    print("-" * 60)
    for metric in table_columns:
        metric_name = metric.title()
        value = averages[metric]
        unit = units.get(metric, '')
        print(f"{metric_name:40} {value:>10}  {unit}")
    print("-" * 60)
    print(f"{'Weather Condition (Most Common)':40} {weather}")
    print(f"{'Roadwork & Construction Activity (Most Common)':40} {construction}")

    #ideal values for comparison according to my web search
    ideal_values = {
        'average speed': 60.0,
        'travel time index': 1.0,
        'congestion level': 10.0,
        'road capacity utilization': 60.0,
        'incident reports': 0.0,
        'environmental impact': 50.0,
        'public transport usage': 90.0,
        'traffic signal compliance': 95.0,
        'parking usage': 50.0,
        'pedestrian and cyclist count': 100.0
    }

    # prepare data for graphs
    actual_y = averages[graph_columns].values
    ideal_y = [ideal_values[col] for col in graph_columns]
    x_labels = [col.title() for col in graph_columns]
    x_pos = range(len(graph_columns))
    bar_width = 0.35

    #plot size of the graphs
    fig, axs = plt.subplots(1, 2, figsize=(16, 6))

    #actual values graph
    axs[0].bar(x_pos, actual_y, color='skyblue', width=bar_width)
    axs[0].plot(x_pos, actual_y, color='red', marker='o', linewidth=2)
    axs[0].set_title(f"Actual Traffic Metrics for {road_name.title()}")
    axs[0].set_xticks(x_pos)
    axs[0].set_xticklabels(x_labels, rotation=45, ha='right')
    axs[0].set_ylabel("Average Value")
    axs[0].grid(axis='y', linestyle='--', alpha=0.5)

    #actual value vs ideal value graphs comparision
    axs[1].bar(x_pos, actual_y, width=bar_width, label='Actual', color='skyblue')
    axs[1].bar([i + bar_width for i in x_pos], ideal_y, width=bar_width, label='Ideal', color='lightgreen')
    axs[1].set_title("Actual vs Ideal Traffic Metrics\nWARNING! if the Ideal graph is way to different then actual graph,then your day is ruined")
    axs[1].set_xticks([i + bar_width / 2 for i in x_pos])
    axs[1].set_xticklabels(x_labels, rotation=45, ha='right')
    axs[1].set_ylabel("Value")
    axs[1].legend()
    axs[1].grid(axis='y', linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.show()

# Main function to run the above functions
def run_analysis():
    display_available_roads()
    selected = input("\nEnter the Road/Intersection Name from the list above: ")
    analyze_selected_road(selected)

# Main script
if __name__ == "__main__":
    load_data("D:\\learning\\samsung_class\\hackathon\\Banglore_traffic_Dataset.csv")  # please use your folder location mr/mrs.evaluator
    run_analysis()
