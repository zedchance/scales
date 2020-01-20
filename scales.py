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
    """ A tool to generate stringed instruments visual aids """

    def __init__(self, scale: list, strings=None, title=None):
        """
        Constructs a Scales object
        :param scale: the notes to draw, as a list of strings
        :param strings: the tuning of the instrument, defaults to standard 6 string guitar
        :param title: title of the image
        """
        if strings is None:  # Standard tuning
            self.strings = ['E', 'A', 'D', 'G', 'B', 'E']
        else:
            self.strings = strings
        self.scale = scale
        self.title = title

    def _draw_fretboard(self, x: float, y: float):
        """ Draws a scale on a full fretboard """
        fig, ax = plt.subplots(figsize=(x, y))
        plt.subplots_adjust(left=0.04, right=.98, top=.85, bottom=.1)
        ax.set_axis_off()
        # ax.margins(y=0.1)
        ax.set_title(self.title)
        marker_style = dict(color='tab:blue', linestyle=':', marker='o', markersize=15, markerfacecoloralt='tab:red')
        # Draw fretboard
        markers = [3, 5, 7, 9, 12, 15, 17]
        total_frets = 24
        for n, string in enumerate(self.strings):
            ax.text(-0.4, n, string, horizontalalignment='center', verticalalignment='center')
            ax.plot(n * np.ones(total_frets), linestyle='solid', color='black')
            for fret in range(1, total_frets):
                ax.plot(fret, n, fillstyle='none', **marker_style)
                number_color = 'black'
                if fret in markers:
                    plt.axvline(fret, color='black')
                    number_color = 'red'
                ax.text(fret, -0.75, fret, color=number_color, horizontalalignment='center', verticalalignment='center')
        # Draw notes
        for i in range(len(self.strings)):
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
        """
        Draws the fretboard and notes of the scale
        Roots are marked with red
        :param start: fret to start drawing at, defaults to 0
        :param stop: fret to stop drawing at, defaults to 15
        """
        distance = abs(start - stop)
        self._draw_fretboard(distance * .5 + 1, len(self.strings) / 2.5)
        plt.axis([start - 0.5, stop + 0.5, -.5, len(self.strings) - 0.5])
        plt.show()
        plt.close()


if __name__ == '__main__':
    a_mixo = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G']
    six_string = Scales(title='A Mixolydian', scale=a_mixo)
    six_string.draw(start=11, stop=15)

    c_major = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    ukelele = Scales(title='C Major on Ukelele', strings=['G', 'C', 'E', 'A'], scale=c_major)
    ukelele.draw()

    g_chord = ['G', 'B', 'D']
    Scales(title='Open G', scale=g_chord).draw(stop=3)
