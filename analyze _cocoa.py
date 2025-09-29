import pandas as pd
import matplotlib.pyplot as plt

def analyze_cocoa_data(file_path='FAOSTAT_data_7-23-2022(1).csv'):

    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        print("Please make sure the CSV file is in the same directory as the script,"
              " or provide the correct file path.")
        return

    ghana_df = df[df['Area'] == 'Ghana']
    ivory_coast_df = df[df['Area'] == "Côte d'Ivoire"]

    ghana_table = create_country_table(ghana_df)
    ivory_coast_table = create_country_table(ivory_coast_df)

    ghana_table.to_csv('ghana_cocoa_data.csv', index=False)
    ivory_coast_table.to_csv('ivory_coast_cocoa_data.csv', index=False)
    print("Generated 'ghana_cocoa_data.csv' and 'ivory_coast_cocoa_data.csv'")


    plot_scatter(ghana_table, 'Ghana', 'ghana_yield_plot.png')
    plot_scatter(ivory_coast_table, "Côte d'Ivoire", 'ivory_coast_yield_plot.png')

    plot_bar(ghana_table, 'Ghana', 'ghana_area_harvested_plot.png')
    plot_bar(ivory_coast_table, "Côte d'Ivoire", 'ivory_coast_area_harvested_plot.png')

    print("Generated all plots successfully.")


def create_country_table(df):

    table = df.pivot_table(index='Year', columns='Element', values='Value')
    table = table.reset_index()
    table = table[['Year', 'Area harvested', 'Yield', 'Production']]
    return table


def plot_scatter(df, country_name, filename):

    plt.figure(figsize=(10, 5))
    plt.scatter(df['Year'], df['Yield'])
    plt.title(f'Cocoa Yield in {country_name} over the Years')
    plt.xlabel('Year')
    plt.ylabel('Yield (tonnes/ha)')
    plt.grid(True)
    plt.savefig(filename)
    plt.close()


def plot_bar(df, country_name, filename):

    plt.figure(figsize=(12, 6))
    plt.bar(df['Year'], df['Area harvested'])
    plt.title(f'Area Harvested for Cocoa in {country_name}')
    plt.xlabel('Year')
    plt.ylabel('Area Harvested (ha)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()


def main():

    analyze_cocoa_data()


if __name__ == '__main__':
    main()
