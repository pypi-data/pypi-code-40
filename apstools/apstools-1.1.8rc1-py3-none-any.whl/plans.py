"""
Plans that might be useful at the APS when using BlueSky

.. autosummary::
   
   ~addDeviceDataAsStream
   ~execute_command_list
   ~get_command_list
   ~nscan
   ~parse_Excel_command_file
   ~parse_text_command_file
   ~register_command_handler
   ~run_blocker_in_plan
   ~run_command_file
   ~snapshot
   ~sscan_1D
   ~summarize_command_file
   ~TuneAxis
   ~tune_axes

"""

#-----------------------------------------------------------------------------
# :author:    Pete R. Jemian
# :email:     jemian@anl.gov
# :copyright: (c) 2017-2019, UChicago Argonne, LLC
#
# Distributed under the terms of the Creative Commons Attribution 4.0 International Public License.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------

from collections import OrderedDict
import datetime
import logging
import numpy as np
import os
import pyRestTable
import sys
import time

from bluesky import preprocessors as bpp
from bluesky import plan_stubs as bps
from bluesky.callbacks.fitting import PeakStats
from ophyd import Device, Component, Signal, DeviceStatus, EpicsSignal
from ophyd.status import Status

from . import utils as APS_utils


logger = logging.getLogger(__name__).addHandler(logging.NullHandler())


class CommandFileReadError(IOError): ...


def addDeviceDataAsStream(devices, label):
    """
    plan: add an ophyd Device as an additional document stream
    
    Use this within a custom plan, such as this example::

        from apstools.plans import addDeviceStream
        ...
        yield from bps.open_run()
        # ...
        yield from addDeviceDataAsStream(prescanDeviceList, "metadata_prescan")
        # ...
        yield from custom_scan_procedure()
        # ...
        yield from addDeviceDataAsStream(postscanDeviceList, "metadata_postscan")
        # ...
        yield from bps.close_run()

    """
    yield from bps.create(name=label)
    if not isinstance(devices, list):     # just in case...
        devices = [devices]
    for d in devices:
        yield from bps.read(d)
        yield from bps.save()


def execute_command_list(filename, commands, md={}):
    """
    plan: execute the command list

    The command list is a tuple described below.

    * Only recognized commands will be executed.
    * Unrecognized commands will be reported as comments.
    
    See example implementation with APS USAXS instrument:
    https://github.com/APS-USAXS/ipython-usaxs/blob/5db882c47d935c593968f1e2144d35bec7d0181e/profile_bluesky/startup/50-plans.py#L381-L469

    PARAMETERS

    filename : str
        Name of input text file.  Can be relative or absolute path,
        such as "actions.txt", "../sample.txt", or
        "/path/to/overnight.txt".
    commands : list[command]
        List of command tuples for use in ``execute_command_list()``

    where

    command : tuple
        (action, OrderedDict, line_number, raw_command)
    action: str
        names a known action to be handled
    parameters: list
        List of parameters for the action.
        The list is empty of there are no values
    line_number: int
        line number (1-based) from the input text file
    raw_command: obj (str or list(str)
        contents from input file, such as:
        ``SAXS 0 0 0 blank``

    SEE ALSO

    .. autosummary::
    
        ~execute_command_list
        ~register_command_handler
        ~run_command_file
        ~summarize_command_file
        ~parse_Excel_command_file
        ~parse_text_command_file
    """
    full_filename = os.path.abspath(filename)

    if len(commands) == 0:
        yield from bps.null()
        return

    text = f"Command file: {filename}\n"
    text += str(APS_utils.command_list_as_table(commands))
    print(text)

    for command in commands:
        action, args, i, raw_command = command
        print(f"file line {i}: {raw_command}")

        _md = {}
        _md["full_filename"] = full_filename
        _md["filename"] = filename
        _md["line_number"] = i
        _md["action"] = action
        _md["parameters"] = args    # args is shorter than parameters, means the same thing here

        _md.update(md or {})      # overlay with user-supplied metadata

        action = action.lower()
        if action == "tune_optics":
            # example: yield from tune_optics(md=_md)
            emsg = "This is an example.  action={raw_command}."
            emsg += "  Must define your own execute_command_list() function"
            logger.warn(emsg)
            yield from bps.null()

        else:
            print(f"no handling for line {i}: {raw_command}")


def get_command_list(filename):
    """
    return command list from either text or Excel file

    SEE ALSO

    .. autosummary::
    
        ~execute_command_list
        ~get_command_list
        ~register_command_handler
        ~run_command_file
        ~summarize_command_file
        ~parse_Excel_command_file
        ~parse_text_command_file

    """
    full_filename = os.path.abspath(filename)
    if not os.path.exists(full_filename):
        raise IOError(f"file not found: {filename}")
    try:
        commands = parse_Excel_command_file(filename)
    except APS_utils.ExcelReadError:
        try:
            commands = parse_text_command_file(filename)
        except ValueError as exc:
            emsg = f"could not read {filename} as command list file: {exc}"
            raise CommandFileReadError(emsg)
    return commands


def run_blocker_in_plan(blocker, *args, _poll_s_=0.01, _timeout_s_=None, **kwargs):
    """
    plan: run blocking function ``blocker_(*args, **kwargs)`` from a Bluesky plan

    .. warning: This plan is deprecated.  It will be removed by 2019-12-31.

    PARAMETERS

    blocker : func
        function object to be called in a Bluesky plan

    _poll_s_ : float
        sleep interval in loop while waiting for completion 
        (default: 0.01)

    _timeout_s_ : float
        maximum time for completion 
        (default: `None` which means no timeout)
    
    Example: use ``time.sleep`` as blocking function::
    
        RE(run_blocker_in_plan(time.sleep, 2.14))

    Example: in a plan, use ``time.sleep`` as blocking function::

        def my_sleep(t=1.0):
            yield from run_blocker_in_plan(time.sleep, t)

        RE(my_sleep())

    """
    logger.warning("This plan is deprecated.  It will be removed by 2019-12-31.")
    status = Status()
    
    @APS_utils.run_in_thread
    def _internal(blocking_function, *args, **kwargs):
        blocking_function(*args, **kwargs)
        status._finished(success=True, done=True)
    
    if _timeout_s_ is not None:
        t_expire = time.time() + _timeout_s_

    # FIXME: how to keep this from running during summarize_plan()?
    _internal(blocker, *args, **kwargs)

    while not status.done:
        if _timeout_s_ is not None:
            if time.time() > t_expire:
                status._finished(success=False, done=True)
                break
        yield from bps.sleep(_poll_s_)
    return status


def nscan(detectors, *motor_sets, num=11, per_step=None, md=None):
    """
    Scan over ``n`` variables moved together, each in equally spaced steps.

    PARAMETERS

    detectors : list
        list of 'readable' objects
    motor_sets : list
        sequence of one or more groups of: motor, start, finish
    motor : object
        any 'settable' object (motor, temp controller, etc.)
    start : float
        starting position of motor
    finish : float
        ending position of motor
    num : int
        number of steps (default = 11)
    per_step : callable, optional
        hook for customizing action of inner loop (messages per step)
        Expected signature: ``f(detectors, step_cache, pos_cache)``
    md : dict, optional
        metadata
    
    See the `nscan()` example in a Jupyter notebook:
    https://github.com/BCDA-APS/apstools/blob/master/docs/source/resources/demo_nscan.ipynb
    """
    def take_n_at_a_time(args, n=2):
        yield from zip(*[iter(args)]*n)
        
    if len(motor_sets) < 3:
        raise ValueError("must provide at least one movable")
    if len(motor_sets) % 3 > 0:
        raise ValueError("must provide sets of movable, start, finish")

    motors = OrderedDict()
    for m, s, f in take_n_at_a_time(motor_sets, n=3):
        if not isinstance(s, (int, float)):
            msg = "start={} ({}): is not a number".format(s, type(s))
            raise ValueError(msg)
        if not isinstance(f, (int, float)):
            msg = "finish={} ({}): is not a number".format(f, type(f))
            raise ValueError(msg)
        motors[m.name] = dict(motor=m, start=s, finish=f, 
                              steps=np.linspace(start=s, stop=f, num=num))

    _md = {'detectors': [det.name for det in detectors],
           'motors': [m for m in motors.keys()],
           'num_points': num,
           'num_intervals': num - 1,
           'plan_args': {'detectors': list(map(repr, detectors)), 
                         'num': num,
                         'motors': repr(motor_sets),
                         'per_step': repr(per_step)},
           'plan_name': 'nscan',
           'plan_pattern': 'linspace',
           'hints': {},
           'iso8601': datetime.datetime.now(),
           }
    _md.update(md or {})

    try:
        m = list(motors.keys())[0]
        dimensions = [(motors[m]["motor"].hints['fields'], 'primary')]
    except (AttributeError, KeyError):
        pass
    else:
        _md['hints'].setdefault('dimensions', dimensions)

    if per_step is None:
        per_step = bps.one_nd_step

    @bpp.stage_decorator(list(detectors) 
                         + [m["motor"] for m in motors.values()])
    @bpp.run_decorator(md=_md)
    def inner_scan():
        for step in range(num):
            step_cache, pos_cache = {}, {}
            for m in motors.values():
                next_pos = m["steps"][step]
                m = m["motor"]
                pos_cache[m] = m.read()[m.name]["value"]
                step_cache[m] = next_pos
            yield from per_step(detectors, step_cache, pos_cache)

    return (yield from inner_scan())


def parse_Excel_command_file(filename):
    """
    parse an Excel spreadsheet with commands, return as command list

    TEXT view of spreadsheet (Excel file line numbers shown)::

        [1] List of sample scans to be run
        [2]
        [3]
        [4] scan    sx  sy  thickness   sample name
        [5] FlyScan 0   0   0   blank
        [6] FlyScan 5   2   0   blank

    PARAMETERS

    filename : str
        Name of input Excel spreadsheet file.  Can be relative or absolute path,
        such as "actions.xslx", "../sample.xslx", or
        "/path/to/overnight.xslx".

    RETURNS

    list of commands : list[command]
        List of command tuples for use in ``execute_command_list()``

    RAISES

    FileNotFoundError
        if file cannot be found

    SEE ALSO

    .. autosummary::
    
        ~get_command_list
        ~register_command_handler
        ~run_command_file
        ~summarize_command_file
        ~parse_text_command_file


    """
    full_filename = os.path.abspath(filename)
    assert os.path.exists(full_filename)
    xl = APS_utils.ExcelDatabaseFileGeneric(full_filename)

    commands = []

    if len(xl.db) > 0:
        for i, row in enumerate(xl.db.values()):
            action, *values = list(row.values())

            # trim off any None values from end
            while len(values) > 0:
                if values[-1] is not None:
                    break
                values = values[:-1]

            commands.append((action, values, i+1, list(row.values())))

    return commands


def parse_text_command_file(filename):
    """
    parse a text file with commands, return as command list

    * The text file is interpreted line-by-line.
    * Blank lines are ignored.
    * A pound sign (#) marks the rest of that line as a comment.
    * All remaining lines are interpreted as commands with arguments.

    Example of text file (no line numbers shown)::

        #List of sample scans to be run
        # pound sign starts a comment (through end of line)

        # action  value
        mono_shutter open

        # action  x y width height
        uslits 0 0 0.4 1.2

        # action  sx  sy  thickness   sample name
        FlyScan 0   0   0   blank
        FlyScan 5   2   0   "empty container"

        # action  sx  sy  thickness   sample name
        SAXS 0 0 0 blank

        # action  value
        mono_shutter close

    PARAMETERS

    filename : str
        Name of input text file.  Can be relative or absolute path,
        such as "actions.txt", "../sample.txt", or
        "/path/to/overnight.txt".

    RETURNS

    list of commands : list[command]
        List of command tuples for use in ``execute_command_list()``

    RAISES

    FileNotFoundError
        if file cannot be found

    SEE ALSO

    .. autosummary::
    
        ~execute_command_list
        ~get_command_list
        ~register_command_handler
        ~run_command_file
        ~summarize_command_file
        ~parse_Excel_command_file

    """
    full_filename = os.path.abspath(filename)
    assert os.path.exists(full_filename)
    with open(full_filename, "r") as fp:
        buf = fp.readlines()

    commands = []
    for i, raw_command in enumerate(buf):
        row = raw_command.strip()
        if row == "" or row.startswith("#"):
            continue                    # comment or blank

        else:                           # command line
            action, *values = APS_utils.split_quoted_line(row)
            commands.append((action, values, i+1, raw_command.rstrip()))

    return commands


# internal use, allows redefinition of execute_command_list()
_COMMAND_HANDLER_ = execute_command_list


def register_command_handler(handler=None):
    """
    (re)define the function called to execute the command list

    PARAMETERS

    handler : obj
        Reference of the ``execute_command_list`` function
        to be used from :func:`~apstools.plans.run_command_file()`.
        If ``None`` or not provided, 
        will reset to :func:`~apstools.plans.execute_command_list()`,
        which is also the initial setting.

    SEE ALSO

    .. autosummary::
    
        ~execute_command_list
        ~get_command_list
        ~register_command_handler
        ~summarize_command_file
        ~parse_Excel_command_file
        ~parse_text_command_file

    """
    global _COMMAND_HANDLER_
    _COMMAND_HANDLER_ = handler or execute_command_list


def run_command_file(filename, md={}):
    """
    plan: execute a list of commands from a text or Excel file

    * Parse the file into a command list
    * yield the command list to the RunEngine (or other)

    SEE ALSO

    .. autosummary::
    
        ~execute_command_list
        ~get_command_list
        ~register_command_handler
        ~summarize_command_file
        ~parse_Excel_command_file
        ~parse_text_command_file

    """
    commands = get_command_list(filename)
    yield from _COMMAND_HANDLER_(filename, commands)


def snapshot(obj_list, stream="primary", md=None):
    """
    bluesky plan: record current values of list of ophyd signals

    PARAMETERS

    obj_list : list
        list of ophyd Signal or EpicsSignal objects
    stream : str
        document stream, default: "primary"
    md : dict
        metadata
    """
    from .__init__ import __version__
    from bluesky import __version__ as bluesky_version
    from databroker import __version__ as databroker_version
    from epics import __version__ as pyepics_version
    from ophyd import __version__ as ophyd_version
    import socket 
    import getpass 

    objects = []
    for obj in obj_list:
        # TODO: consider supporting Device objects
        if isinstance(obj, (Signal, EpicsSignal)) and obj.connected:
            objects.append(obj)
        else:
            if hasattr(obj, "pvname"):
                nm = obj.pvname
            else:
                nm = obj.name
            print(f"ignoring object: {nm}")
        
        if len(objects) == 0:
            raise ValueError("No signals to log.")

    hostname = socket.gethostname() or 'localhost' 
    username = getpass.getuser() or 'bluesky_user'

    # we want this metadata to appear
    _md = dict(
        plan_name = "snapshot",
        plan_description = "archive snapshot of ophyd Signals (usually EPICS PVs)",
        iso8601 = str(datetime.datetime.now()),     # human-readable
        hints = {},
        software_versions = dict(
            python = sys.version,
            PyEpics = pyepics_version,
            bluesky = bluesky_version,
            ophyd = ophyd_version,
            databroker = databroker_version,
            apstools = __version__,),
        hostname = hostname,
        username = username,
        login_id = f"{username}@{hostname}",
        )
    # caller may have given us additional metadata
    _md.update(md or {})

    def _snap(md=None):
        yield from bps.open_run(md)
        yield from bps.create(name=stream)
        for obj in objects:
            # passive observation: DO NOT TRIGGER, only read
            yield from bps.read(obj)
        yield from bps.save()
        yield from bps.close_run()

    return (yield from _snap(md=_md))


def summarize_command_file(filename):
    """
    print the command list from a text or Excel file

    SEE ALSO

    .. autosummary::
    
        ~execute_command_list
        ~get_command_list
        ~run_command_file
        ~parse_Excel_command_file
        ~parse_text_command_file

    """
    commands = get_command_list(filename)
    print(f"Command file: {filename}")
    print(APS_utils.command_list_as_table(commands))


def _get_sscan_data_objects(sscan):
    """
    prepare a dictionary of the "interesting" ophyd data objects for this sscan

    PARAMETERS

    sscan : Device
        one EPICS sscan record (instance of `apstools.synApps_ophyd.sscanRecord`)

    """
    scan_data_objects = OrderedDict()
    for part in (sscan.positioners, sscan.detectors):
        for chname in part.read_attrs:
            if not chname.endswith("_value"):
                continue
            obj = getattr(part, chname)
            key = obj.name.lstrip(sscan.name + "_")
            scan_data_objects[key] = obj
    return scan_data_objects


def sscan_1D(
        sscan, 
        poll_delay_s=0.001, 
        phase_timeout_s = 60.0,
        running_stream="primary", 
        final_array_stream=None, 
        device_settings_stream="settings", 
        md={}):
    """
    simple 1-D scan using EPICS synApps sscan record
    
    assumes the sscan record has already been setup properly for a scan

    PARAMETERS

    sscan : Device
        one EPICS sscan record (instance of `apstools.synApps_ophyd.sscanRecord`)
    running_stream : str or `None`
        (default: ``"primary"``)
        Name of document stream to write positioners and detectors data
        made available while the sscan is running.  This is typically 
        the scan data, row by row.
        If set to `None`, this stream will not be written.
    final_array_stream : str or `None`
        (default: ``None``)
        Name of document stream to write positioners and detectors data 
        posted *after* the sscan has ended.
        If set to `None`, this stream will not be written.
    device_settings_stream : str or `None`
        (default: ``"settings"``)
        Name of document stream to write *settings* of the sscan device.
        This is all the information returned by ``sscan.read()``.
        If set to `None`, this stream will not be written.
    poll_delay_s : float
        (default: 0.001 seconds)
        How long to sleep during each polling loop while collecting
        interim data values and waiting for sscan to complete.
        Must be a number between zero and 0.1 seconds.
    phase_timeout_s : float
        (default: 60 seconds)
        How long to wait after last update of the ``sscan.FAZE``.
        When scanning, we expect the scan phase to update regularly
        as positioners move and detectors are triggered.  If the scan
        hangs for some reason, this is a way to end the plan early.
        To cancel this feature, set it to ``None``.
    
    NOTE about the document stream names
    
    Make certain the names for the document streams are different from 
    each other.  If you make them all the same (such as ``primary``),
    you will have difficulty when reading your data later on.
    
    *Don't cross the streams!*
    
    EXAMPLE
    
    Assume that the chosen sscan record has already been setup.
    
        from apstools.devices import sscanDevice
        scans = sscanDevice(P, name="scans")
        
        from apstools.plans import sscan_1D
        RE(sscan_1D(scans.scan1), md=dict(purpose="demo"))

    """
    global new_data, inactive_deadline
    
    msg = f"poll_delay_s must be a number between 0 and 0.1, received {poll_delay_s}"
    assert 0 <= poll_delay_s <= 0.1, msg
    
    t0 = time.time()
    sscan_status = DeviceStatus(sscan.execute_scan)
    started = False
    new_data = False
    inactive_deadline = time.time()
    if phase_timeout_s is not None:
        inactive_deadline += phase_timeout_s
    
    def execute_cb(value, timestamp, **kwargs):
        """watch for sscan to complete"""
        if started and value in (0, "IDLE"):
            sscan_status._finished()
            sscan.execute_scan.unsubscribe_all()
            sscan.scan_phase.unsubscribe_all()
    
    def phase_cb(value, timestamp, **kwargs):
        """watch for new data"""
        global new_data, inactive_deadline
        if phase_timeout_s is not None:
            inactive_deadline = time.time() + phase_timeout_s
        if value in (15, "RECORD SCALAR DATA"):
            new_data = True            # set flag for main plan
    
    # acquire only the channels with non-empty configuration in EPICS
    sscan.select_channels()
    # pre-identify the configured channels
    sscan_data_objects = _get_sscan_data_objects(sscan)
    
    # watch for sscan to complete
    sscan.execute_scan.subscribe(execute_cb)
    # watch for new data to be read out
    sscan.scan_phase.subscribe(phase_cb)
    
    md["plan_name"] = "sscan_1D"

    yield from bps.open_run(md)               # start data collection
    yield from bps.mv(sscan.execute_scan, 1)   # start sscan
    started = True

    # collect and emit data, wait for sscan to end
    while not sscan_status.done or new_data:
        if new_data and running_stream is not None:
            yield from bps.create(running_stream)
            for _k, obj in sscan_data_objects.items():
                yield from bps.read(obj)
            yield from bps.save()
        new_data = False
        if phase_timeout_s is not None and time.time() > inactive_deadline:
            print(f"No change in sscan record for {phase_timeout_s} seconds.")
            print("ending plan early as unsuccessful")
            sscan_status._finished(success=False)
        yield from bps.sleep(poll_delay_s)

    # dump the complete data arrays
    if final_array_stream is not None:
        yield from bps.create(final_array_stream)
        # we have to search for the arrays since they have ``kind="omitted"``
        # (which means they do not get reported by the ``.read()`` method)
        for part in (sscan.positioners, sscan.detectors):
            for nm in part.read_attrs:
                if "." not in nm:
                    # TODO: write just the acquired data, not the FULL arrays!
                    yield from bps.read(getattr(part, nm).array)
        yield from bps.save()

    # dump the entire sscan record into another stream
    if device_settings_stream is not None:
        yield from bps.create(device_settings_stream)
        yield from bps.read(sscan)
        yield from bps.save()

    yield from bps.close_run()
    
    elapsed = time.time() - t0
    print(f"total time for sscan_1D: {elapsed} s")

    return sscan_status


class TuneAxis(object):
    """
    tune an axis with a signal
    
    This class provides a tuning object so that a Device or other entity
    may gain its own tuning process, keeping track of the particulars
    needed to tune this device again.  For example, one could add
    a tuner to a motor stage::
    
        motor = EpicsMotor("xxx:motor", "motor")
        motor.tuner = TuneAxis([det], motor)
    
    Then the ``motor`` could be tuned individually::
    
        RE(motor.tuner.tune(md={"activity": "tuning"}))
    
    or the :meth:`tune()` could be part of a plan with other steps.
    
    Example::
    
        tuner = TuneAxis([det], axis)
        live_table = LiveTable(["axis", "det"])
        RE(tuner.multi_pass_tune(width=2, num=9), live_table)
        RE(tuner.tune(width=0.05, num=9), live_table)
    
    Also see the jupyter notebook referenced here:
    :ref:`example_tuneaxis`.

    .. autosummary::
       
       ~tune
       ~multi_pass_tune
       ~peak_detected
    
    SEE ALSO

    .. autosummary::
       
       ~tune_axes

    """
    
    _peak_choices_ = "cen com".split()
    
    def __init__(self, signals, axis, signal_name=None):
        self.signals = signals
        self.signal_name = signal_name or signals[0].name
        self.axis = axis
        self.stats = {}
        self.tune_ok = False
        self.peaks = None
        self.peak_choice = self._peak_choices_[0]
        self.center = None
        self.stats = []
        
        # defaults
        self.width = 1
        self.num = 10
        self.step_factor = 4
        self.pass_max = 6
        self.snake = True

    def tune(self, width=None, num=None, md=None):
        """
        BlueSky plan to execute one pass through the current scan range
        
        Scan self.axis centered about current position from
        ``-width/2`` to ``+width/2`` with ``num`` observations.
        If a peak was detected (default check is that max >= 4*min), 
        then set ``self.tune_ok = True``.

        PARAMETERS
    
        width : float
            width of the tuning scan in the units of ``self.axis``
            Default value in ``self.width`` (initially 1)
        num : int
            number of steps
            Default value in ``self.num`` (initially 10)
        md : dict, optional
            metadata
        """
        width = width or self.width
        num = num or self.num
        
        if self.peak_choice not in self._peak_choices_:
            msg = "peak_choice must be one of {}, geave {}"
            msg = msg.format(self._peak_choices_, self.peak_choice)
            raise ValueError(msg)

        initial_position = self.axis.position
        # final_position = initial_position       # unless tuned
        start = initial_position - width/2
        finish = initial_position + width/2
        self.tune_ok = False

        tune_md = dict(
            width = width,
            initial_position = self.axis.position,
            time_iso8601 = str(datetime.datetime.now()),
            )
        _md = {'tune_md': tune_md,
               'plan_name': self.__class__.__name__ + '.tune',
               'tune_parameters': dict(
                    num = num,
                    width = width,
                    initial_position = self.axis.position,
                    peak_choice = self.peak_choice,
                    x_axis = self.axis.name,
                    y_axis = self.signal_name,
                   ),
               'motors': (self.axis.name,),
               'detectors': (self.signal_name,),
               'hints': dict(
                   dimensions = [
                       (
                           [self.axis.name], 
                           'primary')]
                   )
               }
        _md.update(md or {})
        if "pass_max" not in _md:
            self.stats = []
        self.peaks = PeakStats(x=self.axis.name, y=self.signal_name)
        
        class Results(Device):
            """because bps.read() needs a Device or a Signal)"""
            tune_ok = Component(Signal)
            initial_position = Component(Signal)
            final_position = Component(Signal)
            center = Component(Signal)
            # - - - - -
            x = Component(Signal)
            y = Component(Signal)
            cen = Component(Signal)
            com = Component(Signal)
            fwhm = Component(Signal)
            min = Component(Signal)
            max = Component(Signal)
            crossings = Component(Signal)
            peakstats_attrs = "x y cen com fwhm min max crossings".split()
            
            def report(self, title=None):
                keys = self.peakstats_attrs + "tune_ok center initial_position final_position".split()
                t = pyRestTable.Table()
                t.addLabel("key")
                t.addLabel("result")
                for key in keys:
                    v = getattr(self, key).value
                    t.addRow((key, str(v)))
                if title is not None:
                    print(title)
                print(t)

        @bpp.subs_decorator(self.peaks)
        def _scan(md=None):
            yield from bps.open_run(md)

            position_list = np.linspace(start, finish, num)
            signal_list = list(self.signals)
            signal_list += [self.axis,]
            for pos in position_list:
                yield from bps.mv(self.axis, pos)
                yield from bps.trigger_and_read(signal_list)
            
            final_position = initial_position
            if self.peak_detected():
                self.tune_ok = True
                if self.peak_choice == "cen":
                    final_position = self.peaks.cen
                elif self.peak_choice == "com":
                    final_position = self.peaks.com
                else:
                    final_position = None
                self.center = final_position

            # add stream with results
            # yield from add_results_stream()
            stream_name = "PeakStats"
            results = Results(name=stream_name)

            results.tune_ok.put(self.tune_ok)
            results.center.put(self.center)
            results.final_position.put(final_position)
            results.initial_position.put(initial_position)
            for key in results.peakstats_attrs:
                v = getattr(self.peaks, key)
                if key in ("crossings", "min", "max"):
                    v = np.array(v)
                getattr(results, key).put(v)

            if results.tune_ok.value:
                yield from bps.create(name=stream_name)
                try:
                    yield from bps.read(results)
                except ValueError as ex:
                    separator = " "*8 + "-"*12
                    print(separator)
                    print(f"Error saving stream {stream_name}:\n{ex}")
                    print(separator)
                yield from bps.save()
            
            yield from bps.mv(self.axis, final_position)
            self.stats.append(self.peaks)
            yield from bps.close_run()

            results.report(stream_name)
    
        return (yield from _scan(md=_md))
        
    
    def multi_pass_tune(self, width=None, step_factor=None, 
                        num=None, pass_max=None, snake=None, md=None):
        """
        BlueSky plan for tuning this axis with this signal
        
        Execute multiple passes to refine the centroid determination.
        Each subsequent pass will reduce the width of scan by ``step_factor``.
        If ``snake=True`` then the scan direction will reverse with
        each subsequent pass.

        PARAMETERS
    
        width : float
            width of the tuning scan in the units of ``self.axis``
            Default value in ``self.width`` (initially 1)
        num : int
            number of steps
            Default value in ``self.num`` (initially 10)
        step_factor : float
            This reduces the width of the next tuning scan by the given factor.
            Default value in ``self.step_factor`` (initially 4)
        pass_max : int
            Maximum number of passes to be executed (avoids runaway
            scans when a centroid is not found).
            Default value in ``self.pass_max`` (initially 10)
        snake : bool
            If ``True``, reverse scan direction on next pass.
            Default value in ``self.snake`` (initially True)
        md : dict, optional
            metadata
        """
        width = width or self.width
        num = num or self.num
        step_factor = step_factor or self.step_factor
        snake = snake or self.snake
        pass_max = pass_max or self.pass_max
        
        self.stats = []

        def _scan(width=1, step_factor=10, num=10, snake=True):
            for _pass_number in range(pass_max):
                _md = {'pass': _pass_number+1,
                       'pass_max': pass_max,
                       'plan_name': self.__class__.__name__ + '.multi_pass_tune',
                       }
                _md.update(md or {})
            
                yield from self.tune(width=width, num=num, md=_md)

                if not self.tune_ok:
                    return
                width /= step_factor
                if snake:
                    width *= -1
        
        return (
            yield from _scan(
                width=width, step_factor=step_factor, num=num, snake=snake))
    
    def peak_detected(self):
        """
        returns True if a peak was detected, otherwise False
        
        The default algorithm identifies a peak when the maximum
        value is four times the minimum value.  Change this routine
        by subclassing :class:`TuneAxis` and override :meth:`peak_detected`.
        """
        if self.peaks is None:
            return False
        self.peaks.compute()
        if self.peaks.max is None:
            return False
        
        ymax = self.peaks.max[-1]
        ymin = self.peaks.min[-1]
        return ymax > 4*ymin        # this works for USAXS@APS


def tune_axes(axes):
    """
    BlueSky plan to tune a list of axes in sequence
    
    EXAMPLE
    
    Sequentially, tune a list of preconfigured axes::
        
        RE(tune_axes([mr, m2r, ar, a2r])
    
    SEE ALSO

    .. autosummary::
       
       ~TuneAxis
    """
    for axis in axes:
        yield from axis.tune()
