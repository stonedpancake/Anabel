SIZE = 880
for i in "abcdefghijklmnopqrstuvwxyz":
    print(f"if event_.key == K_{i}:")
    print()
    print(f'\tself.screen.blit(self.{i.upper()}, (self.keyboard_x, self.keyboard_y))')
    print('\tdisplay.flip()')
    print('\ttime.delay(400)')
    print()
