
Your job is to design a webpage that demonstrates a creative image hover effect. The webpage consists of three images that change their clipping path when hovered over. Below are the detailed instructions to re-implement the webpage.

### Initial Webpage
The initial webpage should be as shown below:
![initial webpage](./_images/origin.png)

### HTML Structure
- The webpage should have a `section` element with the class `container`.
- Inside the `container`, there should be three `div` elements with the classes `clip clip1`, `clip clip2`, and `clip clip3`.

### CSS Styling
- Each `clip` element should be absolutely positioned to cover the entire container and have a transition effect of `0.5s`.
- The `clip1`, `clip2`, and `clip3` elements should have different background images (`img1.png`, `img2.png`, `img3.png` respectively) and different initial clipping paths.

### Hover Effects
- When the container is hovered over, all `clip` elements should change their clipping path to `polygon(100% 0, 100% 0, 100% 100%, 100% 100%)`.
- When an individual `clip` element is hovered over, it should change its clipping path to `polygon(0 0, 100% 0, 100% 100%, 0% 100%)`.

### Resources
- `img1.png` is used as the background image for the element with class `clip1`.
- `img2.png` is used as the background image for the element with class `clip2`.
- `img3.png` is used as the background image for the element with class `clip3`.

### Interaction Screenshots
The provided screenshots are rendered under a resolution of (1920, 1080).

5. **After Hovering Over Clip2**: ![after hovering over clip2](./_images/after_hover_clip2.png)

### Element Specifications
- Use class name `container` for the main container element.
- Use class name `clip` for all clip elements.
- Use class name `clip1` for the first clip element.
- Use class name `clip2` for the second clip element.
- Use class name `clip3` for the third clip element.

### Animations
- The transition effect for the clipping path changes should be `0.5s`.
