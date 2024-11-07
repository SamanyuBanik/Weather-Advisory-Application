weather = int(input(" Enter the current weather: "))
if weather == 0:
    print(" Its too cold outside! Wear many layers!")
elif  0 < weather < 10:
    print(" Its very cold! Wear heavy clothing and bring extra jackets with you!")
elif 10 < weather < 20:
    print(" Its mild and cool outside! Wear heavy clothing and bring extra in case you get chilly!")
elif 20 < weather < 30:
    print(" The weather is warm & hot! Wear lightweight clothing and carry water, hats, sunglasses, and sunscreen!")
elif 30 < weather < 40:
    print(" The weather is very hot! Wear light & breathable fabrics, and carry water and sun protections with you!")
