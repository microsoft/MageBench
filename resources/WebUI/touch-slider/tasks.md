
# Task Description: Implement a Touch Slider Webpage

Your job is to design a webpage that features a touch slider with multiple slides. The initial webpage should look like this:

![initial webpage](./_images/origin.png)

The webpage consists of three slides, each showcasing a different Apple product. Users can navigate through the slides by dragging them left or right. Each slide contains a product image, name, price, and a "Buy Now" button.

## Requirements

### HTML Structure
- The webpage should have a `div` with class `slider-container` that contains multiple `div` elements with class `slide`.
- Each `slide` should contain:
  - An `h2` element for the product name.
  - An `h4` element for the product price.
  - An `img` element for the product image.
  - An `a` element with class `btn` for the "Buy Now" button.

### CSS Styling
- Use the Google Font "Open Sans" for the entire webpage.

### JavaScript Functionality
- Implement touch and mouse events to enable dragging of slides.
- When a slide is dragged more than 100 pixels, it should transition to the next or previous slide.
- The `slider-container` should have a smooth transition effect when sliding.
- When dragging, the cursor should change to `grabbing`, and the image should scale down slightly.

### Resources
- Use the following images for the products:
  - `resource1.png` for the AirPods.
  - `resource2.png` for the iPhone 12.
  - `resource3.png` for the iPad.

### Interactions
- The initial webpage should look like the provided screenshot.
- When the user slides to the next item, the webpage should look like this:

![after sliding to next](./_images/after_slide_next.png)

- When the user slides back to the previous item, the webpage should look like this:

![after sliding to previous](./_images/after_slide_previous.png)

### Additional Notes
- The provided screenshots are rendered under a resolution of 1920x1080.
- Ensure that the `slider-container` has the class `grabbing` when dragging, and remove it when the dragging ends.
- Use the following IDs and class names for elements:
  - Use class name `slider-container` for the main slider container.
  - Use class name `slide` for each individual slide.
  - Use class name `btn` for the "Buy Now" button.

By following these instructions, you should be able to re-implement the touch slider webpage as described.
