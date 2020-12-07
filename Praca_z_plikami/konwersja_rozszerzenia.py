from PIL import Image
import os


pic1 = Image.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic1.jpg'))
pic1.save(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic1_new.png'))

pic2 = Image.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic2.jpg'))
pic2.save(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic2_new.png'))

pic3 = Image.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic3.jpg'))
pic3.save(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic3_new.png'))

pic4 = Image.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic4.jpg'))
pic4.save(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic4_new.png'))
