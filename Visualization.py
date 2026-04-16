#O2 dissociation
import matplotlib.pyplot as plt

# Function to read COPASI txt data
def read_data(filename):
    x = []
    y = []
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue  # skip header
            parts = line.strip().split()
            if len(parts) < 2:
                continue
            x.append(float(parts[0]))  # O2
            y.append(float(parts[1]))  # Sat_O2
    return x, y


# File paths (use raw string to avoid path errors)
files = {
    "CO = 0": r"C:\Users\彭成远\Desktop\miniprojects_simulation_data\O2_scan_CO_0.txt",
    "CO = 0.1": r"C:\Users\彭成远\Desktop\miniprojects_simulation_data\O2_scan_CO_0.1.txt",
    "CO = 0.5": r"C:\Users\彭成远\Desktop\miniprojects_simulation_data\O2_scan_CO_0.5.txt",
    "CO = 1": r"C:\Users\彭成远\Desktop\miniprojects_simulation_data\O2_scan_CO_1.txt",
    "CO = 2": r"C:\Users\彭成远\Desktop\miniprojects_simulation_data\O2_scan_CO_2.txt",
    "CO = 5": r"C:\Users\彭成远\Desktop\miniprojects_simulation_data\O2_scan_CO_5.txt",
    "CO = 10": r"C:\Users\彭成远\Desktop\miniprojects_simulation_data\O2_scan_CO_10.txt",
}


# Plot
plt.figure(figsize=(8, 6))

for label, filepath in files.items():
    O2, Sat = read_data(filepath)
    plt.plot(O2, Sat, label=label)


# Labels and title
plt.xlabel("O2 concentration (mol/L)")
plt.ylabel("O2 Saturation (Sat_O2)")
plt.title("Effect of CO on Hemoglobin Oxygen Dissociation Curve")

# Legend
plt.legend(title="CO concentration")

# Grid
plt.grid()

# Show plot
plt.show()


#CO Poisoning
import matplotlib.pyplot as plt

# Read COPASI time-course data
def read_data(filename):
    time = []
    sat_o2 = []

    with open(filename, "r") as f:
        for line in f:
            if line.startswith("#"):
                continue

            parts = line.strip().split()
            if len(parts) < 11:
                continue

            time.append(float(parts[0]))        # Time
            sat_o2.append(float(parts[10]))     # Values[Sat_O2]

    return time, sat_o2


# File paths
files = {
    "CO = 2": r"C:\Users\彭成远\Desktop\Final_data\CO_poisoning\CO_poisoning_CO_2.txt",
    "CO = 5": r"C:\Users\彭成远\Desktop\Final_data\CO_poisoning\CO_poisoning_CO_5.txt",
    "CO = 10": r"C:\Users\彭成远\Desktop\Final_data\CO_poisoning\CO_poisoning_CO_10.txt",
}

# Plot
plt.figure(figsize=(8, 6), dpi=150)

for label, filepath in files.items():
    time, sat_o2 = read_data(filepath)
    plt.plot(time, sat_o2, label=label, linewidth=2)

plt.xlabel("Time (s)")
plt.ylabel("Oxygen Saturation (Sat_O2)")
plt.title("Time-dependent Effect of CO Concentration on Hemoglobin Oxygen Saturation")
plt.axvline(x=5, linestyle="--", color="gray", alpha=0.7)
plt.xlim(0, 30)
plt.ylim(0, 1)
plt.legend(title="CO concentration")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

#Hb decay
import matplotlib.pyplot as plt

# Read COPASI time-course data
def read_data(filename):
    time = []
    total_hb = []
    o2_content = []

    with open(filename, "r") as f:
        for line in f:
            if line.startswith("#"):
                continue

            parts = line.strip().split()
            if len(parts) < 12:
                continue

            time.append(float(parts[0]))         # Time
            total_hb.append(float(parts[9]))     # Values[Total_Hb]
            o2_content.append(float(parts[11]))  # Values[O2_content]

    return time, total_hb, o2_content


# File paths
files = {
    "k = 0": r"C:\Users\彭成远\Desktop\Final_data\Hb_decay\Final_model_CO_O2_Hb_Decay_0.txt",
    "k = 0.005": r"C:\Users\彭成远\Desktop\Final_data\Hb_decay\Final_model_CO_O2_Hb_Decay_0.005.txt",
    "k = 0.01": r"C:\Users\彭成远\Desktop\Final_data\Hb_decay\Final_model_CO_O2_Hb_Decay_0.01.txt",
}


# Plot 1: Total Hb vs time
plt.figure(figsize=(8, 6), dpi=150)

for label, filepath in files.items():
    time, total_hb, o2_content = read_data(filepath)
    plt.plot(time, total_hb, label=label, linewidth=2)

plt.xlabel("Time (s)")
plt.ylabel("Total hemoglobin")
plt.title("Effect of Hemoglobin Decay on Total Hemoglobin")
plt.xlim(0, 30)
plt.legend(title="Decay rate")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()


# Plot 2: O2 content vs time
plt.figure(figsize=(8, 6), dpi=150)

for label, filepath in files.items():
    time, total_hb, o2_content = read_data(filepath)
    plt.plot(time, o2_content, label=label, linewidth=2)

plt.xlabel("Time (s)")
plt.ylabel("O2 content")
plt.title("Effect of Hemoglobin Decay on Oxygen Content")
plt.xlim(0, 30)
plt.legend(title="Decay rate")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()