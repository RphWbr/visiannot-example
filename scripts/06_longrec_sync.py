from visiannot.visiannot import ViSiAnnoTLongRec

# video directory
dir_vid = "../data/video"

# video configuration
video_dict = {}
video_dict["vid_0"] = [dir_vid, "vid_*.mp4", '_', 1, "%Y-%m-%dT%H-%M-%S"]

# signal directory
dir_sig = "../data/signal_sync"

# define plot style
plot_style_dot = {
    'pen': None,
    'symbol': '+',
    'symbolPen': 'r',
    'symbolSize': 10
}

plot_style_rand = {'pen': {'color': 'm', 'width': 1}}

# signal configuration
signal_dict = {}

signal_dict["Sin"] = [
    [dir_sig, "sin_*.h5", '_', 1, "%Y-%m-%dT%H-%M-%S", "sin", "sin/freq", None],
    [dir_sig, "sin_*.h5", '_', 1, "%Y-%m-%dT%H-%M-%S", "dots", 0, plot_style_dot]
]

signal_dict["Rand"] = [
    [dir_sig, "rand_*.txt", '_', 1, "%Y-%m-%dT%H-%M-%S", '', 2, plot_style_rand]
]

# interval directory
dir_inter = "../data/interval_sync"

# interval configuration
interval_dict = {}
interval_dict["Sin"] = [
    [dir_inter, "intervalA_*.txt", '_', 1, "%Y-%m-%dT%H-%M-%S", '', -1, (0, 255, 0, 50)],
    [dir_inter, "intervalB_*.txt", '_', 1, "%Y-%m-%dT%H-%M-%S", '', -1, (255, 200, 0, 50)]
]

# create ViSiAnnoT window
win_visiannot = ViSiAnnoTLongRec(
    video_dict, signal_dict, interval_dict=interval_dict,
    flag_pause_status=True
)
