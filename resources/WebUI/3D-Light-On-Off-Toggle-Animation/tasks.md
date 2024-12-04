
Your job is to design a webpage that features a 3D light on/off toggle animation. The webpage should have a toggle switch that, when clicked, changes the state of a light from off to on and vice versa. Below are the details you need to re-implement the webpage.

The initial webpage should be ![initial webpage](./_images/origin.png)

### Requirements:

1. **HTML Structure**:
    - Create a `div` element with the class `toggle`.
    - Inside this `div`, add an `input` element of type `checkbox` with the ID `btn`.
    - Add a `label` element for the `btn` input.
    - Inside the `label`, add a `span` element with the class `thumb`.
    - Add another `div` element with the class `light`.

2. **CSS Styling**:
    - Use the following CSS variables:
        - `--sz`: Size of the toggle elements.
        - `--on`: Color when the light is on.
        - `--of`: Color when the light is off.
        - `--gr`: Gray color.
        - `--tr`: Transition property.
        - `--lg`: Light gradient color.
    - Apply the following styles:
        - `body`: Center the content, set background gradients, and apply a blur effect.
        - `toggle`: Position the toggle switch and center its content.
        - `input`: Hide the checkbox.
        - `label[for="btn"]`: Style the toggle switch background and apply shadows.
        - `thumb`: Style the toggle button, apply gradients, shadows, and set its position.
        - `light`: Style the light indicator, apply shadows, and set its position.
    - Use transitions to animate the toggle switch and light indicator when the checkbox is checked.

3. **Interactions**:
    - Clicking on the `span` element with the class `thumb` should toggle the state of the checkbox and animate the light indicator.
    - Use the ID `btn` for the checkbox input.
    - Use the class name `thumb` for the toggle button.
    - Use the class name `light` for the light indicator.

### Resources:
- The provided screenshots are rendered under a resolution of (1920, 1080).

### Screenshots:
- After clicking the toggle: ![after clicking](./_images/after_click.png)

### Description of Animations:
- When the `thumb` is clicked, the light indicator changes its color and shadow to simulate turning on or off.
- The `thumb` itself moves from one end of the toggle switch to the other, accompanied by a color change.

By following the above instructions, you should be able to re-implement the 3D light on/off toggle animation webpage.
