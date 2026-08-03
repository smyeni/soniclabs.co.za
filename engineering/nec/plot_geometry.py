import matplotlib.pyplot as plt
from parse_nec import NECModel

# Half-wave dipole at 30 MHz

model = NECModel("dipole_05.nec")

plt.figure(figsize=(6,8))

for wire in model.wires:
	plt.plot( [wire.x1, wire.x2],	[wire.z1, wire.z2], linewidth=3, color="blue" )
	plt.scatter( [wire.x1, wire.x2], [wire.z1, wire.z2], color="red" )

plt.title("Sonic Labs RF\nNEC Geometry")

plt.xlabel("X [m]")
plt.ylabel("Z [m]")

plt.grid(True)

plt.axis("equal")

plt.show()
