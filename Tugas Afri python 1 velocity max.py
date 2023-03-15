import math

# Variabel awal
y0 = 1   # ketinggian awal (m)
v0 = 15  # kecepatan awal (m/s)
g = 9.8  # percepatan gravitasi (m/s^2)

# Inisialisasi list
t_list = []
y_list = []
v_list = []

# Hitung ketinggian dan kecepatan bola pada setiap saat
t = 0
while True:
    y = y0 + v0*t - 0.5*g*t**2
    v = v0 - g*t
    if y < 0:
        y = 0
        v = 0
    t_list.append(t)
    y_list.append(y)
    v_list.append(v)
    if y == 0:
        break
    t += 0.01  # waktu dihitung setiap 0.01 detik

# Cetak waktu, ketinggian, dan kecepatan bola
print("Waktu\tKetinggian\tKecepatan")
for i in range(len(t_list)):
    print("{:.2f}\t{:.2f}\t\t{:.2f}".format(t_list[i], y_list[i], v_list[i]))

# Hitung ketinggian maksimum dan kecepatan maksimum bola
y_max = max(y_list)
v_max = max(v_list)

# Cetak ketinggian maksimum dan kecepatan maksimum bola
print("Ketinggian maksimum: {:.2f} m".format(y_max))
print("Kecepatan maksimum: {:.2f} m/s".format(v_max))
