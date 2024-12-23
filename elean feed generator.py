id = ["43", "44"]
url = "https://eleanboutique.ru/kostyum-smoking.html"
price = "84600"
name = "Костюм-смокинг коричневый"
picture1 = "https://eleanboutique.ru/image/cache/catalog/novinki24/osen24/eleanny4180-700x900.jpg"
picture2 = "https://eleanboutique.ru/image/cache/catalog/novinki24/elean27340-700x900.jpg"


categoryId = "5"
description = "Премиальное качество. Итальянская шерсть. Размеры 40-52. В наличии"
text = f'''
<offer id="{id[0]}" available="true">
<url>{url}</url>
<price>{price}</price>
<currencyId>RUB</currencyId>
<categoryId>{categoryId}</categoryId>
<pickup>true</pickup>
<delivery>true</delivery>
<name>{name}</name>
<description>
<![CDATA[ <div><font face="Helvetica">{description}</font></div> ]]>
</description>
<picture>{picture1}</picture>
</offer>
<offer id="{id[1]}" available="true">
<url>{url}</url>
<price>{price}</price>
<currencyId>RUB</currencyId>
<categoryId>{categoryId}</categoryId>
<pickup>true</pickup>
<delivery>true</delivery>
<name>{name}</name>
<description>
<![CDATA[ <div><font face="Helvetica">{description}</font></div> ]]>
</description>
<picture>{picture2}</picture>
</offer>
'''
print(text)