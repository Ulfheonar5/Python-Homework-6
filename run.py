import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

num_points = 1000
x_koordinat = np.random.randint(0, 1001, size=num_points)
y_koordinat = np.random.randint(0, 1001, size=num_points)

df = pd.DataFrame({
    'X': x_koordinat,
    'Y': y_koordinat
})

excel_path = r'C:\Users\murat\PycharmProjects\ODEV6\data.xlsx'
df.to_excel(excel_path, index=False)

# Excel dosyasını okuma
df = pd.read_excel(excel_path)

# Koordinatları alma
x_koordinat = df['X']
y_koordinat = df['Y']

# Izgara boyutunu belirleme
grid_size = 100

# Her bir ızgara boyutu için grafiği çizelim

plt.figure(figsize=(10, 10))

# Her bir hücreye rastgele bir renk atayalım
colors = np.random.rand(1001 // grid_size, 1001 // grid_size, 3)

for i in range(1001 // grid_size):
    for j in range(1001 // grid_size):
        mask = (x_koordinat >= i * grid_size) & (x_koordinat < (i + 1) * grid_size) & \
                (y_koordinat >= j * grid_size) & (y_koordinat < (j + 1) * grid_size)
        plt.scatter(x_koordinat[mask], y_koordinat[mask], color=colors[i, j], s=10)

plt.xticks(np.arange(0, 1001, grid_size))
plt.yticks(np.arange(0, 1001, grid_size))
plt.grid(True)

plt.xlabel('X Koordinatları')
plt.ylabel('Y Koordinatları')
plt.title(f'Rastgele Noktaların Dağılımı (Izgara Boyutu: {grid_size}x{grid_size})')
plt.show()