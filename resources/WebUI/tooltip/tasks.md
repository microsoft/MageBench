
# Task Description: Re-implement a Tooltip Webpage

Your job is to design a webpage that features tooltips appearing in different directions when hovered over. The initial webpage should look like this:

![initial webpage](./_images/origin.png)

## Requirements

1. **HTML Structure**:
    - Create a `div` element for each tooltip with the class `tooltip`.
    - There should be four tooltips with the following classes and text content:
        - `tooltip top` with text "Show Top"
        - `tooltip right` with text "Show Right"
        - `tooltip left` with text "Show Left"
        - `tooltip bottom` with text "Show Bottom"

2. **CSS Styling**:
    - Use the Google Font "Roboto" with weights 400 and 700. Import it using:
      ```css
      @import url("https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap");
      ```
    - The tooltip messages should appear in different positions relative to the tooltip:
        - Top tooltip message should appear above the tooltip.
        - Right tooltip message should appear to the right of the tooltip.
        - Left tooltip message should appear to the left of the tooltip.
        - Bottom tooltip message should appear below the tooltip.
    - Each tooltip should also have an arrow pointing to the tooltip when hovered over.
    
3. **Interactions**:
    - When hovering over each tooltip, the corresponding message and arrow should appear.
    - The hover interactions should be implemented using CSS only.

## Screenshots

The provided screenshots are rendered under a resolution of 1920x1080.

### Hover over Top Tooltip
![hover over top tooltip](./_images/hover_top.png)

### Hover over Right Tooltip
![hover over right tooltip](./_images/hover_right.png)

### Hover over Left Tooltip
![hover over left tooltip](./_images/hover_left.png)

### Hover over Bottom Tooltip
![hover over bottom tooltip](./_images/hover_bottom.png)

## Element Specifications

- Use class name `tooltip` for all tooltip elements.
- Use class name `top` for the top tooltip.
- Use class name `right` for the right tooltip.
- Use class name `left` for the left tooltip.
- Use class name `bottom` for the bottom tooltip.

## Additional Notes

- Ensure that the tooltips and their messages are styled and positioned correctly as described.
- The hover effects should be smooth and visually appealing.
- No JavaScript is required for the hover effects; they should be achieved using CSS only.
