import cirq


def make_bell_state(q0, q1, index=(0, 0)):
    if index[0]:
        yield cirq.X(q0)
    if index[1]:
        yield cirq.X(q1)
    yield cirq.H(q0)
    yield cirq.CNOT(q0, q1)


def bell_measurement(c, q0, q1):
    c.append([cirq.CNOT(q0, q1), cirq.H(q0)])
    c.append(cirq.measure(q0, q1))
