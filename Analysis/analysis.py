import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных для Долины Смерти
dv_data = pd.read_csv('death_valley_2018_full.csv', parse_dates=['DATE'])
# Загрузка данных для Ситки
sitka_data = pd.read_csv('sitka_weather_2018_full.csv', parse_dates=['DATE'])

# Для Долины Смерти
dv_data = dv_data.dropna(subset=['TMAX', 'TMIN'])
dv_data['TMAX'] = pd.to_numeric(dv_data['TMAX'], errors='coerce')
dv_data['TMIN'] = pd.to_numeric(dv_data['TMIN'], errors='coerce')

# Для Ситки
sitka_data = sitka_data.dropna(subset=['TMAX', 'TMIN'])
sitka_data['TMAX'] = pd.to_numeric(sitka_data['TMAX'], errors='coerce')
sitka_data['TMIN'] = pd.to_numeric(sitka_data['TMIN'], errors='coerce')

# Найдем глобальные минимум и максимум для обеих локаций
global_min = min(dv_data['TMIN'].min(), sitka_data['TMIN'].min())  # Убрали .min()
global_max = max(dv_data['TMAX'].max(), sitka_data['TMAX'].max())  # Убрали .max()

plt.figure(figsize=(12, 6))

# График для Долины Смерти
plt.subplot(1, 2, 1)
plt.plot(dv_data['DATE'], dv_data['TMAX'], c='red', alpha=0.5, label='Максимум')
plt.plot(dv_data['DATE'], dv_data['TMIN'], c='blue', alpha=0.5, label='Минимум')
plt.fill_between(dv_data['DATE'], dv_data['TMIN'], dv_data['TMAX'], facecolor='blue', alpha=0.1)
plt.title('Долина Смерти, 2018')
plt.xlabel('Дата')
plt.ylabel('Температура (°F)')
plt.ylim(global_min - 5, global_max + 5)  # Общий масштаб
plt.legend()

# График для Ситки
plt.subplot(1, 2, 2)
plt.plot(sitka_data['DATE'], sitka_data['TMAX'], c='red', alpha=0.5, label='Максимум')
plt.plot(sitka_data['DATE'], sitka_data['TMIN'], c='blue', alpha=0.5, label='Минимум')
plt.fill_between(sitka_data['DATE'], sitka_data['TMIN'], sitka_data['TMAX'], facecolor='blue', alpha=0.1)
plt.title('Ситка, 2018')
plt.xlabel('Дата')
plt.ylabel('Температура (°F)')
plt.ylim(global_min - 5, global_max + 5)  # Общий масштаб
plt.legend()

plt.tight_layout()
plt.show()