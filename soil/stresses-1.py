import numpy as np
import matplotlib.pyplot as plt
from edafos.soil import SoilProfile

caseA = SoilProfile(unit_system='English', water_table=10)
caseA.add_layer(soil_type='cohesionless', height=16, tuw=90)

z = np.arange(0,17,1)
t = []; p = []; s = [];
for i in z:
   total, pore, eff = caseA.calculate_stress(i, kind='all')
   t.append(total.magnitude)
   p.append(pore.magnitude)
   s.append(eff.magnitude)
plt.plot(p, z, label="Pore Water Pressure")
plt.plot(t, z, label="Total Stress")
plt.plot(s, z, label="Effective Stress")
plt.title("Stress Distribution for Case A")
plt.xlabel("(kip/ft2)")
plt.ylabel("Depth (ft)")
plt.gca().invert_yaxis()
plt.grid()
plt.legend()
plt.show()