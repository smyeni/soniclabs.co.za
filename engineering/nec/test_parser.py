from parse_nec import NECModel

model = NECModel("dipole_01.nec")

print()

print("Model:", model.filename)

print()

print("Number of wires:", len(model.wires))

print()

for wire in model.wires:
    print(wire)

print("Excitation:\n", model.excitation)