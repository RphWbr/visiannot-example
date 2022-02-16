from visiannot.visiannot import ViSiAnnoT

# video path
dir_vid = "../data/video"
path_video = "%s/vid_2021-06-21T15-16-00.mp4" % dir_vid

# video configuration
video_dict = {}
video_dict["vid_0"] = [path_video, '_', 1, "%Y-%m-%dT%H-%M-%S"]

# signal paths
dir_sig = "../data/signal_sync"
path_sin = "%s/sin_2021-06-21T15-16-00.h5" % dir_sig
path_rand = "%s/rand_2021-06-21T15-16-00.txt" % dir_sig

# define plot style
plot_style_dot = {
    'pen': None,
    'symbol': '+',
    'symbolPen': 'r',
    'symbolSize': 10
}

# signal configuration
signal_dict = {}

signal_dict["Sin"] = [
    [path_sin, '_', 1, "%Y-%m-%dT%H-%M-%S", "sin", "sin/freq", None],
    [path_sin, '_', 1, "%Y-%m-%dT%H-%M-%S", "dots", 0, plot_style_dot]
]

# create ViSiAnnoT window
win_visiannot = ViSiAnnoT(video_dict, signal_dict)
