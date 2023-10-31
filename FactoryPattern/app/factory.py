import audio_exporter
import video_exporter
from abstract_classes import AudioExporter, ExporterFactory, VideoExporter


class HighQualityExporter(ExporterFactory):
    def get_audio_exporter(self) -> AudioExporter:
        return audio_exporter.WAVAudioExporter()

    def get_video_exporter(self) -> VideoExporter:
        return video_exporter.LosslessVideoExporter()


class MediumQualityExporter(ExporterFactory):
    def get_audio_exporter(self) -> AudioExporter:
        return audio_exporter.WAVAudioExporter()

    def get_video_exporter(self) -> VideoExporter:
        return video_exporter.H264BVideoExporter()


class LowQualityExporter(ExporterFactory):
    def get_audio_exporter(self) -> AudioExporter:
        return audio_exporter.AACAudioExporter()

    def get_video_exporter(self) -> VideoExporter:
        return video_exporter.Hi422PVideoExporter()


def choose_quality(quality: str) -> ExporterFactory:
    qualities = {
        'low': LowQualityExporter,
        'medium': MediumQualityExporter,
        'high': HighQualityExporter,
        'higher': HighQualityExporter
    }
    while True:
        if quality in qualities:
            return qualities[quality]()
        print("Input a valid option")
