
# Task Description: Form Validator Webpage

Your job is to design a webpage that includes a form validator. The form consists of fields for username, email, password, and password confirmation. The form should provide real-time validation messages for each field. Below are the detailed requirements and resources needed to re-implement the webpage.

## Initial Webpage
The initial webpage should look like this:
![initial webpage](./_images/origin.png)

## Resources
### Images
- `resource1.jpg` is used for the background image on the right side of the form.

### Text Content
- The text content for the heading is:
  ```
  Shoe 
  Palace
  ```

## Layout and Styling
- Use a CSS file named `style.css` for styling.
- The webpage should have a dark background color.
- The form should be centered and have a semi-transparent border.
- The form fields should have padding and a specific width.
- The submit button should have a primary color background and change the cursor to a pointer on hover.
- Error messages should be hidden by default and only shown when validation fails.
- The background image should be positioned absolutely on the right side of the form.
- The heading should be positioned absolutely and have a large font size.

## Form Elements
- The form should include the following input fields:
  - Username: Use ID `username` and class `username`.
  - Email: Use ID `email` and class `email`.
  - Password: Use ID `password1` and class `password1`.
  - Confirm Password: Use ID `password2` and class `password2`.
- Each input field should have an associated error message paragraph with the class `msg` and a specific class for each field (e.g., `user-msg`, `email-msg`).
- The submit button should have the class `submit`.

## Interactions and Validations
- When the form is submitted, validate each field:
  - If the username is empty, show the message "Please Provide Your Name" in red.
  - If the email is empty, show the message "Please Provide Your Email" in red.
  - If the password is empty, show the message "Please Provide Your Password" in red.
  - If the confirm password is empty or does not match the password, show the appropriate error message in red.
  - If the fields are valid, show success messages in green.
- Use the `showMessage` function to display validation messages and change the border color of the input fields.

## Screenshots of Intermediate Steps
The screenshots below show the intermediate steps of the form validation process. These screenshots were rendered under a resolution of 1920x1080.

### After Submitting Form
![after submitting form](./_images/after_submit.png)

## Additional Notes
- Ensure that the form validation messages are displayed correctly based on the input values.
- The form should prevent submission if any field is invalid.
- The provided screenshots should be used as a reference to ensure the webpage is implemented correctly.

By following the above instructions and using the provided resources, you should be able to re-implement the form validator webpage successfully.
