from plot_signals import PlotSignals
from collections import OrderedDict

od = OrderedDict([('CLK_25MHZ',
                   [(0, '1'), (20, '0'), (40, '1'), (60, '0'), (80, '1'), (100, '0'), (120, '1'), (140, '0'),
                    (160, '1'),
                    (180, '0'), (200, '1'), (220, '0'), (240, '1'), (260, '0'), (280, '1'), (300, '0'), (320, '1'),
                    (340, '0'), (360, '1'), (380, '0'), (400, '1'), (420, '0'), (440, '1'), (460, '0'), (480, '1'),
                    (500, '1')]), ('CLK_160MHZ',
                                   [(0, '0'), (20, '0'), (40, '0'), (60, '1'), (80, '1'), (100, '0'), (120, '0'),
                                    (140, '1'),
                                    (160, '1'), (180, '0'), (200, '0'), (220, '0'), (240, '1'), (260, '1'), (280, '0'),
                                    (300, '0'), (320, '1'), (340, '1'), (360, '0'), (380, '0'), (400, '1'), (420, '1'),
                                    (440, '1'), (460, '0'), (480, '0'), (500, '1')])])

if __name__ == '__main__':
    pso = PlotSignals(od)
    pso.plot_signals()
