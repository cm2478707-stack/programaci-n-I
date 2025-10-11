import time

def reloj():
    for horas in range(1):
        for minutos in range(60):
            for segundos in range(60):
                print(horas, ":", minutos, ":", segundos)
                time.sleep(1)

if __name__ == "__main__":
    reloj()
