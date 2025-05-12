#  Copyright (c) 2019-2020 by the Cabana authors
#   All rights reserved.

#   This file is part of the ScheduleFlow package. ScheduleFlow is
#   distributed under a BSD 3-clause license. For details see the
#   LICENSE file in the top-level directory.

#   SPDX-License-Identifier: BSD-3-Clause


############################################
###   NOTED: MY TESTING FILE   ###
###  all original code came from run_simple_example.py ###
############################################

import ScheduleFlow
import sys
import numpy as np


def run_scenario(num_procssing_units, job_list):
    simulator = ScheduleFlow.Simulator(check_correctness=True,
                                       generate_gif=True,
                                       output_file_handler=sys.stdout)
    '''sch = ScheduleFlow.BatchScheduler(
        ScheduleFlow.System(num_processing_units))
    simulator.create_scenario("test_batch", sch, job_list=job_list)
    simulator.run()'''

    sch = ScheduleFlow.OnlineScheduler(
        ScheduleFlow.System(num_processing_units))
    simulator.create_scenario("test_online", sch, job_list=job_list)
    simulator.run()


if __name__ == '__main__':
    num_processing_units = 10 #edit
    job_list = set()
    # create the list of applications
    for i in range(10):
        execution_time = np.random.randint(11, 100) #execution time - 0-100
        #try to understand request time
        #processing units - amount of work per job
        #idk submission time either
        #idea #1 0 make num_processing_units of a job a function based on execution time, parabola style
            #this idea felt kind of dumb, shouldnt manipulate processing units of a job, but num_processing_units
        #idea #2 - num_processing units has to be an input per job
            #make current num_processing_units the max units of a job, and manipulate how many units a job actually has as a function of when it runs ig
            #idea 2.1 - find where jobs are generated in the code, like how they are built in the schedulers
                #in these functions, there should prob be a get_num_processing_units
                #use that and modify the code based on when the job is scheduled(x axis? jobs probably all schedule back to back)
                    #2.1.1 - if jobs are scheduling back to back automatically, keep a running total to work with
                #manipulate that number based on the current "time" in the program to get the desired curve
            #side note - gonna probably need to learn how batch scheduling and online scheduling work in this context
        request_time = execution_time + int(i / 2) * 10
        #processing_units = -((1/31) * execution_time) ** 2 + 10
        processing_units = np.random.randint(
            1, num_processing_units + 1)
        submission_time = 0
        job_list.add(ScheduleFlow.Application(
            processing_units,
            submission_time,
            execution_time,
            [request_time]))
    # add a job that request less time than required for its first run
    job_list.add(ScheduleFlow.Application(4, 0, 100, [90, 135]))
    job_list.add(ScheduleFlow.Application(np.random.randint(9, 11), 0,
                                          100, [90, 135]))
    job_list.add(ScheduleFlow.Application(np.random.randint(9, 11), 0,
                                          100, [90, 135]))
    job_list.add(ScheduleFlow.Application(np.random.randint(9, 11), 0,
                                          100, [90, 135]))
    job_list.add(ScheduleFlow.Application(np.random.randint(9, 11), 0,
                                          100, [90, 135]))
    job_list.add(ScheduleFlow.Application(np.random.randint(9, 11), 0,
                                          100, [90, 135]))

    print("Scenario : makespan : utilization : average_job_utilization : "
          "average_job_response_time : average_job_stretch : "
          "average_job_wait_time : failures")

    run_scenario(num_processing_units, job_list)
