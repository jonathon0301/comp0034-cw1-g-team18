import pandas as pd

# Load dataset
df = pd.read_csv('src/gender_pay_gap_dash_app/data/gender_pay_gap_prepared.csv')
print(df)

# Manually update UK region geographical locations
regions = ['London', 'South East', 'East of England', 'North West',
           'West Midlands', 'Yorkshire and The Humber', 'East Midlands', 'South West',
           'North East', 'Wales', 'Scotland', 'Northern Ireland']

longitudes = [-0.1277583, 0.6830127, 0.8591270, -2.6779086, -1.890401, -1.2802699, -1.3002699, -3.2027699,
              -1.6002699, -3.2027699, -4.2027699, -5.90827699]

latitudes = [51.5073509, 51.0834196, 52.240477, 53.4807593, 52.486243, 53.7996396, 52.9653566, 51.2703623,
             55.0428371, 51.5, 56.4907, 54.597285]

coord_df = pd.DataFrame({'UK region': regions, 'Longitude': longitudes, 'Latitude': latitudes})

print(coord_df)

# Integrate coordinates to the original dataset
df = df.merge(coord_df, on='UK region')
print(df.isnull().sum())

# Group_by Uk region
grouped = df.groupby('UK region')

# Calculate results of diff hourly percent
result_hourly_percent = grouped['DiffMeanHourlyPercent'].agg(['mean', 'median', lambda x: x.quantile(0.25), lambda x: x.quantile(0.75)])

# Merge the grouped stats of hourly percent with original data
result_hourly_percent = result_hourly_percent.reset_index()
result_hourly_percent = result_hourly_percent.merge(df[['UK region', 'Longitude', 'Latitude']].drop_duplicates(),
                                                    on='UK region')
# Rename columns
result_hourly_percent.columns = ['UK region', 'mean_diff_hourly_percent', 'median_diff_hourly_percent',
                                 'lower_quartile_hourly_percent', 'upper_quartile_hourly_percent', 'Longitude',
                                 'Latitude']
print(result_hourly_percent)

result_hourly_percent.to_csv('src/gender_pay_gap_dash_app/data/df_hourly_percent_on_region')












