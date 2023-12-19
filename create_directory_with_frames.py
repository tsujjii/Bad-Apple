import cv2
import os
from tqdm import tqdm


def get_frames_from_video():
    directory_name = "frames"
    os.mkdir(directory_name) if not os.path.exists(directory_name) else ""
    vid_cap = cv2.VideoCapture("video.mp4")
    total_frames = int(vid_cap.get(cv2.CAP_PROP_FRAME_COUNT))
    success, image = vid_cap.read()

    print("Verificando integridade dos frames")
    # Inicializa a barra de progresso
    progress_bar = tqdm(total=total_frames, desc="Verificando frames", position=0, leave=True, ncols=100)
    for i in range(total_frames):
        # Salva o frame em um arquivo JPEG
        if not os.path.exists(f"{directory_name}/{i}.jpg") and success:
            cv2.imwrite(f"{directory_name}/{i}.jpg", image)
            progress_bar.set_description(f"Criado frame: {i}")
        
        success, image = vid_cap.read()
        progress_bar.update(1)

    progress_bar.close()
    vid_cap.release()