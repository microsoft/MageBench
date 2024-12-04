
# Task Description: Creative Card 2 Webpage

Your job is to design a webpage that features a creative card with hover effects. The initial webpage should look like this:

![initial webpage](./_images/origin.png)

## Requirements

1. **Background and Layout:**
   - The webpage should be centered both vertically and horizontally.
   - Use the `sans-serif` font family for the entire webpage.

2. **Card:**
   - The card should have two pseudo-elements (`:before` and `:after`) that cover the entire card and have a white background. These pseudo-elements should have a transition effect of `1s`.

3. **Hover Effects:**
   - When the card is hovered over, the `:before` pseudo-element should rotate by `20deg` and have a box shadow of `0 2px 20px rgba(0, 0, 0, 0.2)`.
   - When the card is hovered over, the `:after` pseudo-element should rotate by `10deg` and have a box shadow of `0 2px 20px rgba(0, 0, 0, 0.2)`.
   - When the card is hovered over, the `.imgBox` should move up, reducing its bottom margin to `80px`.

4. **Image Box:**
   - The image box should have a background color of `#222` and a transition effect of `1s`.
   - The image inside the image box should cover the entire box, maintaining its aspect ratio using `object-fit: cover`.

6. **Text Content:**
   - The heading inside the details section should display the text "Olivia".

7. **Image Resource:**
   - Use the image `marian-oleksyn-Edv_EEWiB3E-unsplash.jpg` for the card's image.

## Interaction

When the user hovers over the card, the card should animate as described above. The webpage after hovering over the card should look like this:

![after hover](./_images/after_hover.png)

## Additional Information

- The provided screenshots are rendered under a resolution of `1920x1080`.
- Ensure to use the following class names for the elements:
  - Use class name `card` for the card container.
  - Use class name `imgBox` for the image container.
  - Use class name `details` for the details section.
