import numpy as np
import pathlib

noisy_dataset = np.loadtxt(
    pathlib.Path(__file__).parent / "../wifi_db/noisy_dataset.txt"
)
clean_dataset = np.loadtxt(
    pathlib.Path(__file__).parent / "../wifi_db/clean_dataset.txt"
)
