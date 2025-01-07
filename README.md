## Traffic Sign Recognition with YOLOv8

This project uses a YOLOv8 model 'yolov8s.pt' for detecting traffic signs. The model was trained on a dataset of traffic signs for **20 epochs** and utilizes the best-performing weights for inference. 

### Model Metrics (Validation Results):

| Class                    | Precision | Recall | F1-Score |
|--------------------------|-----------|--------|----------|
| all                      | 0.97      | 0.912  | 0.969    |
| Green Light              | 0.918     | 0.73   | 0.864    |
| Red Light                | 0.897     | 0.75   | 0.85     |
| Speed Limit 100          | 0.981     | 0.986  | 0.995    |
| Speed Limit 110          | 0.95      | 1      | 0.995    |
| Speed Limit 120          | 1         | 0.914  | 0.995    |
| Speed Limit 20           | 0.962     | 0.982  | 0.986    |
| Speed Limit 30           | 1         | 0.968  | 0.992    |
| Speed Limit 40           | 0.979     | 0.927  | 0.982    |
| Speed Limit 50           | 1         | 0.891  | 0.988    |
| Speed Limit 60           | 0.997     | 0.921  | 0.983    |
| Speed Limit 70           | 0.982     | 0.974  | 0.994    |
| Speed Limit 80           | 0.946     | 0.929  | 0.983    |
| Speed Limit 90           | 1         | 0.819  | 0.975    |
| Stop                     | 0.973     | 0.975  | 0.981    |

Dataset used: [Kaggle Traffic Sign Dataset](https://www.kaggle.com/datasets/pkdarabi/cardetection)

### How to Run Inference

To run inference on an image, video, or directory of files, follow the steps below:

1. Clone the repository:

```bash
git clone https://github.com/your-username/Traffic-Sign-Recognition.git
cd Traffic-Sign-Recognition
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the inference script:

```bash
python inference.py /path/to/images_or_videos
```
- **source**: Path to the input file(s) (image, video, or directory with them).
Results will be saved in the `results` folder, where the model’s predictions will be stored. The images will include detected labels and bounding boxes.
