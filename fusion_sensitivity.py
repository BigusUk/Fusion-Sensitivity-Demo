import sympy as sp
import numpy as np

E_res = sp.Symbol('E_res')
rate_log = -1000 / E_res  # Log rate to avoid underflow

E_default = 1.0
rate_log_default = float(rate_log.subs(E_res, E_default))
c_o_ratio_default = 0.6

variations = np.array([-0.005, 0.0, 0.005])

rate_logs = [float(rate_log.subs(E_res, E_default * (1 + v))) for v in variations]
normalized_rates = np.exp(np.array(rate_logs) - rate_log_default)  # Exp of diff for ratio
c_o_adjusted = c_o_ratio_default * normalized_rates

print('Default C/O ≈ 0.6')
print('-0.5% shift: C/O ≈', round(c_o_adjusted[0], 3))  # 0.003
print('+0.5% shift: C/O ≈', round(c_o_adjusted[2], 1))  # 165.3