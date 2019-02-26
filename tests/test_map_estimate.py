import numpy as np


from ptfidf.train.inference import map_estimate


def test_map_estimate_easy():
    """
    check trivial example without matches.

    pi is population average,
    s stays at prior mean.
    """
    n = np.array([1, 1])
    k = np.array([0, 1])

    weights = np.array([
        [7, 3],
        [99, 1],
    ])

    prior_mean = -1.

    expected_pi = np.array([.3, .01])
    expected_s = np.exp(prior_mean) * np.ones_like(expected_pi)

    pi, s = map_estimate(n, k, weights, prior_mean, 1.)

    assert np.allclose(pi, expected_pi), pi
    assert np.allclose(s, expected_s), s