import c4d


def chuaI():
	object_name = "Chua I Attractor"

	# Growth Parameters
	N = 50000
	delta = 0.01
	factor = 5

	# Attractor Parameters
	x0 = 1.0  # Initial x coordinate
	y0 = 1.0  # Initial y coordinate
	z0 = 1.0  # Initial z coordinate
	a = 15.6
	b = 1.0
	c = 25.58
	d = -1.0
	e = 0.0

	# Create fresh spline object
	spline = c4d.SplineObject(N, c4d.SPLINETYPE_LINEAR)
	spline.SetName(object_name)

	# Initialize coordinates
	x = x0
	y = y0
	z = z0

	for i in range(N):
		h = e * x + (d + e) * (abs(x + 1) - abs(x - 1))
		dx = a * (y - x - h)
		dy = b * (x - y + z)
		dz = y * -c

		x = x + delta * dx
		y = y + delta * dy
		z = z + delta * dz

		spline.SetPoint(i, c4d.Vector(x * factor, y * factor, z * factor))

	return spline


# Main function
def main():
	spline = chuaI()
	doc.InsertObject(spline)
	doc.SetActiveObject(spline)
	c4d.EventAdd()
