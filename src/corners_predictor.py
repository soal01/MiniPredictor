import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import InputLayer, Dense
import keras

columns_for_corners = ['Хозяева', 'Гости', 'Владение мячом хозяев', 'Владение мячом гостей',
                        'Удары по воротам хозяев', 'Удары по воротам гостей',
                       'Удары в створ хозяев', 'Удары в створ гостей',
                        'Заблокированные удары хозяев', 'Заблокированные удары гостей',
                        'Сэйвы хозяев', 'Сэйвы гостей',
                       'Угловые удары хозяев', 'Угловые удары гостей']

columns_for_corners_home = ['Хозяева', 'Владение мячом хозяев','Удары по воротам хозяев',
                       'Удары в створ хозяев', 'Заблокированные удары хозяев', 'Сэйвы гостей']

columns_for_corners_guest = ['Гости', 'Владение мячом гостей','Удары по воротам гостей',
                       'Удары в створ гостей','Заблокированные удары гостей', 'Сэйвы хозяев']




def convert_percents(s):
    return int(s[:-1])


class Corners_predictor:
    def __init__(self, name):
        self.data = pd.read_csv(name)
        self.data['Владение мячом хозяев'] = self.data['Владение мячом хозяев'].apply(convert_percents)
        self.data['Владение мячом гостей'] = self.data['Владение мячом гостей'].apply(convert_percents)
        self.model = Sequential([
            Dense(8, input_shape=(6,)),
            Dense(128, activation='sigmoid'),
            Dense(64, activation='sigmoid'),
            Dense(1, )
        ])

        self.model.compile(loss=keras.losses.cosine,
                           optimizer=keras.optimizers.Adam(learning_rate=0.005),
                           metrics=["accuracy"])

    def get_corners_of_team(self, team):
        ans = self.data[(self.data['Хозяева'] == team) | (self.data['Гости'] == team)]
        ans = ans[columns_for_corners]
        return ans

    def get_part_train_data(self, data, team, y_column, is_home):
        x_data = []
        if is_home:
            data = data[data['Хозяева'] == team]
            columns = columns_for_corners_home
        else:
            data = data[data['Гости'] == team]
            columns = columns_for_corners_guest
        #print(data)
        y_data = np.array(data[y_column][1:])
        y_data = np.array([[el] for el in y_data])
        for i in range(1, len(data.index)):
            current_row = [is_home]
            for column in columns[1:]:
                current_row.append(data[column][:i].mean())
            current_row = np.array(current_row)
            x_data.append(current_row)
        x_data = np.array(x_data)
        return x_data, y_data

    def get_train_data(self, data, team, y_column):
        x_home_train, y_home_train = self.get_part_train_data(data, team, y_column, True)
        x_guest_train, y_guest_train = self.get_part_train_data(data, team, y_column, False)
        #print(x_home_train)
        #print(x_guest_train)
        x_train = np.concatenate((x_home_train, x_guest_train))
        y_train = np.concatenate((y_home_train, y_guest_train))
        #print(x_train)
        return x_train, y_train

    def get_part_of_arguments_for_predict(self, data, team, is_home):
        if is_home:
            data = data[data['Хозяева'] == team]
            columns = columns_for_corners_home
        else:
            data = data[data['Гости'] == team]
            columns = columns_for_corners_guest
        row = [is_home]
        for column in columns[1:]:
            row.append(data[column].mean())
        row = np.array(row)
        return row

    def get_arguments_for_predict(self, data, team):
        home_arguments = self.get_part_of_arguments_for_predict(data, team, True)
        guest_arguments = self.get_part_of_arguments_for_predict(data, team, False)
        arguments = np.concatenate(([home_arguments], [guest_arguments]))
        return arguments

    def predict(self, x_train, y_train, x_predict):
        print(y_train)
        self.model.fit(x_train, y_train, epochs=600)
        print(x_predict)
        predict = self.model.predict(x_predict)
        values = map(int, predict)
        with open('predicts.txt', 'w') as f:
            for value in values:
                f.write(str(value) + '\n')
        return predict


predictor = Corners_predictor('BL_matches.csv')
df = predictor.get_corners_of_team('ФК Бавария')
x_train, y_train = predictor.get_train_data(df, 'ФК Бавария', 'Угловые удары хозяев')
x_predict = predictor.get_arguments_for_predict(df, 'ФК Бавария')
predicts = predictor.predict(x_train, y_train, x_predict)


