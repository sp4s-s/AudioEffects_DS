
---

```markdown
# Audio Dataset Processor 🎶

## Overview
The Audio Dataset Processor is a modular Python package designed to transform your audio files into smaller chunks, apply a set of audio effects (pitch shift, time stretch, and noise addition), and generate comprehensive metadata in JSON and CSV formats. Whether you are a data scientist, sound engineer, or audio enthusiast, this pipeline offers a flexible solution to pre-process your audio datasets with minimal effort. 

> “Supports `.wav`, `.mp3`, and `.flac` formats. Default sampling rate is preserved from original files.”
- [ Can Supoort other formats though ]

## Folder Structure Diagram
The project is organized as follows:

```plaintext
project/
├── main.py
├── audio_pipeline/
│   ├── __init__.py
│   ├── effects.py
│   ├── io_utils.py
│   └── processor.py
├── requirements.txt
└── README.md
```

- **main.py**: CLI entry point for running the processor.
- **audio_pipeline/**: Package containing all modules.
  - **effects.py**: Functions for applying audio effects.
  - **io_utils.py**: I/O utilities including file saving (with progress bars using `tqdm`).
  - **processor.py**: Main processing logic to generate chunks, apply effects, and create metadata.
- **requirements.txt**: Lists all dependencies.
- **README.md**: This documentation.

## Getting Started 🚀

### Installation
Make sure to have Python installed (preferably Python 3.6+). Then, install the required Python packages:

```bash
pip install -r requirements.txt
```

### Usage
To run the processor, open your terminal and execute:

```bash
python main.py --dirname <path-to-audio-dir>
```

Replace `<path-to-audio-dir>` with the directory where your audio files reside. The processor will:
- Split audio files into chunks (saved in the `clips/` directory),
- Apply random audio effects (saved in the `effects/` directory),
- Generate `labels.json` and `labels.csv` containing processing details and metadata.

## Detailed Functionality

### Processing Pipeline
1. **Audio Splitting**:
   - Audio files are sliced into chunks of random durations (between 3 and 10 seconds).
   - Timestamps (start and end samples) are stored for each chunk.

2. **Audio Effects**:
   - Three types of effects are applied:
     - **Pitch Shift**: Alters the pitch by a random number of semitones.
     - **Time Stretch**: Modifies the speed of the audio.
     - **Add Noise**: Introduces a noise factor to simulate different acoustic conditions.
     
   The effects are applied based on a randomized selection for each chunk.

3. **Metadata Generation**:
   - The pipeline generates JSON and CSV files containing file indices, applied effects, chunk time stamps, and file paths.

> “The power of this processor lies in its modularity and ease of customization. Change a module, change the world!”

## Customizing the Directory Structure 🔧

If you need to change where outputs are saved or want to restructure the project directories, here are the key places to modify:

- **Changing Output Directories**:
  - In `audio_pipeline/io_utils.py` within the functions `save_chunks()` and `apply_effects()`, you can change the hard-coded folder paths (`clips/` and `effects/`).
  - For example, to change the clips folder, edit:
    ```python
    def save_chunks(y_chunks, sr, base_name, path='clips/'):
    ```
    Replace `'clips/'` with your desired output folder (e.g., `'audio_chunks/'`).

- **Modifying the Package Structure**:
  - If you decide to change the internal package layout (e.g., moving modules into a subfolder), update the imports in `main.py` and adjust the relative import paths in `audio_pipeline/processor.py` and `audio_pipeline/io_utils.py`.

- **Extending Functionality**:
  - To add new audio effects, create functions in `audio_pipeline/effects.py` and then import them in `io_utils.py` (inside `apply_effects()`). Update the `available_effects` list in `audio_pipeline/processor.py` accordingly.

## Additional Notes 📝

- **Progress Feedback**: The pipeline uses `tqdm` for progress bars, providing feedback during I/O operations, which is particularly useful when processing large datasets.
- **Extensibility**: The modular design means you can easily integrate additional features like parallel processing or support for more audio formats.
- **Debugging & Logging**: For troubleshooting, consider adding logging statements or using a debugger in your favorite IDE.

With this tool, managing and transforming your audio datasets becomes a breeze! Dive in, tweak the settings, and let the code work its magic. Happy processing! 🎧

```



---
---

## Wrapping Up 🎉

You've now got a powerful, customizable toolbox at your fingertips. Whether you're an audio aficionado, a budding data scientist, or simply someone who loves exploring sound, this pipeline is built to expand and adapt to your creative needs. We’ve integrated intuitive progress feedback with `tqdm`, a clean modular architecture for easy modifications, and comprehensive metadata generation to keep all your experiments in check.

> “Innovation in audio starts with curiosity and a few lines of code.”  
> – The Sound Experimenter

This processor isn't just about splitting and augmenting audio files—it's a platform to experiment, learn, and turn your raw sounds into impactful insights. Tinker with the source, extend its functionality by adding new effects, or even tweak the directory structure to suit your workflow. Remember, the only limit is your imagination!

Dive into the code, unleash your creativity, and let your sound waves resonate with brilliance. Happy coding, and may every waveform bring you closer to perfection! 🎵


---
---

```
