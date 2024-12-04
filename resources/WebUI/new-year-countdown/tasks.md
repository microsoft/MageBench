
# Task Description: New Year Countdown Webpage

Your job is to design a webpage that displays a countdown to the New Year. The webpage should have a background image, a title, and a countdown timer that updates every second. Below are the detailed requirements and resources needed to re-implement the webpage.

## Initial Webpage
The initial webpage should be:
![initial webpage](./_images/origin.png)



## Requirements

### HTML Structure
1. The webpage should have a `div` with the class `year` and ID `year` to display the upcoming year.
2. The title of the webpage should be an `h1` element with the text "New Year Countdown".
3. The countdown timer should be a `div` with the class `countdown` and ID `countdown`, containing four `div` elements with the class `time` for days, hours, minutes, and seconds.
4. Each `time` `div` should contain an `h2` element for the numeric value and a `p` element with a `small` tag for the label (days, hours, minutes, seconds).
5. An `img` element with the class `loading` and ID `loading` should be used to display a loading image initially.

### CSS Styling
1. Use the Google Font "PT Sans Narrow" for the entire webpage.
2. The background of the webpage should be an image from the URL: `bg.png`.
4. The webpage should be centered both vertically and horizontally, with a flexbox layout.
6. The `countdown` element should be hidden initially and displayed as a flexbox with a scale transformation.
7. The `time` elements should be styled to align items and justify content to the center, with appropriate margins and font sizes for different screen widths.

### JavaScript Functionality
1. Use JavaScript to calculate the time difference between the current time and the next New Year.
2. Update the countdown timer every second.
3. After a 1-second delay, remove the loading image and display the countdown timer.
4. Set the `year` element's text to the upcoming year.

### Resources
- Background Image: `bg.png`.
- Loading Image: `resource1.png`
- Font: "PT Sans Narrow" from Google Fonts

### Element IDs and Class Names
- Use ID `year` for the element displaying the upcoming year.
- Use ID `countdown` for the countdown timer container.
- Use class name `time` for each time unit container (days, hours, minutes, seconds).
- Use ID `loading` for the loading image.

### Screenshots
The provided screenshots are rendered under a resolution of 1920x1080.

By following the above description, you should be able to re-implement the New Year Countdown webpage successfully.
