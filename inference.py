import sys
import shutil
from ultralytics import YOLO
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Usage: python inference.py <source>")
        sys.exit(1)

    source_path = Path(sys.argv[1])
    if not source_path.exists():
        print(f"Error: Source path not found: {source_path}")
        sys.exit(1)

    model = YOLO("./model.pt")

    result_dir = Path("results")
    result_dir.mkdir(parents=True, exist_ok=True)

    try:
        results = model.predict(source=str(source_path), conf=0.25, save=True)
        latest_predict_folder = sorted(Path("runs/detect").glob("predict*"), key=lambda x: x.stat().st_ctime, reverse=True)[0]
        
        for file in latest_predict_folder.iterdir():
            if file.is_file():
                shutil.copy(file, result_dir)
    except Exception as e:
        print(f"Error during inference: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
