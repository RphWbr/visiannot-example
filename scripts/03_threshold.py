# -*- coding: utf-8 -*-

from visiannot.visiannot import ViSiAnnoT

# signal path
dir_sig = "../data/data_single"
path_rand = "%s/rand_2021-06-21T15-16-00.txt" % dir_sig

# signal configuration
signal_dict = {}
signal_dict["rand"] = [[path_rand, '_', 1, "%Y-%m-%dT%H-%M-%S", '', 2, None]]

# threshold configuration
threshold_dict = {}
threshold_dict["rand"] = [
    [0.2, (51, 102, 0, 80)],
    [0.8, (178, 34, 34, 80)]
]

# create ViSiAnnoT window
win_visiannot = ViSiAnnoT(
    {}, signal_dict, flag_pause_status=True, layout_mode=2,
    threshold_dict=threshold_dict
)
