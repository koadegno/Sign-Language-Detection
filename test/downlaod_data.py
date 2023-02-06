from lsfb_dataset.visualisation.video import VideoPlayer
from os import path
import pandas as pd

from lsfb_dataset.utils.download.dataset_downloader import DatasetDownloader

downloader = DatasetDownloader(
    "./data/subset",
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