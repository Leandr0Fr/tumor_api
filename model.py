import numpy as np
import tensorflow
from PIL import Image

def prediction():
    #Carga el modelo.
    model = tensorflow.keras.models.load_model("tumor_model.h5")
    img = Image.open("image.png").convert("L")
    #Transforma la imagen para que coincidan con el modelo. 
    img = img.resize((224, 224)) 
    img = np.array(img)
    img = img / 255.0
    img = img.reshape((1,224,224,1))
    #Predice el modelo
    predict = model.predict(img)    
    #Como son 4 clases, entonces es un arreglo de 4 elementos.
    #Entonces, predicted_class retorna la posición del arreglo donde la posición es la clase que predice.
    predicted_class = np.argmax(predict)
    return classify_result(predicted_class)

def classify_result(index):
    class_model = ["Glioma", "Meningioma", "Pituitary", "No_tumor"]
    return class_model[index]
