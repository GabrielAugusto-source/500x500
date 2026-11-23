from PIL import Image


img = Image.open('assets/evolution_120822.png').convert('RGBA')


img.thumbnail((420, 420), Image.Resampling.LANCZOS)


canvas = Image.new('RGBA', (500, 500), (255, 255, 255, 255))


largura, altura = img.size
x = (500 - largura) // 2
y = (500 - altura) // 2


canvas.paste(img, (x, y), img)


canvas.convert('RGB').save('assets/evolution_quadrada.png')
print("Imagem quadrada gerada com sucesso em assets/evolution_quadrada.png!")
