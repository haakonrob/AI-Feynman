import os
import aifeynman

# Testing
for fname in os.listdir('ma_data/'):
    print(f"Running aifeynman on {fname}")
    aifeynman.run_aifeynman("./ma_data/", 
                            fname, 
                            BF_try_time=60,  
                            BF_ops_file_type= "14ops.txt",
                            BF_gen_sym_try_time=600, 
                            polyfit_deg=4, 
                            NN_epochs=500, 
                            cuda=False
)

# # Testing
# aifeynman.get_demos("example_data") # Download examples from server
# aifeynman.run_aifeynman("./example_data/", "example1.txt", 0.1, "14ops.txt", polyfit_deg=1, NN_epochs=1, cuda=False)
