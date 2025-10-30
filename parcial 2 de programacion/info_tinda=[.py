info_tiend=("Bienvenido a Gameplanet. 2010")
stock = { 
    "COD MW2" :{"nombre":'COD', "precio": 1500,"stock":15},
    "Smash Bros ultimate" :{"nombre":"Smash Bros", "precio":1200,"stock":12},
    "Assasing creed II" :{"nombre":"Assasing Creed II", "precio":1100,"stock":10},
    "minecraft":{"nombre":"Minecraft", "precio":300,"stock":10}
}
print(stock)
print("Actualización de stock")
stock["minecraft"]['stock']-=1
print(stock['minecraft'])
print("=======================================================================")
stock["COD MW2"]['stock']-=1
print(stock['COD MW2'])
print("=============================================================================")
stock["Smash Bros ultimate"]['stock']+=3
print(stock['Smash Bros ultimate'])
print("///////////////////////////////////////////////////////////////")