# PixelPerfect

*Elevate your images: make every shot pixel perfect.*

Built at a hackathon after one too many evenings scrolling through near-identical photos, PixelPerfect ranks a set of images and returns the best ones.

## How it works

- **Blur:** converts each image to grayscale and applies a Laplacian filter. The filter measures how quickly brightness changes, so low values mean a blurry photo (`blurry.py`).
- **Faces and eyes:** uses computer vision to find faces and check whether eyes are open (`eyes_status.py`).
- **Quality:** also considers lighting (`lighting.py`) and resolution (`resolution.py`).

## Run it locally

```bash
pip install -r requirements.txt
streamlit run draft1.py
```

## Tech stack

Python, OpenCV and Streamlit, deployed on an AWS EC2 instance.

## Team

Built by [Vivek Manoj](https://github.com/viv500), Lakshit Luhadia and Sunil Mamu.

## What's next

- Rating video quality using frame rate, audio and resolution
- Recognizing friends in photos and suggesting who to send them to
