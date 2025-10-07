import numpy as np
import matplotlib.pyplot as plt

# Parametreler
wavelength = 632e-9       # Dalga boyu (m)
d = 0.25e-3               # Yarıklar arası mesafe (m)
a = 0.05e-3               # Tek yarık genişliği (m)
I0 = 1                    # Maksimum şiddet
screen_distance = 1.0     # Ekran uzaklığı (m)
screen_width = 0.02       # Ekran genişliği (m)
num_points = 3000         # Nokta sayısı

# Ekran üzerindeki konumlar
x = np.linspace(-screen_width/2, screen_width/2, num_points)
theta = np.arctan(x / screen_distance)

# Kırınım ve girişim desenleri
beta = (np.pi * a * np.sin(theta)) / wavelength
delta = (np.pi * d * np.sin(theta)) / wavelength

# Tek yarık zarfı (sin(beta)/beta)^2
envelope = (np.sin(beta) / beta)**2
envelope[np.isnan(envelope)] = 1  # 0/0 durumlarını düzelt

# Çift yarık girişimi
interference = (np.cos(delta))**2

# Toplam şiddet
I = I0 * envelope * interference

# Grafik
plt.figure(figsize=(10, 5))
plt.plot(x * 1000, I, color='red', label='Çift Yarık Deseni')
plt.plot(x * 1000, envelope, 'k--', label='Tek Yarık Zarfı (Envelope)')
plt.title("Young Deneyi ")
plt.xlabel("Perdedeki konum (mm)")
plt.ylabel("Işık Şiddeti (bağıl)")
plt.legend()
plt.grid(True)
plt.show()
