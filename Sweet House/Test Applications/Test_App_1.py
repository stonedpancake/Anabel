for i in "Like now".replace(' ', ''):
    print(f"self.{i} = self.font.render('{i}', True, Color('white'))")
