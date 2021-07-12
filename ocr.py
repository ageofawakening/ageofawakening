from videocr import save_subtitles_to_file

if __name__ == '__main__':  # This check is mandatory for Windows.
    save_subtitles_to_file('trailer_cropped.mp4',
                           file_path='觉醒年代.Age.of.Awakening_预告片.Trailer.zh.srt',
                           lang='chi_sim',
                           #time_end='00:01:28.820',
                           conf_threshold=60,
                           sim_threshold=100,
                           use_fullframe=True)
