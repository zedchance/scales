import matplotlib.pyplot as plt
import numpy as np


def _get_fret_number(string, note):
    """ Returns the fret number of a given note on a given string """
    pitches = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    start = pitches.index(string)
    stop = pitches.index(note)
    fret = 12 - (start - stop)
    # print(string, note, fret % 12)
    return fret % 12


class Scales:
    """ Python library to draw guitar scales """

    def __init__(self, scale: list, strings=None, title=None):
        if strings is None:  # Standard tuning
            self.strings = ['E', 'A', 'D', 'G', 'B', 'E']
        self.scale = scale
        self.title = title

    def _draw_fretboard(self):
        """ Draws a scale on a full fretboard """
        fig, ax = plt.subplots(figsize=(7, 2.25))
        plt.subplots_adjust(left=0.04, right=.98)
        ax.set_axis_off()
        ax.margins(y=0.1)
        ax.set_title(self.title)
        marker_style = dict(color='tab:blue', linestyle=':', marker='o', markersize=15, markerfacecoloralt='tab:red')
        # Draw fretboard
        markers = [3, 5, 7, 9, 12, 15, 17]
        total_frets = 24
        for n, string in enumerate(self.strings):
            ax.text(-0.6, n, string, horizontalalignment='center', verticalalignment='center')
            ax.plot(n * np.ones(total_frets), linestyle='solid', color='black')
            for fret in range(1, total_frets):
                ax.plot(fret, n, fillstyle='none', **marker_style)
                number_color = 'black'
                if fret in markers:
                    plt.axvline(fret, color='black')
                    number_color = 'red'
                ax.text(fret, -0.75, fret, color=number_color, horizontalalignment='center', verticalalignment='center')
        # Draw notes
        for i in range(6):
            for j in range(len(self.scale)):
                # Determine fill style, unique on root
                fillstyle = 'full'
                if self.scale[j] == self.scale[0]:
                    fillstyle = 'top'
                # Plot notes
                fret = _get_fret_number(self.strings[i], self.scale[j])
                ax.plot(fret, i, fillstyle=fillstyle, **marker_style)
                ax.plot(fret + 12, i, fillstyle=fillstyle, **marker_style)

    def draw(self, start=0, stop=15):
        """ Draws a scale on a fretboard """
        distance = abs(start - stop)
        print(distance)
        self._draw_fretboard()
        plt.axis([start - 0.5, stop + 0.5, -0.5, 5.5])
        plt.show()


if __name__ == '__main__':
    a_mixo = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G']
    s = Scales(title='A Mixolydian', scale=a_mixo)
    s.draw(start=11, stop=15)

    c_major = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    s2 = Scales(title='C Major', scale=c_major)
    s2.draw()

    g_chord = ['G', 'B', 'D']
    s3 = Scales(title='Open G', scale=g_chord)
    s3.draw(stop=3)
