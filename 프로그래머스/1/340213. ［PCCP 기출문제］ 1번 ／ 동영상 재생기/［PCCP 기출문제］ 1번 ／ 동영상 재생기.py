from collections import deque

def time_to_seconds(time_str):
    minutes, seconds = map(int, time_str.split(':'))
    return minutes * 60 + seconds

def seconds_to_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f'{minutes:02}:{seconds:02}'

def solution(video_len, pos, op_start, op_end, commands):
    video_len_sec = time_to_seconds(video_len)
    pos_sec = time_to_seconds(pos)
    op_start_sec = time_to_seconds(op_start)
    op_end_sec = time_to_seconds(op_end)
    
    for command in commands:
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec
            
        if command == "prev":
            pos_sec = max(0, pos_sec - 10)
        elif command == "next":
            pos_sec = min(video_len_sec, pos_sec + 10)
        
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec
    
    return seconds_to_time(pos_sec)
