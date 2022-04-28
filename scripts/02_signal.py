# -*- coding: utf-8 -*-

from visiannot.visiannot import ViSiAnnoT

# signal paths
dir_sig = "../data/data_single"
path_sin = "%s/sin_2021-06-21T15-16-00.h5" % dir_sig
path_rand = "%s/rand_2021-06-21T15-16-00.txt" % dir_sig

# define plot style
plot_style_dot = {
    'pen': None,
    'symbol': '+',
    'symbolPen': 'r',
    'symbolSize': 10
}

plot_style_quality = {
    'pen': None,
    'symbol': 'x',
    'symbolPen': 'g',
    'symbolSize': 10
}

plot_style_rand = {'pen': {'color': 'm', 'width': 1}}

# signal configuration
signal_dict = {}

signal_dict["Sin"] = [
    [path_sin, '_', 1, "%Y-%m-%dT%H-%M-%S", "sin", "sin/freq", None],
    [path_sin, '_', 1, "%Y-%m-%dT%H-%M-%S", "dots - value", 0, plot_style_dot],
    [path_sin, '_', 1, "%Y-%m-%dT%H-%M-%S", "dots - quality", 0, plot_style_quality]
]

signal_dict["Rand"] = [
    [path_rand, '_', 1, "%Y-%m-%dT%H-%M-%S", '', 2, plot_style_rand]
]

# create ViSiAnnoT window
win_visiannot = ViSiAnnoT(
    {}, signal_dict, flag_pause_status=True, layout_mode=2
)
