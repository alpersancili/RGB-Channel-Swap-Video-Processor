import cv2 as cv
import numpy as np
import gradio as gr
import os

def process_video(input_video):
    output_path="car_output.mp4"

    cap=cv.VideoCapture(input_video)
    fourcc=cv.VideoWriter_fourcc(*"mp4v") #Kodek
    fps=int(cap.get(cv.CAP_PROP_FPS)) #saniyedeki frame sayısı
    width=int(cap.get(cv.CAP_PROP_FRAME_WIDTH)) #genişlik
    height=int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)) #yükseklik
    out=cv.VideoWriter(output_path,fourcc,fps,(width,height))

    while cap.isOpened():
        ret,frame=cap.read()

        if not ret: #okuma başarılı ise
            break

        #renk kanallarını ayarla
        b,g,r=cv.split(frame)
        
        rgb_frame=cv.merge((r,g,b))
        out.write(rgb_frame) #videoya yaz

    cap.release()
    out.release()

    return output_path

gr.Interface(
    fn=process_video,
    inputs=gr.Video(label="Upload a video"),
    outputs=gr.Video(label="Processed Video Output"),
    title="RGB Channel Swap Video Processor",
    description="This app reads a video ,swaps the BGR to RGB channel, and shows the processed video.",
    allow_flagging="never" #Disable flag button
).launch()
