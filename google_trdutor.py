import googletrans
from googletrans import Translator

translator = Translator()

translation = translator.translate("These projects provide advanced insights and charting tools to track historical token prices, real-time trades and volume. Other more advanced features include impermanent loss calculation and data querying. Some of these projects may require you to hold a certain number of tokens to access the full version of their product suite.", dest='pt')
print(translation.text)
