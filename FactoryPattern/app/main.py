from abstract_classes import ExporterFactory
from factory import choose_quality


def main(factory: ExporterFactory):
    factory.get_audio_exporter().prepare_audio("SOME_AUDIO_DATA")
    factory.get_video_exporter().prepare_export("SOME_AUDIO_DATA")
    factory.get_audio_exporter().do_export("SOME_VIDEO_DATA")
    factory.get_video_exporter().do_export("SOME_VIDEO_DATA")


quality = choose_quality('high')

main(quality)
