#!/usr/bin/env python3

class Excitation:

    def __init__(self, 
                 exc_type, 
                 exc_tag,
                 segment_id,
                 source_real,
                 source_imag):
        
        self.exc_type = exc_type
        self.exc_tag = exc_tag
        self.segment_id = segment_id
        self.source_real = source_real
        self.source_imag = source_imag

    def __str__(self):
        return f"EX card on wire tag {self.exc_tag} segment {self.segment_id} and voltage {self.source_real} +j {self.source_imag} V"


class Wire:

    def __init__(self, 
                 tag, 
                 num_segments,
                 x1, y1, z1,
                 x2, y2, z2,
                 radius):

        self.tag = tag
        self.num_segments = num_segments

        self.x1 = x1
        self.y1 = y1
        self.z1 = z1

        self.x2 = x2
        self.y2 = y2
        self.z2 = z2

        self.radius = radius


class NECModel:

    def __init__(self, filename):

        self.filename = filename

        self.wires = []

        self.read()


    def read(self):

        with open(self.filename) as f:

            for line in f:

                line = line.strip()

                if not line:
                    continue

                fields = line.split()

                card = fields[0]

                if card == "GW":

                    wire = Wire(
                        int(fields[1]),
                        int(fields[2]),

                        float(fields[3]),
                        float(fields[4]),
                        float(fields[5]),

                        float(fields[6]),
                        float(fields[7]),
                        float(fields[8]),

                        float(fields[9])
                    )

                    self.wires.append(wire)

                elif card == "EX":
                    self.excitation = Excitation(
                        int(fields[1]),
                        int(fields[2]),
                        int(fields[3]),
                        float(fields[5]),
                        float(fields[6])
                    )
