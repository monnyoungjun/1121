import numpy as np
import pandas as pd
import random
import os
import sys
from keras.preprocessing import image
from keras.utils import to_categorical
from keras.preprocessing.image import ImageDataGenerator, load_img
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense, Activation, BatchNormalization
from keras.callbacks import EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.models import load_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#글로벌 다시 정의
FAST_RUN = False
IMAGE_WIDTH = 128
IMAGE_HEIGHT = 128
IMAGE_SIZE = (IMAGE_WIDTH, IMAGE_HEIGHT)
IMAGE_CHANNELS = 3
batch_size = 15

#모델불러오기
#model = load_model('catdog.hdf5')
#model.load_weight('catdog.h5')
model = load_model('./my_model2')

#사진폴더 경로
test_filenames = os.listdir("./test/")
test_df = pd.DataFrame({
    'filename' : test_filenames
})
nb_samples = test_df.shape[0]

#평가 데이터 준비
test_gen = ImageDataGenerator(rescale= 1./255)
test_generator = test_gen.flow_from_dataframe(
    test_df,
    "./test/",
    x_col = 'filename',
    y_col = None,
    class_mode= None,
    target_size= IMAGE_SIZE,
    batch_size = batch_size,
    shuffle= False
)

#모델 예측
predict = model.predict_generator(test_generator, steps = np.ceil(nb_samples/batch_size))
#평가생성
test_df['category'] = np.argmax(predict, axis = -1)
#레이블변환
test_df['category'] = test_df['category'].replace({ 'dog':1, 'cat':0})
#정답비율확인
test_df['category'].value_counts().plot.bar()


#정답확인
sample_test = test_df.head(18)
sample_test.head()
plt.figure(figsize= (12,24))
for index, row in sample_test.iterrows():
    filename = row['filename']
    category = row['category']
    img = load_img("./test/" + filename, target_size=IMAGE_SIZE)
    plt.subplot(6,3, index+1)
    plt.imshow(img)
    plt.xlabel(filename + '('+"{}".format(category) + ')')

plt.tight_layout()
plt.show()

