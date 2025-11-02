# main.py
import os
from data_loader import load_data
from road_display import display_available_roads
from road_analysis import analyze_selected_road

def run_analysis():
    filename = "Banglore_traffic_Dataset.csv"
    file_path = os.path.join(os.path.dirname(__file__), filename)

    try:
        df = load_data(file_path)
        display_available_roads(df)
        selected = input("\nEnter the Road/Intersection Name from the list above: ")
        analyze_selected_road(df, selected)
    except FileNotFoundError:
        print(f"\nError: Could not find '{filename}' in the project directory.")
        print("Make sure the dataset CSV file is placed in the same folder as this script.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    run_analysis()
