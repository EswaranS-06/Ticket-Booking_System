print("\033[<style>;<color>;<bg_color>m hello \033[0m")
print("\033[<style>;<color>m hello \033[0m")
print("\033[<color>;<bg_color>m hello \033[0m")
print("\033[<color>m hello \033[0m")

print("""
color: 
    black :     30
    Red :       31
    Green :     32
    Yellow :    33
    Blue :      34
    Magenta :   35
    Cyan :      36
    White : Default
    
Bg Color:
    black :     40
    Red :       41
    Green :     42
    Yellow :    43
    Blue :      44
    Magenta :   45
    Cyan :      46
    White :     47
    
Style Codes:
    Reset : 0
    Bold : 1
    Underline : 4
    Reversed : 7
      """)