import pandas as pd
import matplotlib.pyplot as plt

def create_combined_plot(file_path='FAOSTAT_data_7-23-2022.csv'):
    
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        print("Please ensure the CSV file is in the same directory as your script.")
        return

    ghana_df = df[df['Area'] == 'Ghana']
    ivory_coast_df = df[df['Area'] == "Côte d'Ivoire"]

    ghana_table = create_country_table(ghana_df)
    ivory_coast_table = create_country_table(ivory_coast_df)

    fig, axs = plt.subplots(2, 2, figsize=(18, 12))
    fig.suptitle('Cocoa Production Analysis: Ghana and Côte d\'Ivoire', fontsize=20)

    axs[0, 0].scatter(ghana_table['Year'], ghana_table['Yield'], color='green')
    axs[0, 0].set_title('Ghana: Yield Over Time')
    axs[0, 0].set_xlabel('Year')
    axs[0, 0].set_ylabel('Yield (tonnes/ha)')
    axs[0, 0].grid(True)

    axs[0, 1].scatter(ivory_coast_table['Year'], ivory_coast_table['Yield'], color='orange')
    axs[0, 1].set_title('Côte d\'Ivoire: Yield Over Time')
    axs[0, 1].set_xlabel('Year')
    axs[0, 1].set_ylabel('Yield (tonnes/ha)')
    axs[0, 1].grid(True)

    axs[1, 0].bar(ghana_table['Year'], ghana_table['Area harvested'], color='green')
    axs[1, 0].set_title('Ghana: Area Harvested Over Time')
    axs[1, 0].set_xlabel('Year')
    axs[1, 0].set_ylabel('Area Harvested (ha)')
    
    axs[1, 0].tick_params(axis='x', rotation=90)


    axs[1, 1].bar(ivory_coast_table['Year'], ivory_coast_table['Area harvested'], color='orange')
    axs[1, 1].set_title('Côte d\'Ivoire: Area Harvested Over Time')
    axs[1, 1].set_xlabel('Year')
    axs[1, 1].set_ylabel('Area Harvested (ha)')

    axs[1, 1].tick_params(axis='x', rotation=90)


    plt.tight_layout(rect=[0, 0.03, 1, 0.95]) 
    plt.savefig('combined_cocoa_plots.png')
    plt.close()
    print("Successfully generated the combined plot and saved it as 'combined_cocoa_plots.png'")

def create_country_table(df):
    """
    Pivots the DataFrame to create a table with 'Area harvested', 'Yield',
    and 'Production' as columns.
    """
    table = df.pivot_table(index='Year', columns='Element', values='Value')
    table = table.reset_index()
    
    for col in ['Year', 'Area harvested', 'Yield', 'Production']:
        if col not in table.columns:
            table[col] = 0
    return table[['Year', 'Area harvested', 'Yield', 'Production']]

if __name__ == '__main__':
    create_combined_plot()
