from build.lib.stochastic_models.gbm import GeometricBrownianMotion
from statistics_utils import calculate_statistics, display_statistics, plot_simulation

# Simulate using GBM
gbm = GeometricBrownianMotion(mu=0.1, sigma=0.2, s0=100, T=1, n=1000, paths=1000)
time, simulations = gbm.simulate()

# Use the initial value (s0) as the actual value for P_LEVEL
initial_value = 100

# Calculate statistics
stats_df = calculate_statistics(simulations, initial_value)


# Display the statistics
display_statistics(stats_df, time)

#Plots the simulated paths
plot_simulation(time, simulations)
