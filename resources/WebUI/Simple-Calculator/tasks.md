
# Task Description: Simple Calculator Webpage

Your job is to design a simple calculator webpage that allows users to perform basic arithmetic operations (addition, subtraction, multiplication, and division) between two numbers. The webpage should be styled and interactive as described below.

## Initial Webpage

The initial webpage should look like this:

![initial webpage](./_images/origin.png)

### Layout and Styling

1. **Body**:
   - Use the font family `sans-serif`.

2. **Main Container**:
   - Use a `div` with class `main` to wrap the content.
   
3. **Inputs Section**:
   - Use a `div` with class `inputs` to wrap the input elements.
   - Include an `h1` element with class `result` to display the result of the calculation. The initial text should be "Result".
   - Use a `select` element with ID `selectOp` to choose the arithmetic operation. The options should be:
     - `+` with value `plus`
     - `-` with value `min`
     - `/` with value `dev`
     - `*` with value `multi`
   - Include two `input` elements with class `num1` and `num2` respectively. These inputs should have placeholders "Number 1" and "Number 2".

4. **Submit Button**:
   - Use a `div` with class `submitBtn` to wrap the button.
   - Include a `button` element with ID `btn` and text "Submit".

### JavaScript Interactivity

- Add an event listener to the button with ID `btn` to perform the calculation when clicked.
- Retrieve the values from the input fields with class `num1` and `num2`.
- Retrieve the selected operation from the `select` element with ID `selectOp`.
- Perform the calculation based on the selected operation and display the result in the `h1` element with class `result`.

### Interaction Steps

1. **Input First Number**:
   - Enter the number `10` in the input field with class `num1`.
   - The webpage should look like this after entering the first number:

   ![after input number 1](./_images/after_input_number1.png)

2. **Input Second Number**:
   - Enter the number `5` in the input field with class `num2`.
   - The webpage should look like this after entering the second number:

   ![after input number 2](./_images/after_input_number2.png)

3. **Select Operation**:
   - Select the `+` operation from the `select` element with ID `selectOp`.
   - The webpage should look like this after selecting the operation:

   ![after select operation](./_images/after_select_operation.png)

4. **Click Submit**:
   - Click the button with ID `btn` to perform the calculation.
   - The result should be displayed in the `h1` element with class `result`.
   - The webpage should look like this after clicking submit:

   ![after click submit](./_images/after_click_submit.png)

### Notes

- The provided screenshots are rendered under a resolution of 1920x1080.
- Ensure that the IDs and class names are used as specified for auto-testing purposes.
