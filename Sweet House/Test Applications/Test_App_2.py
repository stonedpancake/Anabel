SIZE = 900
for i in "Likenow".replace(' ', ''):
    for size in range(10):
        SIZE += 20
        print(f"self.screen.blit(self.{i}, ({SIZE}, 200))")
        print('time.delay(100)')
        print('display.flip()')
        break