# road_display.py

def display_available_roads(df):
    print("Available Roads and Their Areas:\n")
    unique_roads = df[['area name', 'road/intersection name']].drop_duplicates()
    print(unique_roads.to_string(index=False))
