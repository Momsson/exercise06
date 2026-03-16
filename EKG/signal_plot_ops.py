import matplotlib.pyplot as plt


def load_signal_from_txt(path):
    values = []

    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                values.append(float(line))

    return values


def signal_min(values):
    return min(values)


def signal_max(values):
    return max(values)


def signal_avg(values):
    return sum(values) / len(values)


def plot_signal(values):
    plt.plot(values)
    plt.title("Signal Plot")
    plt.xlabel("Sample")
    plt.ylabel("Value")
    plt.show()


if __name__ == "__main__":

    values = load_signal_from_txt("ekg_signal.txt")

    print("Minimum:", signal_min(values))
    print("Maximum:", signal_max(values))
    print("Average:", signal_avg(values))

    plot_signal(values)