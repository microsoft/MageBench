
# Task Description: Re-implement the Webpage with Hover Effect

Your job is to design a webpage that features an image with a hover effect that reveals a text overlay. The initial webpage should look like this:

![initial webpage](./_images/origin.png)

When the user hovers over the image, the text overlay should slide in from the left, and the image should slide out to the right. The webpage after hovering should look like this:

![after hover](./_images/after_hover.png)

The provided screenshots are rendered under a resolution of 1920x1080.

## Detailed Requirements

### HTML Structure

1. **Container Section**:
   - Use a `<section>` element with the class name `container`.

2. **Image**:
   - Use an `<img>` element inside the container to display the image `rayul-_M6gy9oHgII-unsplash.jpg`.

3. **Content Overlay**:
   - Use an `<article>` element with the class name `content` inside the container.
   - Inside the `<article>`, include:
     - An `<h1>` element with the text: "Welcome To The Real World 😉".
     - An `<h4>` element with the text: "Write Your Content Here 🥂".

### CSS Styling

1. **Body**:
   - Use flexbox to center the container both vertically and horizontally.
   - Use the `sans-serif` font family.

3. **Image**:
   - Set the width to 100%.
   - Apply a transition effect of 1 second for all properties.

3. **Content Overlay**:
   - Apply a transition effect of 1 second for all properties.

5. **Hover Effects**:
   - When the container is hovered:
     - Translate the content overlay to its original position (translateX(0)).
     - Translate the image to the right by 100%.

### Interactions

- The hover effect should be applied to the container with the class name `container`.

### Resources

- **Image**: `rayul-_M6gy9oHgII-unsplash.jpg` is used for the main image.
- **Text Content**:
  - `<h1>`: "Welcome To The Real World 😉"
  - `<h4>`: "Write Your Content Here 🥂"

### Additional Notes

- Ensure that the hover effect transitions smoothly over 1 second.
- The text overlay should be centered both vertically and horizontally within the container.

By following these instructions, you should be able to re-implement the webpage with the specified hover effect.
