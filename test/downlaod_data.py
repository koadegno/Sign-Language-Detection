from lsfb_dataset.visualisation.video import VideoPlayer
from os import path
import pandas as pd

from lsfb_dataset.utils.download.dataset_downloader import DatasetDownloader

def donwload_isol_video():
    downloader = DatasetDownloader(
    "./data/subset/isol",
    include_video=True,
    split='test',
    )
    downloader.download()

def download_cont_video():
    downloader = DatasetDownloader(
    "./destination/folder",
    dataset="cont",
    split='test',       # Only download the 'test' subset of the dataset
    landmarks=[         # Choose landmarks. default is pose and hands
        'pose',
        'hands',
        'face'
    ],
    include_raw=True,   # Also download raw landmarks (without interpolation and smoothing)
    include_video=True,
    )
    downloader.download()

if __name__ == "__main__":
    #download_cont_video()
    donwload_isol_video()
