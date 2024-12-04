
# Task Description: Light On and Off Webpage

Your job is to design a webpage that simulates a light bulb turning on and off when a switch is clicked. The initial webpage should look like this:

![initial webpage](./_images/origin.png)

## Requirements

1. **HTML Structure**:
    - The webpage should have a `div` with class `light` that contains the following elements:
        - A `div` with class `wire`.
        - A `div` with class `bulb` containing two `span` elements.
        - A `div` with class `switch` containing a `div` with class `btn`.
    - An `audio` element with the source `https://www.fesliyanstudios.com/play-mp3/387`, id `audio`, and `autostart` set to `false`.

2. **CSS Styling**:
    - The `wire` should be positioned absolutely, centered horizontally, and extend from the bottom to 60% of the viewport height.
    - When the body has the class `on`, the `bulb` should change to a bright white color with multiple layers of box-shadow to simulate light.
    - The `switch` should be positioned at the bottom right corner with a gradient background and a button (`btn`) inside it.
    - When the body has the class `on`, the button inside the switch should move slightly to indicate it has been pressed.

3. **JavaScript Functionality**:
    - When the button with class `btn` is clicked, the body should toggle the class `on`.
    - The audio should play when the button is clicked.

4. **Audio**:
    - The audio file from `https://www.fesliyanstudios.com/play-mp3/387` should play when the switch is clicked.

5. **Interactivity**:
    - Use class name `btn` for the switch button.
    - Use class name `on` for the body when the light is turned on.

## Screenshots

- After clicking the switch, the webpage should look like this:
  ![after clicking the switch](./_images/after_click.png)

## Additional Notes

- The provided screenshots are rendered under a resolution of 1920x1080.
- Ensure that the light bulb and switch have smooth transitions and animations to enhance the user experience.
- The audio should play each time the switch is clicked, regardless of the current state of the light.

By following the above requirements, you should be able to re-implement the webpage successfully.
