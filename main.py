import argparse
from pathlib import Path
from audio_pipeline.effects import ds_create

def main():
    parser = argparse.ArgumentParser(description="Audio Dataset Processor")
    parser.add_argument('--dirname', type=str, required=True, help='Directory containing audio files')
    args = parser.parse_args()

    ds_create(Path(args.dirname))

if __name__ == '__main__':
    main()