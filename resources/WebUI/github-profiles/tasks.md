
# Task Description: Re-implement the GitHub Profiles Webpage

Your job is to design a webpage that allows users to search for GitHub profiles and display relevant information. The webpage should look and function as described below. The provided screenshots are rendered under a resolution of 1920x1080.

## Initial Webpage

The initial webpage should be a simple search form centered on the page. The form should have an input field where users can type a GitHub username.

![initial webpage](./_images/origin.png)

### Elements and Styling

- The webpage should use the `Poppins` font from Google Fonts.
- The webpage should be centered both vertically and horizontally.

### Form

- The form should have a class name `user-form` and an ID `form`.
- The input field should have an ID `search` and a placeholder text "Search a Github User".

## After Entering Username

When a user enters a GitHub username (e.g., "octocat") in the input field, the input field should display the entered text.

![after entering username](./_images/after_enter_username.png)

## After Submitting Form

Upon submitting the form, the webpage should display the GitHub profile information of the entered username. This includes the user's avatar, name, bio, followers, following, and public repositories.

![after submitting form](./_images/after_submit_form.png)

### Profile Card

- The profile card should have a class name `card`.

### Avatar

- The avatar image should have a class name `avatar`.
- The avatar should have the following styles:

### User Information

- The user information section should have a class name `user-info`.
- The user information should include the user's name (or login if the name is not available), bio, followers, following, and public repositories.

### Repositories

- The repositories section should have an ID `repos`.
- Each repository link should have a class name `repo`.

### Error Handling

- If the entered username does not exist, display an error message in a card with the class name `card`.

### Media Queries

- For screens with a maximum width of 500px, the profile card should be displayed in a column layout and centered.

## External Resources

- The webpage uses the `axios` library for making HTTP requests to the GitHub API. Include the following script in your HTML:
  ```html
  <script src="https://cdnjs.cloudflare.com/ajax/libs/axios/0.21.0/axios.min.js" integrity="sha512-DZqqY3PiOvTP9HkjIWgjO6ouCbq+dxqWoJZ/Q+zPYNHmlnI2dQnbJ5bxAHpAMw+LXRm4D72EIRXzvcHQtE8/VQ==" crossorigin="anonymous"></script>
  ```

- The webpage uses the `Poppins` font from Google Fonts. Include the following import in your CSS:
  ```css
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;400&display=swap');
  ```

## Interaction Details

- When the form with ID `form` is submitted, the JavaScript function `getUser` should be called with the entered username.
- The `getUser` function should fetch the user's profile information from the GitHub API and display it on the webpage.
- If the user has public repositories, the first 5 repositories should be displayed as links.
- If there is an error (e.g., the username does not exist), an error message should be displayed.
