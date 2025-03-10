import requests
import json
import matplotlib.pyplot as plt

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"

try:
    response = requests.get(url)  # GET-запрос
    response.raise_for_status()  # Проверка

    # Парсинг JSON данных
    data = response.json()

except requests.exceptions.RequestException as e:
    print(f"Ошибка при запросе данных: {e}")
    exit()

#Извлечение инфы з
earthquakes = data['features']


longitudes = []
latitudes = []
magnitudes = []
places = []

#Обработка каж з.
for eq in earthquakes:
    props = eq['properties']
    geometry = eq['geometry']


    longitudes.append(geometry['coordinates'][0])
    latitudes.append(geometry['coordinates'][1])

    # Извлечение
    magnitudes.append(props['mag'])
    places.append(props['place'])

# 5. Создание визуализации
plt.figure(figsize=(12, 8))  # Размер графика

# Создание scatter plot
scatter = plt.scatter(
    x=longitudes,
    y=latitudes,
    s=[m*5 for m in magnitudes],
    c=magnitudes,  # Цвет
    alpha=0.9,
    cmap='viridis'  # Цветовая схема
)

plt.colorbar(scatter, label='Магнитуда')
plt.title('Землетрясения за последние 30 дней', fontsize=14)
plt.xlabel('Долгота', fontsize=12)
plt.ylabel('Широта', fontsize=12)
plt.grid(True, alpha=0.3)


plt.show()