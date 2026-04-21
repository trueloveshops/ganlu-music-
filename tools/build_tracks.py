from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
MUSIC_DIR = ROOT / "music"
OUT = ROOT / "tracks.json"

AUDIO_EXTS = {".mp3", ".wav", ".m4a", ".aac", ".ogg", ".flac"}

def display_name(path: Path) -> str:
    return path.stem

def category_name(path: Path) -> str:
    rel = path.relative_to(MUSIC_DIR)
    parts = rel.parts
    if len(parts) >= 3:
        return parts[-2]
    return parts[0]

tracks = []
if MUSIC_DIR.exists():
    for file in sorted(MUSIC_DIR.rglob("*")):
        if file.is_file() and file.suffix.lower() in AUDIO_EXTS:
            rel = file.relative_to(ROOT).as_posix()
            tracks.append({
                "title": file.name,
                "display": display_name(file),
                "category": category_name(file),
                "file": rel
            })

OUT.write_text(json.dumps(tracks, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {len(tracks)} tracks to {OUT}")
