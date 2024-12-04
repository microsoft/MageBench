
# Task Description: Implement a Rounded Navbar with Interactive Icons

Your job is to design a webpage that features a rounded navbar with interactive icons. The initial webpage should look like this:

![initial webpage](./_images/origin.png)

## Requirements

### HTML Structure

1. **Navbar Wrapper**: Create a `div` with the class `navbar-wrapper` to contain the entire navbar.
2. **Navbar**: Inside the `navbar-wrapper`, create another `div` with the class `navbar`.
3. **Navbar Links**: Add six `a` elements with the class `navbar-link` inside the `navbar`. Each `a` element should contain an `i` element with the appropriate Font Awesome icon class:
   - Home: `<i class="fas fa-home"></i>`
   - City: `<i class="fas fa-city"></i>`
   - School: `<i class="fas fa-school"></i>`
   - Landmark: `<i class="fas fa-landmark"></i>`
   - Hotel: `<i class="fas fa-hotel"></i>`
   - Store: `<i class="fas fa-store-alt"></i>`
4. **Navbar Button**: Add a `div` with the class `navbar-btn` inside the `navbar-wrapper`. This `div` should contain an `i` element with the class `fas fa-plus`.

### JavaScript Functionality

1. **Toggle Navbar**: Add an event listener to the `navbar-btn` that toggles the `change` class on the `navbar-wrapper` when clicked.

### Interaction Screenshots

- After clicking the navbar button, the navbar should expand and reveal the icons:

  ![after clicking navbar button](./_images/after_click.png)

- Hovering over the home icon should change its color:

  ![hover over home icon](./_images/hover_home.png)

- Hovering over the city icon should change its color:

  ![hover over city icon](./_images/hover_city.png)


### Resources

- Font Awesome for icons: 
  ```html
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
    integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g=="
    crossorigin="anonymous"
    referrerpolicy="no-referrer"
  />
  ```

### Notes

- The provided screenshots are rendered under a resolution of 1920x1080.
- Ensure that the class names and IDs are used exactly as specified to match the auto-testing requirements.
