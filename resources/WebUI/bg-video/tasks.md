
Your job is to design a webpage that features a full-screen background video with a title and a button overlay. The initial webpage should be as shown below:

![initial webpage](./_images/origin.png)

### Requirements:

1. **HTML Structure**:
    - Create a `<section>` element with the class `hero` to serve as the container for the video and content.
    - Inside the `hero` section, add a `<video>` element with the class `back-video` that will autoplay, loop, and be muted. The video source should be `assets/video.mp4`.
    - Add another `<section>` inside the `hero` section with the class `content` to hold the title and button.
    - Inside the `content` section, add an `<h1>` element with the text "Journey".
    - Below the `<h1>`, add an `<a>` element with the text "Explore".

2. **CSS Styling**:
    - Apply a global reset for padding, margin, and box-sizing. Use a sans-serif font for the entire page.
    - Style the `hero` section to take up the full viewport height and width, with a linear gradient overlay.
    - Center the content both horizontally and vertically within the `hero` section.
    - Style the `content` section to center-align its text.
    - Style the `<h1>` element to have a font size of 160px, white color, and a font weight of 600. Add a hover effect that changes the text color to transparent with a white stroke.
    - Style the `<a>` element to be a white-bordered button with white text. Add a hover effect that changes the background to white and the text color to black.
    - Ensure the `back-video` element is positioned absolutely to cover the entire background, adjusting its size based on the aspect ratio.

3. **Interactions**:
    - When hovering over the `<h1>` element, the text should change to have a white stroke and transparent fill. This is shown in the screenshot below:
    
    ![after hovering over title](./_images/after_hover_title.png)
    
    - When hovering over the `<a>` element, the button should change to have a white background and black text. This is shown in the screenshot below:
    
    ![after hovering over button](./_images/after_hover_button.png)

### Additional Notes:
- The provided screenshots are rendered under a resolution of 1920x1080.
- Use the following class names and IDs for the elements:
    - Use class name `hero` for the main container section.
    - Use class name `back-video` for the video element.
    - Use class name `content` for the content section.
    - Use class name `content h1` for the title.
    - Use class name `content a` for the button.
- The video file `assets/video.mp4` should be used as the background video.
