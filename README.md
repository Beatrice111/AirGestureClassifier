# AirGestureClassifier

We use mobile phone's gyroscope and accelerator data to classify letters written in the air. The repo contains the collected data and DTW algorithm in Python.

## Data

We ask 10 MIT students to write 10 capital letters in the air using the same iPhone 5. Each letter is written 10 times. Specifically, the 10 letters are O, I, J, L, Z, S, V, T, X and B. We give people the following instructions to write the letter:
* Vertically hold and face towards the phone.
* Touch the screen to start, and keep it touched until the end.
* Try to keep the phone vertically straight.
* Try to write the letter on the same plane as the phone’s plane.
* For B, go down and up and then the bumps.
* For I, up -> down end.
* For X, Start at the left top corner.

We collect gyroscope and accelerator sensor data during the time of letter writing. The data is stored in [data](data). We name the 10 people user1, user2, ..., user10 in order to remove personally-identifiable information. UserX's experimental data is stored in a separate Python file userX.py. The format is as the following:
```
data_userX = [
  # Each tuple represents the data during one letter writing. The first element is the letter, and the second 
  # element is a list of sensor log entries. Each entry logs [time, pitch, yaw, roll, wx, wy, wz, ax, ay, az],
  # and their associated units are [s, rad, rad, rad, rads/s, rads/s, rads/s, m/s^2, m/s^2, m/s^2].
  ('O', [[+4495.90608, +0.76544, -1.69096, +0.14862, -0.03917, +0.23694, +0.09660, -0.04301, -0.04088, +0.07551],
       [+4495.91671, +0.76544, -1.69002, +0.15012, +0.00045, +0.19030, +0.05346, -0.03152, -0.03151, +0.05360],
       [+4495.92735, +0.77154, -1.69076, +0.15318, +0.04369, +0.13865, +0.04573, +0.00557, -0.02698, +0.06540],
       ...,
       [+4502.25635, +0.79992, -1.72391, -0.09232, +0.24806, +0.18993, -0.13500, +0.03376, -0.00922, -0.09191]]),
  ('O', ...),
  ...,
  ('B', ...)
]
```
