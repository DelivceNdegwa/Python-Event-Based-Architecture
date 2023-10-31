import pathlib
from abstract_classes import AudioExporter


class AACAudioExporter(AudioExporter):
    """AAC format: Fast exporting"""
    def prepare_audio(self, audio_data):
        print(f"Preparing audio for export in fast AAC format. \
            DATA={audio_data}")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting low quality audio to folder {folder}")


class WAVAudioExporter(AudioExporter):
    """WAV format: Slow, quality exporting"""
    def prepare_audio(self, audio_data):
        print(f"Preparing audio for slow & quality exportation in WAV format \
            {audio_data}")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting high quality audio to {folder}")
