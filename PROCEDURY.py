import math
def vzdalenost(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return (dx**2 + dy**2)**0.5  

def obsahy(body):
  
    max_vzdalenost = 0
    nejvzdalenejsi_body = None
    for i in range(len(body)):
        for j in range(i + 1, len(body)):
            vzd = vzdalenost(body[i][0], body[i][1], body[j][0], body[j][1])
            if vzd > max_vzdalenost:
                max_vzdalenost = vzd
                nejvzdalenejsi_body = (body[i], body[j])

    sirka = abs(nejvzdalenejsi_body[0][0] - nejvzdalenejsi_body[1][0])
    vyska = abs(nejvzdalenejsi_body[0][1] - nejvzdalenejsi_body[1][1])
    obsah_obdelniku = sirka * vyska

    polomer = max_vzdalenost / 2
    obsah_kruhu = 3.141592653589793 * polomer**2 
    return obsah_obdelniku, obsah_kruhu


body = [(1, 2), (3, 4), (5, 6), (7, 8)]
obsah_obdelniku, obsah_kruhu = obsahy(body)
print(f"Obsah obdélníku: {obsah_obdelniku}")
print(f"Obsah kruhu: {obsah_kruhu}")