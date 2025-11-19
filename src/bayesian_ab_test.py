
import numpy as np
from scipy.stats import beta

def posterior(alpha, beta_param, successes, trials):
    return alpha + successes, beta_param + trials - successes

def compare(a_s, a_n, b_s, b_n, alpha=1, beta_param=1, samples=200000):
    a_alpha, a_beta = posterior(alpha, beta_param, a_s, a_n)
    b_alpha, b_beta = posterior(alpha, beta_param, b_s, b_n)
    a_draws = np.random.beta(a_alpha, a_beta, size=samples)
    b_draws = np.random.beta(b_alpha, b_beta, size=samples)
    prob_b_better = (b_draws > a_draws).mean()
    lift = (b_draws - a_draws) / np.maximum(1e-9, a_draws)
    return {
        "a_mean": float(a_draws.mean()),
        "b_mean": float(b_draws.mean()),
        "prob_b_better": float(prob_b_better),
        "lift_mean": float(lift.mean()),
        "a_ci": np.quantile(a_draws, [0.025, 0.975]).tolist(),
        "b_ci": np.quantile(b_draws, [0.025, 0.975]).tolist(),
    }
