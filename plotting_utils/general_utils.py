import os
import matplotlib.pyplot as plt


def save_fig(fig, save_loc: str = None, dpi: int = 600) -> None:
    """
    Save figure
    :param fig: figure
    :param save_loc: location to save the figure
    :param dpi: dpi
    :return: None
    """

    # If save location doesn't exist, create it
    if not os.path.exists(os.path.dirname(save_loc)):
        os.makedirs(os.path.dirname(save_loc))

    # Save the figure
    fig.savefig(save_loc, dpi=dpi)
    plt.close("all")


def set_axis_infos(
    ax,
    xlabel: str = None,
    ylabel: int = None,
    xlim=None,
    ylim=None,
    legend=None,
    title: str = None,
    xticks=None,
    yticks=None,
) -> None:
    """
    Set axis information
    :param ax: axis
    :param xlabel: x-axis label
    :param ylabel: y-axis label
    :param xlim: x-axis limits
    :param ylim: y-axis limits
    :param legend: legend
    :param title_str: title
    :param xticks: x-axis ticks
    :param yticks: y-axis ticks
    :param xlabel_size: x-axis label size
    :param ylabel_size: y-axis label size
    :param title_size: title size
    :param ticks_size: ticks size
    :param legend_size: legend size
    :param legend_loc: legend location
    :return: None
    """

    if xlabel:
        ax.set_xlabel(xlabel)
    if xlabel_size:
        ax.xaxis.label.set_size(xlabel_size)
    if ylabel:
        ax.set_ylabel(ylabel)
    if ylabel_size:
        ax.yaxis.label.set_size(ylabel_size)
    if xlim:
        ax.set_xlim(xlim[0], xlim[1])
    if ylim:
        ax.set_ylim(ylim[0], ylim[1])
    if xticks:
        ax.set_xticks(xticks)
    if yticks:
        ax.set_yticks(yticks)
    if ticks_size:
        ax.tick_params(axis="both", which="major", labelsize=ticks_size)
    if legend:
        ax.legend(legend)
    if title:
        ax.set_title(title)
