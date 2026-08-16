'''
#14 Quiambao, King Berlin M.
9-Samat
08/16/26
'''
zodiacYrs = (1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911)

birthYr = int(input("Enter your birth year: "))

if not birthYr >= 1900:
    print("\nInvalid Year, it should not be earlier than 1900")
    
else:
    while not birthYr in zodiacYrs:
        birthYr = birthYr - 12
        
    if birthYr == 1900:
        print("\nYour Chinese Zodiac Sign is: Rat (鼠 / Shǔ)")
        
    elif birthYr == 1901:
        print("\nYour Chinese Zodiac Sign is: Ox (牛 / Niú)")
        
    elif birthYr == 1902:
        print("\nYour Chinese Zodiac Sign is: Tiger (虎 / Hǔ)")
        
    elif birthYr == 1903:
        print("\nYour Chinese Zodiac Sign is: Rabbit (兔 / Tù)")
        
    elif birthYr == 1904:
        print("\nYour Chinese Zodiac Sign is: Dragon (龙 / Lóng)")
        
    elif birthYr == 1905:
        print("\nYour Chinese Zodiac Sign is: Snake (蛇 / Shé)")
        
    elif birthYr == 1906:
        print("\nYour Chinese Zodiac Sign is: Horse (马 / Mǎ)")
        
    elif birthYr == 1907:
        print("\nYour Chinese Zodiac Sign is: Goat (羊 / Yáng)")
        
    elif birthYr == 1908:
        print("\nYour Chinese Zodiac Sign is: Monkey (猴 / Hóu)")
        
    elif birthYr == 1909:
        print("\nYour Chinese Zodiac Sign is: Rooster (鸡 / Jī)")
        
    elif birthYr == 1910:
        print("\nYour Chinese Zodiac Sign is: Dog (狗 / Gǒu)")
        
    elif birthYr == 1911:
        print("\nYour Chinese Zodiac Sign is: Pig (猪 / Zhū)")













