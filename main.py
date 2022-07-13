
import numpy as np
import pickle


#SVM
# loading the saved model
loaded_model_svm = pickle.load(open('C:/Users/prasa/OneDrive/Desktop/Diabetes/trained_model_svm.sav', 'rb'))

#RFC
# loading the saved model
loaded_model_rfc = pickle.load(open('C:/Users/prasa/OneDrive/Desktop/Diabetes/trained_model_rfc.sav', 'rb'))


input_data = (5,166,72,19,175,25.8,0.587,51)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

#SVM Prediction
prediction_svm = loaded_model_svm.predict(input_data_reshaped)
print(prediction_svm)

if (prediction_svm[0] == 0):
  print('The person is not diabetic(SVM)')
else:
  print('The person is diabetic(SVM)')


#RFC Prediction
prediction_rfc = loaded_model_rfc.predict(input_data_reshaped)
print(prediction_rfc)

if (prediction_rfc[0] == 0):
  print('The person is not diabetic(RFC)')
else:
  print('The person is diabetic(RFC)')








