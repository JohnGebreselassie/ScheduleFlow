from ScheduleFlow import *
import numpy as np

#define power system
def energy_profile(timestamp):
    '''
    if timestamp == 30:
        return 30  
    else:
        return 50   
      
    '''
    #New sine function:
    x = timestamp
    a = 20
    k = (np.pi)/720
    c = (3 * (np.pi)/2) + (2*(np.pi))
    d = 30

    power = (a*(np.sin((k*x)+c)))+30
    if power > 50:
        return 50
    return power
    

# Define system with 50 nodes
#def __init__(self, total_nodes)
sys = System(50, availability_fn=energy_profile)

# Define scheduler
#def __init__(self, system, batch_size=100, logger=None)
sch = OnlineScheduler(sys)

# Create jobs
jobs = [
#def __init__(self, nodes, submission_time, walltime, requested_walltimes, resubmit_factor=-1)
    Application(9, 0, 30, [30]),
    Application(9, 0, 30, [30]),
    Application(10, 720, 30, [30]),
    Application(10, 720, 30, [30]),
    Application(10, 720, 30, [30]),
]

# Run simulation
#def __init__(self, loops=1, generate_gif=False, check_correctness=False,output_file_handler=None)
sim = Simulator(check_correctness=True,generate_gif=True)
sim.create_scenario("my_scenario", sch, jobs)
sim.run()
