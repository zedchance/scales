import matplotlib.pyplot as plt
import numpy as np


def _get_fret_number(string, note):
    """ Returns the fret number of a given note on a given string """
    pitches = [('A', 0), ('Bbb', 0), ('G##', 0),
               ('A#', 1), ('Bb', 1), ('Cbb', 1),
               ('B', 2), ('Cb', 2), ('A##', 2),
               ('B#', 3), ('C', 3), ('Dbb', 3),
               ('C#', 4), ('Db', 4), ('B##', 4),
               ('D', 5), ('C##', 5), ('Ebb', 5),
               ('D#', 6), ('Eb', 6), ('Fbb', 6),
               ('E', 7), ('Fb', 7), ('D##', 7),
               ('E#', 8), ('F', 8), ('Gbb', 8),
               ('F#', 9), ('Gb', 9), ('E##', 9),
               ('G', 10), ('F##', 10), ('Abb', 10),
               ('G#', 11), ('Ab', 11)]
    for (pitch, index) in pitches:
        if string.lower() == pitch.lower():
            start = index
        if note.lower() == pitch.lower():
            stop = index
    fret = 12 - (start - stop)
    return fret % 12


class Scales:
    """ A tool to generate stringed instrument visual aids """

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

    def _draw_fretboard(self, x: float, y: float, start: int):
        """
        Draws a scale on a full fretboard in preparation for the draw function
        :param x: width of figure
        :param y: height of figure
        """
        fig, ax = plt.subplots(figsize=(x, y))
        plt.subplots_adjust(left=0.04, right=.98, top=.85, bottom=.1)
        ax.set_axis_off()
        ax.set_title(self.title)
        marker_style = dict(color='tab:blue', linestyle=':', marker='o', markersize=15, markerfacecoloralt='tab:red')
        # Draw fretboard
        markers = [3, 5, 7, 9, 12, 15, 17]
        total_frets = 24
        for n, string in enumerate(self.strings):
            # Draw string labels and string lines
            ax.text(-0.4 + start, n, string.capitalize(), horizontalalignment='center', verticalalignment='center')
            ax.plot(n * np.ones(total_frets), linestyle='solid', color='black')
            plt.axvline(-0.4 + start, color='white', linewidth=11)
            # Fill fretboard with empty markers and label fret numbers
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
        # Get range of frets to zoom into
        distance = abs(start - stop)
        # Size of figure
        x = distance * .5 + 1
        y = len(self.strings) / 2.7
        self._draw_fretboard(x, y, start)
        # Zoom
        pad = 0.5
        left = start - pad
        right = stop + pad
        bottom = 0 - pad
        top = len(self.strings) - pad
        plt.axis([left, right, bottom, top])
        plt.show()
        plt.close()


# Test code
if __name__ == '__main__':
    a_mixo = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G']
    six_string = Scales(title='A Mixolydian', scale=a_mixo)
    six_string.draw(start=11, stop=15)
    six_string.draw(start=4, stop=8)

    e_mixo = ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D']
    Scales(title='E Mixolydian on 4 string bass', strings=['E', 'A', 'D', 'G'], scale=e_mixo).draw()

    gb_dorian = ['gb', 'Ab', 'Bbb', 'Cb', 'db', 'Eb', 'FB']
    flats = Scales(title='Gb Dorian', scale=gb_dorian)
    # flats.draw(stop=5)

    c_major = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    ukulele = Scales(title='C Major on Ukulele', strings=['G', 'C', 'E', 'A'], scale=c_major)
    ukulele.draw()

    g_chord = ['G', 'B', 'D']
    # Scales(title='Open G', scale=g_chord).draw(stop=3)

    e_minor = ['E', 'F#', 'G', 'A', 'B', 'C', 'D']
    bass = Scales(title='E Minor on 4-string bass', strings=['E', 'A', 'D', 'G'], scale=e_minor)
    # bass.draw()

    # A blank sheet to print and write in your own scales
    # Scales([]).draw()

    # Chord sheet
    # Scales([]).draw(stop=3)
