import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot(scores, mean_scores, xlabel, ylabel, epsilon):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title(f'Training... epsilon {"%.3f" % epsilon}')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))