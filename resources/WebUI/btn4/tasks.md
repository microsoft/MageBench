
Your task is to design a webpage with a button that has a hover effect. The webpage should look and behave as described below. The provided screenshots are rendered under a resolution of 1920x1080.

### Initial Webpage
The initial webpage should be centered with a button labeled "Learn More" in the middle of the screen. The background color of the page should be crimson.

![initial webpage](./_images/origin.png)

### Button Details
- The button should have the text "Learn More".
- The button should have a class name `btn`.
- The button should have a relative position and a cursor pointer.

### Hover Effect
When the button is hovered over, it should display a border effect:
- Before the hover, the button should have two pseudo-elements (`:before` and `:after`) with the following properties:
  - `:before` and `:after` should have a width and height of 24px.
  - `:before` should be positioned at the top-left corner of the button with a border-top and border-left of 4px solid darkblue.
  - `:after` should be positioned at the bottom-right corner of the button with a border-bottom and border-right of 4px solid darkblue.
  - Both pseudo-elements should have a transition effect of 0.25s.
- On hover, the pseudo-elements should expand to cover the entire button.

### Hovered Webpage
When the button is hovered over, the pseudo-elements should expand to cover the entire button, creating a border effect around the button.

![hovered webpage](./_images/after_hover.png)

### Container Details
- The container should have a class name `container`.
- The container should use the font family `sans-serif`.

### Resources
- The text content for the button is "Learn More".

### Interactions
- The button should have a hover effect as described.
- Use class name `btn` for the button.
- Use class name `container` for the container.

By following the above description, you should be able to re-implement the webpage with the specified styles and interactions.
