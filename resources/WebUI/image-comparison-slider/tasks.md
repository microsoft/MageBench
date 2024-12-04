
# Task Description: Image Comparison Slider

Your job is to design a webpage that implements an image comparison slider. The slider allows users to compare two images by dragging a slider left and right. Below are the detailed instructions and resources needed to re-implement the webpage.

## Initial Webpage
The initial webpage should look like this:
![initial webpage](./_images/origin.png)

## Resources
- `resource1.png`: This image is used for the "after" state in the comparison.
- `resource2.png`: This image is used for the "before" state in the comparison.

## Layout and Styling
- The webpage should be centered both vertically and horizontally.
- The images should be contained within two divs: one for the "before" state and one for the "after" state.

## HTML Structure
- Use a `div` with class `container` to hold the entire image comparison component.
- Inside the container, use two `div`s with classes `img-container-before` and `img-container-after` to hold the "before" and "after" images respectively.
- Use an `img` tag inside each of these `div`s to display the images.
- Use a `div` with class `slider` to represent the draggable slider.

## CSS Styling
- Use class name `container` for the main container.
- Use class name `img-container-before` for the "before" image container.
- Use class name `img-container-after` for the "after" image container.
- Use class name `slider` for the draggable slider.

## JavaScript Functionality
- Implement a function to handle the dragging of the slider.
- Use event listeners to handle mouse and touch events for dragging the slider.

## Interactions
- When the user drags the slider to the left, the "before" image should be revealed more.
- When the user drags the slider to the right, the "after" image should be revealed more.

## Screenshots
- After dragging the slider to the left:
![after dragging to the left](./_images/after_drag_left.png)
- After dragging the slider to the right:
![after dragging to the right](./_images/after_drag_right.png)

## Notes
- The provided screenshots are rendered under a resolution of 1920x1080.
- Ensure that the slider is draggable and updates the width of the "before" image container and the position of the slider accordingly.
