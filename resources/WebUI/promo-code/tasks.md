
Your task is to design a webpage that features an interactive Christmas present box. The webpage should have a festive theme and include animations and effects when the user interacts with the present box. Below are the detailed instructions to help you re-implement the webpage.

### Initial Webpage
The initial webpage should look like this:

![initial webpage](./_images/origin.png)

### Requirements

1. **HTML Structure**:
    - The webpage should have a `div` with the class `present` and ID `present`.
    - Inside the `present` div, there should be three main child elements:
        - A `div` with the class `lid`.
        - A `div` with the class `promo` containing a `p` tag with the text "20% off promo" and an `h2` tag with the text "ILOVEYOU".
        - A `div` with the class `box`.

2. **CSS Styling**:
    - Use the Google Font "Itim" for the entire webpage.
    - The background should be a linear gradient.
    - The `box` and `lid` should have a radial gradient background with specific colors and positions.
    - The `lid` should have a transition effect for `top`, `left`, and `transform` properties.
    - When the `present` div is hovered over, the `lid` should move up and rotate slightly, and the `promo` div should move up as well.
    
3. **JavaScript Interactions**:
    - Include the `canvas-confetti` library from the CDN: `https://cdn.jsdelivr.net/npm/canvas-confetti@1.4.0/dist/confetti.browser.min.js`.
    - Add an event listener to the `present` div for `mouseenter` and `touchstart` events to trigger the confetti effect with specific colors.

4. **Animations and Effects**:
    - When the user hovers over the `present` div, the lid should move up and rotate, revealing the promo code.
    - Confetti should be triggered when the user hovers over or touches the `present` div.

### Interaction Screenshots
The provided screenshots are rendered under a resolution of 1920x1080.

- **After Hover**:
    ![after hover](./_images/after_hover.png)

### Element Details
- Use ID `present` for the main present box.
- Use class name `lid` for the lid of the present.
- Use class name `promo` for the promo code section.
- Use class name `box` for the main box of the present.

### Resources
- **Fonts**: Use the Google Font "Itim" from `https://fonts.googleapis.com/css2?family=Itim&display=swap`.
- **Confetti Library**: Include the `canvas-confetti` library from `https://cdn.jsdelivr.net/npm/canvas-confetti@1.4.0/dist/confetti.browser.min.js`.
- **Text Content**:
    - Promo text: "20% off promo"
    - Promo code: "ILOVEYOU"

By following these instructions, you should be able to recreate the interactive Christmas present webpage with the specified animations and effects.
