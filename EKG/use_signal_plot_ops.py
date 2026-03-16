import signal_plot_ops

values = signal_plot_ops.load_signal_from_txt("ekg_signal.txt")

avg = signal_plot_ops.signal_avg(values)
print("Average value:", avg)

signal_plot_ops.plot_signal(values)