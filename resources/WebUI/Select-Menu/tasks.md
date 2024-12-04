
# Task Description: Social Media Menu Select Webpage

Your job is to design a webpage that allows users to select a social media platform from a dropdown menu. The initial webpage should look like this:

![initial webpage](./_images/origin.png)

## Requirements

### HTML Structure

1. **Header Section**:
   - Create a `header` element that will contain the dropdown menu.

2. **Dropdown Menu**:
   - Create a `div` with the class `selector` to wrap the dropdown menu.
   - Inside the `selector` div, create another `div` with the ID `selectField`. This will be the clickable area to open the dropdown.
   - Inside the `selectField` div, add a `p` element with the ID `selectText` and the text content "Select Social Media".
   - Add an `img` element with the ID `arrowIcon` and the source `images/arrow.png`.

3. **Dropdown List**:
   - Create an unordered list (`ul`) with the ID `list` and the class `hide`.
   - Inside the `list` ul, create list items (`li`) with the class `options` for each social media platform. Each `li` should contain:
     - An `img` element for the social media icon.
     - A `p` element with the name of the social media platform.

### CSS Styling

1. **General Styles**:
   - Apply a margin and padding of 0 and use the `sans-serif` font family for all elements.


### JavaScript Functionality

1. **Toggle Dropdown**:
   - Add an event listener to the `selectField` div to toggle the `hide` class on the `list` ul and the `rotate` class on the `arrowIcon` img when clicked.

2. **Select Option**:
   - Add an event listener to each `li` with the class `options` to update the `selectText` p element with the selected option's text content and toggle the `hide` and `rotate` classes.

### Resources

- **Images**:
  - `images/arrow.png` for the dropdown arrow icon.
  - `images/facebook.png` for the Facebook icon.
  - `images/instagram.png` for the Instagram icon.
  - `images/pinterest.png` for the Pinterest icon.
  - `images/twitter.png` for the Twitter icon.
  - `images/whatsapp.png` for the WhatsApp icon.
  - `images/youtube.png` for the YouTube icon.

### Screenshots

The provided screenshots are rendered under a resolution of 1920x1080.

- **Dropdown Open**:
  ![dropdown open](./_images/dropdown_open.png)


### Element Identifiers

- Use ID `selectField` for the clickable area to open the dropdown.
- Use ID `selectText` for the text displaying the selected option.
- Use ID `arrowIcon` for the dropdown arrow icon.
- Use ID `list` for the dropdown list.
- Use class name `options` for each list item in the dropdown.

### Animations

- The arrow icon should rotate 180 degrees when the dropdown is opened and revert back when closed.
