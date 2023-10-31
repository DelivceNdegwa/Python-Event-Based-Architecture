import pathlib
from abc import ABC, abstractmethod


class VideoExporter(ABC):

    @abstractmethod
    def prepare_export(self, video_data):
        """Prepare class for export"""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Do export here"""


class AudioExporter(ABC):
    @abstractmethod
    def prepare_audio(self, audio_data):
        """Audio exportation"""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Video exportation"""


class ExporterFactory(ABC):
    @abstractmethod
    def get_audio_exporter() -> AudioExporter:
        """Gets a selected audio exporter"""

    @abstractmethod
    def get_video_exporter() -> VideoExporter:
        """Get a selected video exporter"""
