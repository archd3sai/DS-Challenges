# libraries
import matplotlib
matplotlib.rcParams['figure.dpi'] = 120 #resolution
matplotlib.rcParams['figure.figsize'] = (8,6) #figure size

import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import seaborn as sns

# for a single plot
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(autoencoder_w1_history['accuracy'], linewidth = 1, label = "Accuracy")
ax.plot(autoencoder_w1_history['val_accuracy'], linewidth = 1, label = "Validation Accuracy")

# for multiple subplots
fig, ax = plt.subplots(1,2, figsize=(5, 3))
ax[0].plot(autoencoder_w1_history['accuracy'], linewidth = 1, label = "Accuracy")
ax[1].plot(autoencoder_w1_history['val_accuracy'], linewidth = 1, label = "Validation Accuracy")

fig, ax = plt.subplots(2,2, figsize=(5, 3))
ax[0,0].plot(autoencoder_w1_history['accuracy'], linewidth = 1, label = "Accuracy")
ax[1,1].plot(autoencoder_w1_history['val_accuracy'], linewidth = 1, label = "Validation Accuracy")

# setting legend and its font size
ax.legend(loc = 'best', prop={'size': 8})

# setting title
ax.set_title('Model Accuracy', size = 12)

# setting labels
ax.set_xlabel('Epochs', size = 10)
ax.set_ylabel('Accuracy', size = 10);

# setting label size
ax.tick_params(axis = 'both', labelsize = 8)

# for limits
ax.set_xlim(2,10)
ax.set_ylim(2,10)

# for rotation 
ax.xaxis.set_tick_params(rotation=0)

# for seaborn plots specify axis as ax
sns.lineplot(range(10), autoencoder_w1_history['accuracy'], ax = ax, linewidth = 1, label = "Accuracy")
sns.lineplot(range(10), autoencoder_w1_history['val_accuracy'], ax = ax, linewidth = 1, label = "Validation Accuracy")
