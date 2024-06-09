import numpy as np
import pygame
import pygame.sndarray

def generate_sound(frequency, duration):
    sample_rate = 44100
    time_points = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.sin(2 * np.pi * frequency * time_points)
    normalized_signal = (signal * 32767).astype(np.int16)  # Convert the signal to 16-bit integers
    return pygame.sndarray.make_sound(normalized_signal.reshape(-1, 1))

def main():
    pygame.init()
    frequency = 440  # Sound frequency in Hz
    duration = 1  # Sound duration in seconds
    sound = generate_sound(frequency, duration)
    sound.play()
    pygame.time.wait(int(duration * 1000))  # Wait for the sound to finish

if __name__ == "__main__":
    main()
