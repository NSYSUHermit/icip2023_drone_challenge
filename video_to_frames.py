import cv2
import argparse
import os


class VideoToImageConverter:
    def __init__(self, video_path, save_path):
        self.video_path = video_path
        self.save_path = save_path

    def convert(self):
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

        cap = cv2.VideoCapture(self.video_path)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print(f"Total frames: {frame_count}")

        for i in range(frame_count):
            ret, frame = cap.read()
            if ret:
                image_path = os.path.join(self.save_path, f"frame_{i}.jpg")
                cv2.imwrite(image_path, frame)
                print(f"Processed frame {i + 1}/{frame_count}")
            else:
                print(f"Failed to read frame {i + 1}/{frame_count}")

        cap.release()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert a video to a series of images')
    parser.add_argument('--video_path', type=str, help='Path to the input video file', required=True)
    parser.add_argument('--save_path', type=str, help='Path to save the output images', required=True)
    args = parser.parse_args()

    converter = VideoToImageConverter(args.video_path, args.save_path)
    try:
        converter.convert()
    except Exception as e:
        print(f"Error occurred: {e}")