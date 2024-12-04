
Your job is to design a webpage that allows users to drag and drop an image into different empty containers. The initial webpage should look like this:

![initial webpage](./_images/origin.png)

The provided screenshots are rendered under a resolution of 1920x1080.

### HTML Structure
- The webpage should have a `div` with class `empty` containing another `div` with class `fill` that is draggable.
- There should be four additional `div` elements with class `empty`.

### JavaScript Functionality
- Implement drag and drop functionality using JavaScript:
  - Use class name `fill` for the draggable element.
  - Use class name `empty` for the drop targets.
  - Add event listeners for `dragstart`, `dragend`, `dragover`, `dragenter`, `dragleave`, and `drop` events.
  - Functions to implement:
    - `dragStart()`: Sets the class name to `invisible` after a timeout.
    - `dragEnd()`: Resets the class name to `fill`.
    - `dragOver(e)`: Prevents the default behavior.
    - `dragEnter(e)`: Adds the `hovered` class.
    - `dragLeave()`: Resets the class name to `empty`.
    - `dragDrop()`: Appends the draggable element to the drop target and resets the class name to `empty`.

### Interaction
- Drag the image to the last empty container. After performing the drag and drop, the webpage should look like this:

![after drag and drop](./_images/after_drag_and_drop.png)

### Resources
- Image `natali-hordiiuk-DTYJck7Amm8-unsplash.jpg` is used for the background of the draggable element.
