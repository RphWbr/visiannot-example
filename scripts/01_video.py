# -*- coding: utf-8 -*-

from visiannot.visiannot import ViSiAnnoT

# video path
dir_vid = "../data/video"
path_video = "%s/vid_2021-06-21T15-15-00.mp4" % dir_vid

# video configuration
video_dict = {}
video_dict["vid_0"] = [path_video, '_', 1, "%Y-%m-%dT%H-%M-%S"]

# create ViSiAnnoT window
win_visiannot = ViSiAnnoT(video_dict, {})
