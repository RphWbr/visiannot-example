from visiannot.visiannot import ViSiAnnoT

# signal path
dir_data = "../data/data_single"
path_sin = "%s/sin_2021-06-21T15-16-00.h5" % dir_data

# signal configuration
signal_dict = {}
signal_dict["sin"] = [
    [path_sin, '_', 1, "%Y-%m-%dT%H-%M-%S", "sin", "sin/freq", None]
]

# interval paths
path_interval_a = "%s/intervalA_2021-06-21T15-16-00.txt" % dir_data
path_interval_b = "%s/intervalB_2021-06-21T15-16-00.txt" % dir_data

# interval configuration
interval_dict = {}
interval_dict["sin"] = [
    [path_interval_a, '_', 1, "%Y-%m-%dT%H-%M-%S", '', 30, (0, 255, 0, 50)],
    [path_interval_b, '_', 1, "%Y-%m-%dT%H-%M-%S", '', 30, (255, 200, 0, 50)]
]

# create ViSiAnnoT window
win_visiannot = ViSiAnnoT(
    {}, signal_dict, flag_pause_status=True, layout_mode=2,
    interval_dict=interval_dict
)
