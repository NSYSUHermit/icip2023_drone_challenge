@echo off
setlocal
set video_path=D:\Projects\ICIP2023_CHANLLENGE\flight-mbg02\avi\video02.avi
set save_path=D:\\Projects\\ICIP2023_CHANLLENGE\\flight-mbg02\\avi\\photos\\
python video_to_frames.py --video_path %video_path% --save_path %save_path%


python video_to_frames.py --video_path D:\Projects\ICIP2023 CHANLLENGE\flight-mbg02\avi\video02.avi --save_path D:\Projects\ICIP2023 CHANLLENGE\flight-mbg02\avi\photos