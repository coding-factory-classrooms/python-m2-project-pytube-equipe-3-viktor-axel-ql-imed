from typing import Optional
from dataclasses import dataclass
import mutagen


@dataclass
class VideoMetadata:
    duration: int = 0


def extract_metadata(file_path: str) -> Optional[VideoMetadata]:
    try:
        metadata = mutagen.File(file_path)
        duration = int(metadata.info.length)
        song_meta = VideoMetadata(duration=duration)
        return song_meta
    except:
        pass

    return None
