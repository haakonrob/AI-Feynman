import aifeynman

# aifeynman.get_demos("example_data") # Download examples from server
# Testing
aifeynman.run_aifeynman("./example_data/", "example1.txt", 60, "14ops.txt", polyfit_deg=3, NN_epochs=500, cuda=False)
# aifeynman.run_aifeynman("./example_data/", "example1.txt", 0.1, "14ops.txt", polyfit_deg=1, NN_epochs=1, cuda=False)