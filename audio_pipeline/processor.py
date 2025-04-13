import json
import csv
import numpy as np
from pathlib import Path
from itertools import chain
from tqdm import tqdm
import librosa

from .io_utils import save_chunks, apply_effects

def split(y, sr, min_duration=3, max_duration=10, n_chunks=5):
    chunks = []
    out = {}
    for i in range(n_chunks):
        max_samples = sr * max_duration
        start = np.random.randint(0, len(y) - max_samples) if len(y) - max_samples > 0 else 0
        chunk_duration = np.random.randint(sr * min_duration, sr * max_duration)
        end = min(start + chunk_duration, len(y))
        chunks.append(y[start:end])
        out[i] = (start, end)
    return chunks, out

def ds_create(path: Path, output_json='labels.json', output_csv='labels.csv'):
    files = list(chain(path.glob('*.wav'), path.glob('*.mp3'), path.glob('*.flac')))
    if not files:
        print("No files found")
        return
    print(f"Found {len(files)} files")
    label = {}
    for idx, file in enumerate(tqdm(files, desc="Processing files")):
        available_effects = ["pitchify", "time_stretch", "noise"]
        n_effects = np.random.randint(1, 4)
        chosen_effects = list(np.random.choice(available_effects, n_effects, replace=False))
        y, sr = librosa.load(file, sr=None)
        chunks, time_stamps = split(y, sr, min_duration=3, max_duration=10, n_chunks=5)
        chunk_paths = []
        effect_file_outputs = []
        for i, (chunk, ts) in enumerate(zip(chunks, time_stamps.values())):
            chunk_base = f"{file.stem}_chunk{i}"
            chunk_out_path = save_chunks([chunk], sr, chunk_base)
            chunk_effect_files = apply_effects(chunk, chosen_effects, chunk_base)
            chunk_paths.append(chunk_out_path)
            effect_file_outputs.append(chunk_effect_files)
        label[str(file)] = {
            "Index": idx,
            "File": str(file),
            "Effects Applied": chosen_effects,
            "Chunk Time Stamps (samples)": time_stamps,
            "Chunk Paths": chunk_paths,
            "Effect File Outputs": effect_file_outputs,
        }
    with open(output_json, 'w') as jf:
        json.dump(label, jf, indent=4)
    print(f"Labels saved to {output_json}")
    with open(output_csv, 'w', newline='') as cf:
        writer = csv.writer(cf)
        writer.writerow(["Index", "File", "Effects Applied", "Chunk Time Stamps (samples)", "Chunk Paths", "Effect File Outputs"])
        for data in label.values():
            writer.writerow([
                data["Index"],
                data["File"],
                '|'.join(data["Effects Applied"]),
                str(data["Chunk Time Stamps (samples)"]),
                str(data["Chunk Paths"]),
                str(data["Effect File Outputs"])
            ])
    print(f"Labels saved to {output_csv}")
