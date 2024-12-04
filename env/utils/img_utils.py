from PIL import Image
  
def resize_image(image: Image.Image, max_size: int) -> Image.Image:  
    """  
    Resize an image while maintaining its aspect ratio such that the longest side is max_size.  
  
    :param image: An instance of Image.Image.  
    :param max_size: The desired size of the longest side of the image.  
    :return: A resized Image.Image instance.  
    """  
    # Get the original dimensions  
    original_width, original_height = image.size  
      
    # Determine the scaling factor  
    if original_width > original_height:  
        scaling_factor = max_size / float(original_width)  
    else:  
        scaling_factor = max_size / float(original_height)  
      
    # Calculate the new dimensions  
    new_width = int(original_width * scaling_factor)  
    new_height = int(original_height * scaling_factor)  
      
    # Resize the image  
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)  
      
    return resized_image 