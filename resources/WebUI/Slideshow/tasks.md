
Your job is to design a webpage that features a slideshow with controls for navigating through the slides and a play/pause button. The initial webpage should look like this:

![initial webpage](./_images/origin.png)

### Requirements:

1. **HTML Structure**:
    - The webpage should have a `div` with class `container` that wraps the entire slideshow.
    - Inside the `container`, there should be a `div` with class `slideshow-wrapper`.
    - The `slideshow-wrapper` should contain:
        - Two `div` elements with class `control` and additional classes `left-arrow` and `right-arrow` respectively for navigation arrows.
        - A `div` with class `slides` that contains multiple `div` elements with class `slide` and additional classes like `slide-1`, `slide-2`, etc., each containing an `img` element.
        - A `div` with class `play-pause` containing an `i` element with class `fas fa-play`.

2. **CSS Styling**:
    - The slideshow should cover the entire viewport.
    - Each slide should be absolutely positioned, covering the entire viewport, and should transition opacity over 1 second.
    - The navigation arrows should be semi-transparent and positioned on the left and right edges of the viewport.
    - The play/pause button should be centered horizontally at the bottom of the viewport.
    - Use the following images for the slides:
        - `images/slide-img-1.jpg`
        - `images/slide-img-2.jpg`
        - `images/slide-img-3.jpg`

3. **JavaScript Functionality**:
    - Implement a function to change slides automatically every 3 seconds when the slideshow is playing.
    - Clicking the play/pause button should toggle between playing and pausing the slideshow.
    - Clicking the left or right arrows should navigate to the previous or next slide respectively.
    - When the slideshow is paused, the navigation arrows should become semi-transparent.

### Interaction Steps:

1. **Initial State**:
    - The slideshow should start playing automatically.
    - The play/pause button should display a pause icon (`fa-pause`).

2. **Pause the Slideshow**:
    - Click the play/pause button to pause the slideshow.
    - The play/pause button should change to a play icon (`fa-play`).
    - The navigation arrows should become semi-transparent.
    - The webpage should look like this after pausing:

    ![after pause](./_images/after_pause.png)

3. **Navigate Left**:
    - Click the left arrow to navigate to the previous slide.
    - The webpage should look like this after clicking the left arrow:

    ![after left arrow](./_images/after_left_arrow.png)

4. **Navigate Right**:
    - Click the right arrow to navigate to the next slide.
    - The webpage should look like this after clicking the right arrow:

    ![after right arrow](./_images/after_right_arrow.png)

### Additional Details:
- The provided screenshots are rendered under a resolution of 1920x1080.
- Use the Font Awesome library for the play/pause icons. Include the following link in the HTML `<head>` section:
    ```html
    <link
      rel="stylesheet"
      href="https://use.fontawesome.com/releases/v5.3.1/css/all.css"
      integrity="sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU"
      crossorigin="anonymous"
    />
    ```
- Use the following class names and IDs for elements:
    - Use class `container` for the main container.
    - Use class `slideshow-wrapper` for the slideshow wrapper.
    - Use class `control` for the navigation controls.
    - Use class `left-arrow` for the left navigation arrow.
    - Use class `right-arrow` for the right navigation arrow.
    - Use class `slides` for the slides container.
    - Use class `slide` for each slide.
    - Use class `play-pause` for the play/pause button.
    - Use class `fas fa-play` and `fas fa-pause` for the play and pause icons respectively.

Follow these instructions to re-implement the webpage as described.
