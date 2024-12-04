
Your job is to design a webpage that features an image carousel. The carousel allows users to navigate through a series of images using "Prev" and "Next" buttons. Below are the detailed instructions to re-implement the webpage.

### Initial Webpage
The initial webpage should look like this:
![initial webpage](./_images/origin.png)

### Resources
- **Images**: 
  - `resource1.png` is used for the first image.
  - `resource2.png` is used for the second image.
  - `resource3.png` is used for the third image.
  - `resource4.png` is used for the fourth image.
- **Fonts**: 
  - The webpage uses the 'Roboto' font from Google Fonts. You can import it using the following URL:
    ```css
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
    ```

### Layout and Styling
- The webpage should be centered both vertically and horizontally.
- The buttons should be styled with a background color of `rebeccapurple`, white text, and should occupy equal width within their container.

### HTML Structure
- Use a `div` with class `carousel` to wrap the entire carousel.
- Use a `div` with class `image-container` and ID `imgs` to wrap the images.
- Use `img` tags to include each image within the `image-container`.
- Use a `div` with class `buttons-container` to wrap the buttons.
- Use `button` tags with IDs `left` and `right` for the "Prev" and "Next" buttons respectively.

### CSS Styling
- Use the class name `carousel` for the main carousel container.
- Use the class name `image-container` for the container that holds the images.
- Use the class name `buttons-container` for the container that holds the buttons.
- Use the class name `btn` for the buttons.

### JavaScript Functionality
- Use the ID `imgs` to select the image container.
- Use the IDs `left` and `right` to select the "Prev" and "Next" buttons.
- Implement the functionality to navigate through the images by changing the `translateX` property of the `image-container`.

### Interactions
- Clicking the "Next" button should show the next image in the carousel.
  - ![after clicking next](./_images/after_next.png)
- Clicking the "Prev" button should show the previous image in the carousel.
  - ![after clicking prev](./_images/after_prev.png)

### Additional Notes
- The provided screenshots are rendered under a resolution of 1920x1080.
- The transition between images should be smooth, with a duration of 0.5 seconds.
- Ensure that the buttons are interactive and change opacity when hovered over.

