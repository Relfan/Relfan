class Load:
  @staticmethod
  def __onload__():
    print("Starting Python app...")
    main(text="Loaded", final=1)
  @staticmethod
  def main(**entries):
    print(entries['text'])
    return entries['final']
