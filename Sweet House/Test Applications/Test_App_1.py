for i in "Do you want to talk?".replace(' ', ''):
    print(f"self.{i} = self.font.render('{i}', True, Color('white'))")
