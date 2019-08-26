#user defined module
import characterextraction
import pickle
print("Loading model")
filename = './finalized_model.sav'
model = pickle.load(open(filename, 'rb'))

print('Model loaded. Predicting characters of number plate')
classification_result = []
for each_character in characterextraction.characters:
    
    each_character = each_character.reshape(1, -1)
    result = model.predict(each_character)
    classification_result.append(result)

# print('Classification result')
# print(classification_result)

plate_string = ''
for eachPredict in classification_result:
    plate_string += eachPredict[0]

print('Predicted license plate')
print(plate_string)



column_list_copy = characterextraction.column_list[:]
characterextraction.column_list.sort()
rightplate_string = ''
for each in characterextraction.column_list:
    rightplate_string += plate_string[column_list_copy.index(each)]

# the re-arranged order as in original plate
print('License plate')
print(rightplate_string)