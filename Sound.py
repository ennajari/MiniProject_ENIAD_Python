import numpy as np
import pygame
import pygame.sndarray
def generate_sound(frequency, duration):
    sample_rate = 44100
    time_points = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.sin(2 * np.pi * frequency * time_points)
    normalized_signal = np.int16(signal * 32767)  # Convertir le signal en entiers 16 bits
    return pygame.sndarray.make_sound(normalized_signal.reshape(-1, 1))

def main():
    pygame.init()
    frequency = 440  # Fréquence du son en Hz
    duration = 1  # Durée du son en secondes
    sound = generate_sound(frequency, duration)
    sound.play()
    pygame.time.wait(int(duration * 1000))  # Attendre que le son se termine

if __name__ == "__main__":
    main()
