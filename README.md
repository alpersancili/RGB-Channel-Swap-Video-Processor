#RGB Channel Swap Video Processor

This project demonstrates a frame-level video transformation using OpenCV in Python. It processes a video by reading each frame, converting the BGR color space (used internally by OpenCV) to the RGB color space, and writes the transformed video to disk. A Gradio interface powers the interactive front end.

🌐 Live Demo

[🚀 Try it on Hugging Face Spaces](https://huggingface.co/spaces/Alpersx/RGB-Channel-Swap-Video-Processor)

🧠 Technical Overview

🔹 1. Video Input Handling

The input video is read with cv.VideoCapture()

Metadata is extracted:

FPS (frames per second)

Width and Height for frame resolution

Codec set via cv.VideoWriter_fourcc(*"mp4v") for .mp4 output

🔹 2. Frame-by-Frame RGB Conversion

Each frame is converted from BGR to RGB using:

b, g, r = cv.split(frame)

rgb_frame = cv.merge((r, g, b))

This manual swap gives more control than cv.cvtColor(), useful for educational or experimental purposes.

🔹 3. Output Video Writing

Output is written using cv.VideoWriter

Preserves original FPS and resolution

Uses MPEG-4 encoding

🔹 4. Gradio Interface

Gradio handles:

Video upload

Calling the processing function

Displaying the processed video in the UI

🔁 Frame Processing Pipeline

Input .mp4 video
      |
[OpenCV VideoCapture]
      |
  Read frame (BGR)
      |
Split channels → (B, G, R)
      |
Merge channels → (R, G, B)
      |
Write frame to output video
      |
  Repeat until done
      ↓
Output .mp4 video (RGB)

🛠️ Installation

Requirements

opencv-python

numpy

gradio

git clone https://github.com/YOUR_USERNAME/rgb-video-processor.git

cd rgb-video-processor

pip install -r requirements.txt

python app.py

📁 File Structure

.
├── app.py                # Main application script
├── requirements.txt      # Python dependencies
└── car_output.mp4        # Example output video (optional)

🔮 Possible Extensions

Add real-time preview of frames

Enable cv.cvtColor() option for comparison

Apply additional filters (e.g., edge detection, blurring)

Measure frame processing time

Batch video support

🤝 Contributing

Feel free to fork the repo and submit PRs with improvements or new features!
