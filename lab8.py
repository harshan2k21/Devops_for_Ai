import pandas as pd
from prophet import Prophet

df = pd.read_csv('powerconsumption.csv', sep=',', parse_dates=['Datetime'])

power_columns = ['PowerConsumption_Zone1', 'PowerConsumption_Zone2', 'PowerConsumption_Zone3']

def prophet_forecast(data, column, future_steps):
    prophet_data = data[['Datetime', column]].rename(columns={'Datetime': 'ds', column: 'y'})
    model = Prophet()
    model.fit(prophet_data)
    future = model.make_future_dataframe(periods=future_steps, freq='10T')
    forecast = model.predict(future)
    return forecast[['ds', 'yhat']]

future_steps = 24 * 6

forecasts = {}
for column in power_columns:
    forecasts[column] = prophet_forecast(df, column, future_steps)

future_df = pd.DataFrame()
future_df['Datetime'] = forecasts[power_columns[0]]['ds']
for column in power_columns:
    future_df[column] = forecasts[column]['yhat']

future_df.set_index('Datetime', inplace=True)
future_df = future_df.iloc[-future_steps:]

print("Forecast for the next 24 hours")
print(future_df)
