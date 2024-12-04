
# Task Description: Re-implement a Signup Form with Validation

Your job is to design a webpage that includes a signup form with validation. The form should have fields for full name, email, and password, and should provide feedback for each field. The initial webpage should look like this:

![initial webpage](./_images/origin.png)

## Requirements

1. **HTML Structure**:
    - The webpage should have a `div` with class `container` that covers the entire viewport.
    - Inside the container, there should be another `div` with class `box` that contains the form elements.
    - The form should have a header with the text "Signup".
    - The form should have three input fields: Full Name, Email, and Password.
    - Each input field should have a corresponding label and a placeholder.
    - There should be a submit button with the text "Create Account".
    - Below the form, there should be a footer with a link to login.

2. **CSS Styling**:
    - The background image `wave-haikei.png` should be used for the container's background.
    - The form should be centered both vertically and horizontally.
    - The form should have a shadow effect and rounded corners.
    - The input fields should have a specific style as described in the CSS file.
    - The submit button should change color when hovered over.

3. **JavaScript Validation**:
    - The form should validate the inputs for full name, email, and password.
    - If the inputs are valid, a green checkmark should appear next to the input field.
    - If the inputs are invalid, an error message should be displayed below the input field.

4. **Resources**:
    - Background image: `wave-haikei.png`
    - Font Awesome for icons (include the script file for Font Awesome in your HTML).

5. **Text Content**:
    - Header: "Signup"
    - Placeholder for Full Name: "Type Name Here"
    - Placeholder for Email: "xyz@gmail.com"
    - Placeholder for Password: "at least 8 characters"
    - Submit Button: "Create Account"
    - Footer: "Already have an account? Login"

## Interaction Screenshots

- After filling in the name:

![after filling name](./_images/after_fill_name.png)

- After filling in the email:

![after filling email](./_images/after_fill_email.png)

- After filling in the password:

![after filling password](./_images/after_fill_password.png)

- After submitting the form:

![after submitting form](./_images/after_submit.png)

## Additional Notes

- The provided screenshots are rendered under a resolution of 1920x1080.
- For elements that can be interacted with (click, hover, etc.), use the following IDs and class names:
    - Use ID `name` for the full name input field.
    - Use ID `email` for the email input field.
    - Use ID `password` for the password input field.
    - Use ID `submitBtn` for the submit button.
    - Use class name `fa-solid` for the icons.
    - Use ID `nameError` for the name error message.
    - Use ID `emailError` for the email error message.
    - Use ID `passError` for the password error message.
