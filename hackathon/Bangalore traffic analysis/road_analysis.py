# road_analysis.py
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

def analyze_selected_road(df, road_name):
    road_name = road_name.strip().lower()
    filtered = df[df['road/intersection name'].str.lower() == road_name]

    if filtered.empty:
        print("\nNo data found for the selected road. Please check the spelling.\n")
        return

    # Ensure sorting by date for proper regression
    filtered = filtered.sort_values('date')

    metrics = [
        'traffic volume', 'average speed', 'travel time index', 'congestion level',
        'road capacity utilization', 'incident reports', 'environmental impact',
        'public transport usage', 'traffic signal compliance', 'parking usage',
        'pedestrian and cyclist count'
    ]

    print(f"\nLinear Regression Analysis for {road_name.title()}")
    print("-" * 75)
    print(f"{'Metric':40} {'Slope (Trend)':>15} {'Interpretation':>20}")
    print("-" * 75)

    x = np.arange(len(filtered)).reshape(-1, 1) 
    slopes = {}
    
    for metric in metrics:
        if metric not in filtered.columns:
            continue
        y = filtered[metric].ffill().bfill().values.reshape(-1, 1)

        model = LinearRegression()
        model.fit(x, y)
        slope = model.coef_[0][0]
        slopes[metric] = slope

        if slope > 0:
            trend = "Increasing"
        elif slope < 0:
            trend = "Decreasing"
        else:
            trend = "Stable"

        print(f"{metric.title():40} {slope:>15.3f} {trend:>20}")

    print("-" * 75)
    print("Positive slope → upward trend | Negative slope → downward trend")

    # Plot selected metrics to visualize trends
    metrics_to_plot = ['traffic volume', 'congestion level', 'average speed']
    fig, axs = plt.subplots(len(metrics_to_plot), 1, figsize=(10, 10))

    for i, metric in enumerate(metrics_to_plot):
        y = filtered[metric].ffill().bfill().values.reshape(-1, 1)  # fixed here too
        model = LinearRegression().fit(x, y)
        y_pred = model.predict(x)

        axs[i].plot(filtered['date'], y, label='Actual', color='skyblue')
        axs[i].plot(filtered['date'], y_pred, label='Trend Line', color='red', linewidth=2)
        axs[i].set_title(f"{metric.title()} Trend over Time")
        axs[i].set_xlabel("Date")
        axs[i].set_ylabel(metric.title())
        axs[i].legend()
        axs[i].grid(alpha=0.5)

    plt.tight_layout()
    plt.show()
