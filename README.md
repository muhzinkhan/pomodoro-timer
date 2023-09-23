# Pomodoro Timer Application

<p align="center">
  <img src="assets/pomodoro.png" alt="Pomodoro Timer Logo">
</p>

## Overview

The Pomodoro Timer is a simple Windows application built using Python and the tkinter GUI library. It helps users manage their time effectively using the Pomodoro Technique, a time management method developed by Francesco Cirillo in the late 1980s.

## Features

- Set custom work and break durations.
- Start, pause, and reset the timer.
- Get visual and audio notifications at the end of each session.
- Track completed Pomodoro cycles.

## Requirements

- Python 3.x
- tkinter (included in standard library)
- Only Works on Windows machines. If you want, you can make supports for different platforms by forking it.😉

## Installation

1. Download the executable file form the releases .
2. Just run it. That's all there's to it.

## Usage

1. Launch the application by running `pomodoro_timer.py`.
2. Set the desired work and break durations using the input fields.
3. Click the "Start" button to begin a Pomodoro session.
4. During a session, the timer will count down the work duration.
5. When the work duration ends, an audio and visual notification will alert you.
6. Take a break, move on to the next session.
7. After completing a set number of sessions, the application will track the number of completed Pomodoro cycles as checkmarks.

## Screenshots

![Main Screen](assets/Screenshot.png)

## Configuration

You can customize the following parameters in `pomodoro_timer.py` and make a package out of it:

- `WORK_MIN`: Default work duration in minutes.
- `SHORT_BREAK_MIN`: Default break duration in minutes.
- `LONG_BREAK_MIN`: Duration of a long break in minutes (after 4 number of pomodoros).

## Acknowledgments

- [Francesco Cirillo](http://francescocirillo.com/) for inventing the Pomodoro Technique.

## Roadmap

- [ ] Add the ability to save and load custom presets.
- [ ] Implement a task list feature.
- [ ] Add a pause button and skip button feature.

## Contributing

If you'd like to contribute, please fork the repository and create a pull request. Please make sure to update tests as appropriate.

## Support

If you encounter any issues or have suggestions, please [open an issue](https://github.com/muhzinkhan/pomodoro-timer/issues).


