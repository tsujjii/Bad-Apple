import os
import time
import fpstimer
from tqdm import tqdm
from playsound import playsound
from image_converting import get_list
from pynput.keyboard import Key, Controller
from create_directory_with_frames import get_frames_from_video


if __name__ == "__main__":
    keyboard = Controller()

    confirm_full_screen = input("Full screen? Y/n: ")
    confirm_sound = input("Tocar música? Y/n: ")
    
    if confirm_full_screen.lower() == 'y':
        keyboard.press(Key.f11)
        keyboard.release(Key.f11)

    get_frames_from_video()

    # Busca a lista com os nomes dos frames
    directory = "frames"
    list_with_frame_names = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            list_with_frame_names.append([filename, int(filename[0:-4])])

    # Ordenar a lista de forma crescente
    list_with_frame_names = sorted(list_with_frame_names, key=lambda x: x[1])

    # Calcula os frames de saída
    out_list = []
    columns, rows = os.get_terminal_size()
    for i in tqdm(list_with_frame_names, desc="Organizando frames.", position=0, leave=True, ncols=100):
        out_list.append(get_list("frames/" + i[0], columns, rows))
    print("Finalizado")
    time.sleep(1)

    if confirm_sound.lower() == 'y':
        audio_file = "bad_apple_audio.mp3"
        playsound(audio_file, False)

    FPS = 30
    timer = fpstimer.FPSTimer(FPS)
    num_of_frames = len(list_with_frame_names)
    for i in range(num_of_frames):
        print(out_list.pop(0), end='')
        timer.sleep()

    time.sleep(5)
