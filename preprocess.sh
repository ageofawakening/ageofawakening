#!/bin/sh
#ffmpeg -i trailer.mp4 -filter_complex "crop=iw:80:0:406,chromahold=color=#FFFFFF" trailer_cropped.mp4
ffmpeg -i 觉醒年代.Age.of.Awakening_预告片.Trailer.mp4 -filter_complex "crop=608:80:0:406,eq=brightness=-0.5:contrast=3:saturation=2" trailer_cropped.mp4
