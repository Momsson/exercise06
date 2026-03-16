import matplotlib.pyplot as plt


def load_signal_from_txt(path):
    """
    Načte hodnoty signálu z txt souboru.
    Každý řádek obsahuje jednu číselnou hodnotu.
    Vrací list[float].
    """
    values = []

    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                values.append(float(line))

    return values


def signal_min(values):
    """Vrátí minimum signálu."""
    return min(values)


def signal_max(values):
    """Vrátí maximum signálu."""
    return max(values)


def signal_avg(values):
    """Vrátí průměr signálu."""
    return sum(values) / len(values)


def plot_signal(values):
    """Vykreslí graf signálu."""
    plt.plot(values)
    plt.title("Signal Plot")
    plt.xlabel("Sample")
    plt.ylabel("Value")
    plt.show()


if __name__ == "__main__":
    # Testovací blok

    values = load_signal_from_txt("ekg_signal.txt")

    print("Minimum:", signal_min(values))
    print("Maximum:", signal_max(values))
    print("Average:", signal_avg(values))

    plot_signal(values)