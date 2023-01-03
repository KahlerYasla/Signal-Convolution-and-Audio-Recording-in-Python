import numpy as np
import matplotlib.pyplot as plt
import sounddevice
from scipy.io.wavfile import write

# part0 both f0 and f1 functions are for convolve but f1 results faster


def f0(x0, y0):

    y0 = y0[::-1]

    return [
        np.dot(x0[max(0, i):min(i+len(y0), len(x0))],
               y0[max(-i, 0):len(x0)-i*(len(x0)-len(y0) < i)])

        for i in range(1-len(y0), len(x0))
    ]


def f1(x, y, n, m):
    c = np.zeros(n + m - 1)
    for i in range(n):
        print(round((i/n)*100), "%")
        for j in range(m):
            c[i + j] += (x[i] * y[j])
    return c

# part1


sizeX = int(input("Enter the size for x: "))
sizeY = int(input("Enter the size for y: "))

x = np.array([])
y = np.array([])

for i in range(sizeX):
    x = np.append(x, float(input("Enter elements for x: ")))

for i in range(sizeY):
    y = np.append(y, float(input("Enter elements for y: ")))

xZero = float(input("Enter the zero point of x: "))
yzero = float(input("Enter the zero point of y: "))

arrMine = f1(x, y, sizeX, sizeY)
arrComp = np.convolve(x, y, 'full')

# part2

print(arrMine)
print(arrComp)

fig, axis = plt.subplots(2)

axis[0].stem(arrMine)
axis[1].stem(arrComp)

plt.show()

# part3

fs = 22550
sounddevice.default.samplerate = fs
sounddevice.default.channels = 1

input("\nPress Enter To Start 5 seconds recording\n")
print("recording...\n")

v0 = sounddevice.rec(int(5 * fs))
sounddevice.wait()
sounddevice.play(v0)
write("5sec.wav", fs, v0)

print("End Of Recording\n")

input("Press Enter To Start 10 seconds recording\n")
print("recording...\n")

v1 = sounddevice.rec(int(10 * fs))
sounddevice.wait()
sounddevice.play(v1)
write("10sec.wav", fs, v1)

print(v0)
print(v1)

int(input("End Of Record-Play part to resume type any number\n"))

# part4

resCMP5_2 = np.array([])
resSelin5_2 = np.array([])
resCMP5_3 = np.array([])
resSelin5_3 = np.array([])
resCMP5_4 = np.array([])
resSelin5_4 = np.array([])

resCMP10_2 = np.array([])
resSelin10_2 = np.array([])
resCMP10_3 = np.array([])
resSelin10_3 = np.array([])
resCMP10_4 = np.array([])
resSelin10_4 = np.array([])

for i in range(2, 5):

    A = 0.8
    arr0 = np.zeros(i * 400 + 1)

    for j in range(0, i * 400 + 1, 400):
        arr0[j] += A * j / 400
    arr0[0] = 1

    plt.show()

    if (i == 2):
        print(
            "Convulating for 5 second record and this may take some time.\nPlease wait...\n")

        resSelin5_2 = f1(v0, arr0, len(v0), len(arr0))
        resCMP5_2 = np.convolve(v0[:, 0], arr0)

        print("Convulating for 10 second record and this may take some time.\nPlease wait...\n")

        resSelin10_2 = f1(v1, arr0, len(v1), len(arr0))
        resCMP10_2 = np.convolve(v1[:, 0], arr0)

    elif (i == 3):
        print(
            "Convulating for 5 second record and this may take some time.\nPlease wait...\n")

        resSelin5_3 = f1(v0, arr0, len(v0), len(arr0))
        resCMP5_3 = np.convolve(v0[:, 0], arr0)

        print("Convulating for 10 second record and this may take some time.\nPlease wait...\n")

        resSelin10_3 = f1(v1, arr0, len(v1), len(arr0))
        resCMP10_3 = np.convolve(v1[:, 0], arr0)

    elif (i == 4):
        print(
            "Convulating for 5 second record and this may take some time.\nPlease wait...\n")

        resSelin5_4 = f1(v0, arr0, len(v0), len(arr0))
        resCMP5_4 = np.convolve(v0[:, 0], arr0)

        print("Convulating for 10 second record and this may take some time.\nPlease wait...\n")

        resSelin10_4 = f1(v1, arr0, len(v1), len(arr0))
        resCMP10_4 = np.convolve(v1[:, 0], arr0)

sel0 = int(
    input("to set an example: Enter 1 to 5sec ; 2 to 10sec concluded records\n"))

if (sel0 == 1):

    print("Playing the code based sound... \n")

    sounddevice.play(resSelin5_2)
    sounddevice.wait()

    print("Playing computer based sound... \n")

    sounddevice.play(resCMP5_2)
    sounddevice.wait()

elif (sel0 == 2):

    print("Playing the code based sound... \n")

    sounddevice.play(resSelin10_2)
    sounddevice.wait()

    print("Playing computer based sound... \n")

    sounddevice.play(resCMP10_2)
    sounddevice.wait()

figure, axis = plt.subplots(3, 4)

titles = [("M={}; 5 second", "M={}; 10 second", "M={}; 5 second numpy",
           "M={}; 10 second numpy") for M in range(2, 5)]

for i, (M, title_tuple) in enumerate(zip(range(2, 5), titles)):
    axis[i, 0].stem(f"resSelin5_{M}")
    axis[i, 0].set_title(title_tuple[0].format(M))
    axis[i, 1].stem(f"resSelin10_{M}")
    axis[i, 1].set_title(title_tuple[1].format(M))
    axis[i, 2].stem(f"resCMP5_{M}")
    axis[i, 2].set_title(title_tuple[2].format(M))
    axis[i, 3].stem(f"resCMP10_{M}")
    axis[i, 3].set_title(title_tuple[3].format(M))

figure.tight_layout()
plt.show()
