import matplotlib.pyplot as plt
Popularity = Song_data['popularity']
Energy = Song_data[‘energy’]

plt.scatter(Popularity,Energy)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

Popularity_array = np.array(Popularity)

plt.pie(Popularity_array)
plt.show() 

import matplotlib.pyplot as plt

Values_thousand_songs = ten_thousand_songs['description'].style
Values_thousand_songs

Popularity_Column =  np.array(Values_thousand_songs[‘popularity'])

Std = Popularity_Column[2]
Mean = Popularity_Column[1]

plt.plot(Popularity,Std)
plt.xlim(-3,3)

import numpy as np

Z_score = (50-Mean)/Std

from scipy import stats
stats.zscore(Z_score)
