from lsfb_dataset.visualisation.video import VideoPlayer
from os import path
import pandas as pd

from lsfb_dataset.utils.download.dataset_downloader import DatasetDownloader

downloader = DatasetDownloader(
    "./data/subset/isol",
    include_video=True,
    split='test',
)
downloader.download()