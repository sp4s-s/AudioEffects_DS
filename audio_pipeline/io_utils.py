from pathlib import Path
import soundfile as sf
from tqdm import tqdm

def save_chunks(y_chunks, sr, base_name, path='clips/'):
    chunk_paths = {}
    Path(path).mkdir(parents=True, exist_ok=True)
    for i, chunk in enumerate(tqdm(y_chunks, desc=f"Saving chunks for {base_name}")):
        filename = f'{base_name}_chunk_{i}.wav'
        full_path = Path(path) / filename
        sf.write(full_path, chunk, sr)
        chunk_paths[i] = str(full_path)
    return chunk_paths

def apply_effects(y, effects, base_name, sr=44100, path='effects/'):
    from .effects import pitchify, stretch_time, add_noise

    file_names = []
    Path(path).mkdir(parents=True, exist_ok=True)
    for i, effect in enumerate(tqdm(effects, desc=f"Applying effects for {base_name}")):
        y_mod = y.copy()
        if effect == "pitchify":
            y_mod = pitchify(y_mod, sr)
        elif effect == "time_stretch":
            y_mod = stretch_time(y_mod)
        elif effect == "noise":
            y_mod = add_noise(y_mod)
        else:
            continue
        filename = f"{base_name}_{effect}_{i}.wav"
        full_path = Path(path) / filename
        sf.write(full_path, y_mod, sr)
        file_names.append(str(full_path))
    return file_names