# plot.py

# author: Neil Baker

### IMPORTS ###
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

import config as c

### FUNCTIONS ###
def plot_xva_single(bodies):
    """
    Plots all quantities x(t), v(t) and a(t) on a single plot for each body
    """
    # create directory if one does not exist
    directory_name = f"Plot_xva_Single--N={c.N}, Tmax={c.Tmax}"
    if os.path.exists(directory_name) == False:
        os.mkdir(directory_name)

    # get time list
    t_list = np.linspace(0, c.Tmax, c.t_num+1)

    # check dimension
    if c.dim == 1:
        # individual acceleration/position/velocity plots
        for i, body in enumerate(bodies):
            # initialize figure
            fig, ax = plt.subplots()
            # get data in a single list
            x_list = body.x.flatten()
            v_list = body.v.flatten()
            a_list = body.a.flatten()
            # plot parameters
            ax.set_title = f"x(t), v(t), a(t), m={body.m}"
            #ax.grid()
            ax.legend(["x(t)", "v(t)", "a(t)"])
            ax.set_xlabel = "time (s)"
            ax.set_ylabel("x(t), v(t), a(t) (m, m/s, m/s^2)")
            # plot
            ax.plot(t_list, x_list, color="springgreen")
            ax.plot(t_list, v_list, color="gold")
            ax.plot(t_list, a_list, color="salmon")
            # save and clean up
            plt.savefig(f"{directory_name}/Body{i} m={body.m}.png")
            plt.close()

    elif c.dim == 2:
        pass
    elif c.dim == 3:
        pass

def plot_xva_all(bodies):
    """
    Plots single quantities x(t), v(t) or a(t) for all bodies on a single plot
    """

def plot_individual(bodies):
    """
    Plots x(t), v(t), a(t) individually for each body
    """

    # create directory if one does not exist
    directory_name = f"Plot_Individual--N={c.N}, Tmax={c.Tmax}"
    if os.path.exists(directory_name) == False:
        os.mkdir(directory_name)

    # get time list
    t_list = np.linspace(0, c.Tmax, c.t_num+1)

    # check dimension
    if c.dim == 1:
        # individual acceleration/position/velocity plots
        for i, body in enumerate(bodies):
            # get data in a single list
            x_list = body.x.flatten()
            v_list = body.v.flatten()
            a_list = body.a.flatten()
            
            # plot x(t)
            plt.title = f"x(t), m={body.m}"
            plt.grid()
            # plt.style.use("dark_background")
            plt.xlabel = "time (s)"
            plt.ylabel("x(t) (m)")
            plt.plot(t_list, x_list, color="springgreen")
            plt.savefig(f"{directory_name}/Body{i} x(t) m={body.m}.png")
            plt.close()

            # plot v(t)
            plt.title = f"x(t), m={body.m}"
            plt.grid()
            # plt.style.use("dark_background")
            plt.xlabel = "time (s)"
            plt.ylabel("v(t) (m)")
            plt.plot(t_list, v_list, color="gold")
            plt.savefig(f"{directory_name}/Body{i} v(t) m={body.m}.png")
            plt.close()

            # plot a(t)
            plt.title = f"x(t), m={body.m}"
            plt.grid()
            # plt.style.use("dark_background")
            plt.xlabel = "time (s)"
            plt.ylabel("a(t) (m)")
            plt.plot(t_list, a_list, color="salmon")
            plt.savefig(f"{directory_name}/Body{i} a(t) m={body.m}.png")
            plt.close()

    elif c.dim == 2:
        pass
    elif c.dim == 3:
        pass

