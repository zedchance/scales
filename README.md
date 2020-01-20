# scales

A tool to generate guitar scale visual aids written in Python

* [Usage](#usage)
* [Dependencies](#dependencies)

## Usage
Scales objects take at least the `scale` parameter, which should be a list of notes. They can be drawn using the `draw` function, where `start` and `stop` are the range of frets to show.

For example:

```py
a_mixo = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G']
six_string = Scales(title='A Mixolydian', scale=a_mixo)
six_string.draw(start=11, stop=15)
```

![a_mix](screenshots/a_mixo.png)

By default, it will assume a 6 string guitar in standard tuning, but you can specify other tunings like:

```py
c_major = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
ukelele = Scales(title='C Major', strings=['E', 'B', 'G', 'D'], scale=c_major)
ukelele.draw()
```

![c_maj_uke](screenshots/c_maj_uke.png)

Scales can be drawn without making it an object:

```py
g_chord = ['G', 'B', 'D']
Scales(title='Open G', scale=g_chord).draw(stop=3)
```

![open_g](screenshots/open_g.png)

## Dependencies

Library | Description
--- | ---
[matplotlib](https://matplotlib.org) | 2D plotting library
[numpy](https://numpy.org) |  Fundamental package for scientific computing