import matplotlib.pyplot as plt


class Scales:
    """ Python library to draw guitar scales """

    def __init__(self, scale : list, strings=None, title=None):
        if strings is None:  # Standard tuning
            self.strings = ['E', 'A', 'D', 'G', 'B', 'E']
        self.scale = scale
        self.title = title

    def get_fret_number(self, string, note):
        """ Returns the fret number of a given note on a given string """
        pitches = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        start = pitches.index(string)
        stop = pitches.index(note)
        fret = 12 - (start - stop)
        # print(string, note, fret % 12)
        return fret % 12

    def draw(self):
        """ Draws a scale on a full fretboard, defaults to standard tuning """
        fig, ax = plt.subplots(figsize=(7, 3))
        ax.set_axis_off()
        ax.set_title(self.title)
        marker_style = dict(color='tab:blue', linestyle=':', marker='o', markersize=15, markerfacecoloralt='tab:red')
        # Draw fretboard
        for n, string in enumerate(self.strings):
            ax.text(-0.75, n, string, horizontalalignment='center', verticalalignment='center')
            for fret in range(1, 15):
                ax.text(fret, -0.75, fret, horizontalalignment='center', verticalalignment='center')
                ax.plot(fret, n, fillstyle='none', **marker_style)
        # Draw notes
        for i in range(6):
            for j in range(7):
                self.get_fret_number(self.strings[i], self.scale[j])
                fillstyle = 'full'
                if self.scale[j] == self.scale[0]:
                    fillstyle = 'top'
                ax.plot(self.get_fret_number(self.strings[i], self.scale[j]), i, fillstyle=fillstyle, **marker_style)
        plt.show()


# Test code
a_mixo = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G']
s = Scales(title='A Mixolydian', scale=a_mixo)
s.draw()

# s.get_fret_number('E', 'A')
# s.get_fret_number('A', 'C')
# s.get_fret_number('B', 'B')
# s.get_fret_number('D', 'D#')
# s.get_fret_number('D', 'C')
# s.get_fret_number('G', 'D')
# s.get_fret_number('G', 'G#')