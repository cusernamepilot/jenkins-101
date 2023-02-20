import fire

def hello(name="World123"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
