from ckiptagger import WS

text = '〔體育中心／綜合報導〕為了紀念墜機驟逝的傳奇球星布萊恩（Kobe Bryant）與其二女兒吉安娜（Gianna Bryant），2020年芝加哥明星賽，詹姆斯（LeBron James）所率領的「Team LeBron」將換上吉安娜背號的「2」號球衣，亞德托昆波（Giannis Antetokounmpo）的「Team Giannis」則是布萊恩的「24」號球衣，而詹姆斯受訪時揭密了自己選擇「2」號球衣的原因。'
ws = WS("./data")

ws_results = ws([text])

print(ws_results)
