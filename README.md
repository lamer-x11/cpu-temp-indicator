# CPU Temperature Indicator

A simple status icon indicating the cpu's temperature level by changing its color.

When working with headphones on it's difficult to hear the laptop's fan going crazy while the cpu turns into lava. This helps to manage the problem by giving the user visual cues that something is wrong.

## Installation

The indicator uses `lm-sensors` to retrieve the temperature info so make sure you have the package available on your system.

Clone the repository and run
```bash
$ python setup.py install
```

## Usage

Launch the icon from the terminal.

```bash
$ cpu-temp-indicator
```

## Todo's

 * unit tests
 * custom temp thresholds
 * format switching (Celsius/Fahrenheit)
 
## Contributing

This project is published under the MIT license. Fork it and go crazy.
