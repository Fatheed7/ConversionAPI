def temp_calcs(from_type, to_type, value):
  if from_type == "celsius":
    if to_type == "fahrenheit":
      print("Test")
      return (value * 9/5) + 32
    elif to_type == "kelvin":
      return value + 273.15
  elif from_type == "fahrenheit":
    if to_type == "celsius":
      return (value - 32) * 5/9
    elif to_type == "kelvin":
      return (value + 459.67) * 5/9
  elif from_type == "kelvin":
    if to_type == "celsius":
      return value - 273.15
    elif to_type == "fahrenheit":
      return (value * 9/5) - 459.67