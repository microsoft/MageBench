
Your task is to design a webpage that features a single interactive button with a hover effect. The initial webpage should look like this:

![initial webpage](./_images/origin.png)

### Requirements:

1. **HTML Structure**:
    - Create a basic HTML structure with a `head` and `body`.
    - Include a `title` tag with the text "Btn 1".
    - Inside the `body`, create a `section` element with the class `container`.
    - Inside the `section`, add an `a` tag with the text "Hover Me".
    
2. **CSS Styling**:
    - Apply the following styles globally:
        - Remove padding and margin.
        - Set `box-sizing` to `border-box`.
    - Style the `.container` class to:
        - Use flexbox to center its content both horizontally and vertically.
        - Use the `sans-serif` font family.
    - Style the `a` tag to:
        - Remove text decoration.
        - Hide overflow.
        - Apply a transition effect of 1 second for all properties.
    - Add a `:before` pseudo-element to the `a` tag to:
        - Set its content to "DOWNLOAD".
        - Apply a transition effect of 1 second for all properties.
        - Center its content using flexbox.
    - Add a hover effect to the `a` tag so that the `:before` pseudo-element slides down to cover the `a` tag using `transform: translateY(0)`.
    
3. **Interactivity**:
    - When the user hovers over the `a` tag, the `:before` pseudo-element should slide down to cover the `a` tag, changing the text to "DOWNLOAD".

The webpage after hovering over the link should look like this:

![after hover](./_images/after_hover.png)

### Additional Information:
- The provided screenshots are rendered under a resolution of 1920x1080.
- Ensure that the `a` tag has the text "Hover Me" initially.
- Use the class name `container` for the `section` element.
- Use the `:before` pseudo-element for the hover effect on the `a` tag.
