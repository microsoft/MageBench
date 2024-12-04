
# Task Description: Background Slider Webpage

Your job is to design a webpage that features a background slider with navigation arrows. The webpage should allow users to navigate through different background images by clicking on the left and right arrows. Below are the detailed instructions and resources needed to re-implement the webpage.

## Initial Webpage

The initial webpage should look like this:

![initial webpage](./_images/origin.png)

This screenshot is rendered under a resolution of 1920x1080.

## Resources

1. **Images**:
   - `resource1.png`: Used as the background image for the first slide.
   - `resource2.png`: Used as the background image for the second slide.
   - `resource3.png`: Used as the background image for the third slide.
   - `resource4.png`: Used as the background image for the fourth slide.

2. **Fonts and Icons**:
   - Font: 'Roboto' from Google Fonts.
   - Icons: Font Awesome for the arrow icons.

## HTML Structure

- The webpage should have a `div` with the class `slider-container` that contains all the slides and navigation buttons.
- Each slide should be a `div` with the class `slide`. The first slide should also have the class `active`.
- There should be two buttons for navigation:
  - A left arrow button with the class `arrow left-arrow` and the ID `left`.
  - A right arrow button with the class `arrow right-arrow` and the ID `right`.

## CSS Styling

- Use the `Roboto` font from Google Fonts.
- The body should have a background image that changes based on the active slide.
- The `slider-container` should have a shadow and be positioned in the center of the viewport.
- Each `slide` should have a background image, be positioned absolutely, and have a transition effect.
- The `arrow` buttons should be styled with a transparent background, white color, and an orange border.

## JavaScript Functionality

- Use JavaScript to handle the click events for the left and right arrow buttons.
- When the right arrow is clicked, the next slide should become active. If the current slide is the last one, the first slide should become active.
- When the left arrow is clicked, the previous slide should become active. If the current slide is the first one, the last slide should become active.
- The background image of the body should change to match the active slide.

## Interaction Screenshots

1. **After First Right Click**:
   
   ![after first right click](./_images/after_first_right_click.png)

2. **After Second Right Click**:
   
   ![after second right click](./_images/after_second_right_click.png)

3. **After Left Click**:
   
   ![after left click](./_images/after_left_click.png)

These screenshots are rendered under a resolution of 1920x1080.

## Element IDs and Class Names

- Use class name `slider-container` for the container of the slides and navigation buttons.
- Use class name `slide` for each slide.
- Use class name `active` for the currently active slide.
- Use class name `arrow` for the navigation buttons.
- Use class name `left-arrow` for the left navigation button.
- Use class name `right-arrow` for the right navigation button.
- Use ID `left` for the left navigation button.
- Use ID `right` for the right navigation button.

## Animations

- The slides should have a fade-in effect when they become active.
- The background image of the body should transition smoothly when changing.
