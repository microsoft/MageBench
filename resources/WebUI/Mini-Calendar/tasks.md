
Your task is to design a mini calendar webpage. The webpage should display the current month, day of the week, day of the month, and year. The initial webpage should look like this:

![initial webpage](./_images/origin.png)

The provided screenshots are rendered under a resolution of 1920x1080.

### Layout and Styling

1. **Body**
   - The body should have a margin of 0.
   - Use flexbox to center the content both vertically and horizontally.
   - Use the font family `cursive`.
   
2. **Calendar Container**
   - Use a `div` with the class name `calendar-container`.
   - Center the text inside the container.
   - Ensure the container does not overflow its content.
   
3. **Month Name**
   - Use a `p` element with the class name `month-name` and ID `month-name`.
   
4. **Day Name**
   - Use a `p` element with the class name `day-name` and ID `day-name`.
   
5. **Day Number**
   - Use a `p` element with the class name `day-number` and ID `day-number`.
   
6. **Year**
   - Use a `p` element with the class name `year` and ID `year`.

### JavaScript Functionality

1. **Elements**
   - Use the following IDs to get the elements:
     - `month-name` for the month name.
     - `day-name` for the day name.
     - `day-number` for the day number.
     - `year` for the year.

2. **Date Handling**
   - Use JavaScript's `Date` object to get the current date.
   - Set the inner text of the `month-name` element to the full name of the current month.
   - Set the inner text of the `day-name` element to the full name of the current day of the week.
   - Set the inner text of the `day-number` element to the current day of the month.
   - Set the inner text of the `year` element to the current year.


