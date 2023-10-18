from PIL import Image, ImageDraw, ImageFont


def make_graphic():
  background = Image.open('misc/background.png')
  map1 = Image.open('maps/brine.png')
  map2 = Image.open('maps/manta.png')
  percentage = 80
  map1_width, map1_height = map1.size
  new_width = int(map1_width * (percentage / 100))
  new_height = int(map1_height * (percentage / 100))
  resized_map1 = map1.resize((new_width, new_height))
  resized_map2 = map2.resize((new_width, new_height))

  background.paste(resized_map1, (0,665), mask = resized_map1)
  background.paste(resized_map2, (0,320), mask = resized_map2)

  draw = ImageDraw.Draw(background)
  text = "Turf War"
  font_size = 100
  myFont = ImageFont.truetype('Splatoon1.ttf', 60)
  text_color = (144, 238, 144)  
  position = (130,40)
  draw.text(position, text, fill=text_color, font=myFont)
  #//
  draw = ImageDraw.Draw(background)
  text = "Timeframe 5:00 - 7:00pm"
  font_size = 100
  myFont = ImageFont.truetype('Splatoon1.ttf', 30)
  text_color = (0, 0, 0) 
  position = (90,220)
  draw.text(position, text, fill=text_color, font=myFont)
  background.save("final.png")
  return ("final.png")

