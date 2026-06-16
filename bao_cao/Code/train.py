model = YOLO("yolo11m.pt")

results = model.train(
    data="/content/datasets/TSBOW/TSBOW.yaml",
    epochs=50,

    imgsz=1280,
    batch=8,
    workers=2,

    patience=10,
    device="0",
    project=output_dir,
    name="tsbow_run",
    exist_ok=True,

    lr0=0.001,
    lrf=0.01,
    freeze=10,

    close_mosaic=10,
    augment=True
)