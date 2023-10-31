import pathlib
from abstract_classes import VideoExporter


class LosslessVideoExporter(VideoExporter):
    """Lossless Exporting"""
    def prepare_export(self, video_data):
        print(f"(HIGH QUALITY VIDEO)---Preparing data \
            for lossless export. DATA={video_data}")

    def do_export(self, folder: pathlib.Path):
        print(f"(HIGH QUALITY VIDEO)Exporting video \
            in lossless format to {folder}")


class H264BVideoExporter(VideoExporter):
    """H.264 Exporting with codec with Baseline Profile"""
    def prepare_export(self, video_data):
        print(f"(MEDIUM QUALITY VIDEO)---Preparing data for \
            H.264 export. DATA={video_data}")

    def do_export(self, folder: pathlib.Path):
        print(f"(MEDIUM QUALITY VIDEO)Exporting video in \
            H.264 format into folder {folder}")


class Hi422PVideoExporter(VideoExporter):
    """Hi422P Exporting"""
    def prepare_export(self, video_data):
        print(f"(LOW QUALITY VIDEO)----Preparing data for \
            Hi422P export. DATA={video_data}")

    def do_export(self, folder: pathlib.Path):
        print(f"(LOW QUALITY VIDEO)Exporting video in \
            Hi422P format into folder {folder}")
