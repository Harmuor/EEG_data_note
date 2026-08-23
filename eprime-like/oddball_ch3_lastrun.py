#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2026.1.1),
    on 四  6/25 01:22:21 2026
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware, parallel
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2026.1.1'
expName = 'oddball_ch3'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = (1024, 768)
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/cheng/Desktop/EEG_study/eprime-like/oddball_ch3_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    # store pilot mode in data file
    thisExp.addData('piloting', PILOTING, priority=priority.LOW)
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # update experiment info
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName
    expInfo['expVersion'] = expVersion
    expInfo['psychopyVersion'] = psychopyVersion
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "welcome" ---
    welcome_text_1 = visual.TextStim(win=win, name='welcome_text_1',
        text='This is welcome\n\nPress “space” to continue',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    welcome_keyboard_1 = keyboard.Keyboard(deviceName='defaultKeyboard')
    # Run 'Begin Experiment' code from wel_port_code
    # from psychopy import parallel
    
    # p_port = parallel.ParallelPort(address = '0x0378')
    
    # Begin Experiment —— Mac 上专用
    class DummyPort:
        def setData(self, val): pass
        def setPin(self, pin, val): pass
        def getData(self): return 0
    
    p_port = DummyPort()
    have_port = False
    
    
    # --- Initialize components for Routine "instruction" ---
    instruction_text_1 = visual.TextStim(win=win, name='instruction_text_1',
        text='This is the instruction\n\nPress “space” to continue',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    instruction_keyboard = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "shuffle_stim" ---
    
    # --- Initialize components for Routine "prepare_marker" ---
    
    # --- Initialize components for Routine "KeepInMindSlide" ---
    KeepInMindSlide_image_1 = visual.ImageStim(
        win=win,
        name='KeepInMindSlide_image_1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    KeepInMindSlide_text_1 = visual.TextStim(win=win, name='KeepInMindSlide_text_1',
        text='Remember This face',
        font='Arial',
        pos=(0, 0.3), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "test_stimulus" ---
    
    # --- Initialize components for Routine "fixation" ---
    fixation_polygon_1 = visual.ShapeStim(
        win=win, name='fixation_polygon_1', vertices='cross',
        size=(0.1, 0.1),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "ISI" ---
    ISI_polygon_1 = visual.Rect(
        win=win, name='ISI_polygon_1',
        width=(2, 2)[0], height=(2, 2)[1],
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='black', fillColor='black',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "RSVP_2" ---
    RSVP_image_1 = visual.ImageStim(
        win=win,
        name='RSVP_image_1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "KeepInMindRecog" ---
    KeepInMindRecog_image_1 = visual.ImageStim(
        win=win,
        name='KeepInMindRecog_image_1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.4, 0.2), draggable=False, size=(0.3, 0.3),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    KeepInMindRecog_image_2 = visual.ImageStim(
        win=win,
        name='KeepInMindRecog_image_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.2), draggable=False, size=(0.3, 0.3),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    KeepInMindRecog_image_3 = visual.ImageStim(
        win=win,
        name='KeepInMindRecog_image_3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.4, 0.2), draggable=False, size=(0.3, 0.3),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    KeepInMindRecog_image_4 = visual.ImageStim(
        win=win,
        name='KeepInMindRecog_image_4', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.4, -0.2), draggable=False, size=(0.3, 0.3),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    KeepInMindRecog_image_5 = visual.ImageStim(
        win=win,
        name='KeepInMindRecog_image_5', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.2), draggable=False, size=(0.3, 0.3),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    KeepInMindRecog_image_6 = visual.ImageStim(
        win=win,
        name='KeepInMindRecog_image_6', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.4, -0.2), draggable=False, size=(0.3, 0.3),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    KeepInMindRecog_key_resp_1 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "judge" ---
    judge_text_1 = visual.TextStim(win=win, name='judge_text_1',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "redo_or_not" ---
    
    # --- Initialize components for Routine "pretend_redo" ---
    pretend_redo_text = visual.TextStim(win=win, name='pretend_redo_text',
        text='as if this is redo',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "goodbye" ---
    goodbye_text_1 = visual.TextStim(win=win, name='goodbye_text_1',
        text='This is goodbye\n\nPress the “space” to leave',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    goodbye_keyboard_1 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    if eyetracker is not None:
        eyetracker.enableEventReporting()
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "welcome" ---
    # create an object to store info about Routine welcome
    welcome = data.Routine(
        name='welcome',
        components=[welcome_text_1, welcome_keyboard_1],
    )
    welcome.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for welcome_keyboard_1
    welcome_keyboard_1.keys = []
    welcome_keyboard_1.rt = []
    _welcome_keyboard_1_allKeys = []
    # Run 'Begin Routine' code from wel_port_code
    # begin routine
    pulse_sent = False
    pulse_start = None
    p_port.setData(0)
    # store start times for welcome
    welcome.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    welcome.tStart = globalClock.getTime(format='float')
    welcome.status = STARTED
    thisExp.addData('welcome.started', welcome.tStart)
    welcome.maxDuration = None
    # keep track of which components have finished
    welcomeComponents = welcome.components
    for thisComponent in welcome.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "welcome" ---
    thisExp.currentRoutine = welcome
    welcome.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *welcome_text_1* updates
        
        # if welcome_text_1 is starting this frame...
        if welcome_text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome_text_1.frameNStart = frameN  # exact frame index
            welcome_text_1.tStart = t  # local t and not account for scr refresh
            welcome_text_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_text_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcome_text_1.started')
            # update status
            welcome_text_1.status = STARTED
            welcome_text_1.setAutoDraw(True)
        
        # if welcome_text_1 is active this frame...
        if welcome_text_1.status == STARTED:
            # update params
            pass
        
        # *welcome_keyboard_1* updates
        waitOnFlip = False
        
        # if welcome_keyboard_1 is starting this frame...
        if welcome_keyboard_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome_keyboard_1.frameNStart = frameN  # exact frame index
            welcome_keyboard_1.tStart = t  # local t and not account for scr refresh
            welcome_keyboard_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_keyboard_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcome_keyboard_1.started')
            # update status
            welcome_keyboard_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(welcome_keyboard_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(welcome_keyboard_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if welcome_keyboard_1.status == STARTED and not waitOnFlip:
            theseKeys = welcome_keyboard_1.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _welcome_keyboard_1_allKeys.extend(theseKeys)
            if len(_welcome_keyboard_1_allKeys):
                welcome_keyboard_1.keys = _welcome_keyboard_1_allKeys[-1].name  # just the last key pressed
                welcome_keyboard_1.rt = _welcome_keyboard_1_allKeys[-1].rt
                welcome_keyboard_1.duration = _welcome_keyboard_1_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from wel_port_code
        # for each frame
        if pulse_sent == False and welcome_text_1.status == NOT_STARTED:
            pulse_sent = True
            pulse_start = t
            p_port.setData(1)
        
        if pulse_sent == True and t > pulse_start + 0.1 - frameTolerance:
            p_port.setData(0)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=welcome,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            welcome.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if welcome.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in welcome.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "welcome" ---
    for thisComponent in welcome.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for welcome
    welcome.tStop = globalClock.getTime(format='float')
    welcome.tStopRefresh = tThisFlipGlobal
    thisExp.addData('welcome.stopped', welcome.tStop)
    # check responses
    if welcome_keyboard_1.keys in ['', [], None]:  # No response was made
        welcome_keyboard_1.keys = None
    thisExp.addData('welcome_keyboard_1.keys',welcome_keyboard_1.keys)
    if welcome_keyboard_1.keys != None:  # we had a response
        thisExp.addData('welcome_keyboard_1.rt', welcome_keyboard_1.rt)
        thisExp.addData('welcome_keyboard_1.duration', welcome_keyboard_1.duration)
    thisExp.nextEntry()
    # the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instruction" ---
    # create an object to store info about Routine instruction
    instruction = data.Routine(
        name='instruction',
        components=[instruction_text_1, instruction_keyboard],
    )
    instruction.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for instruction_keyboard
    instruction_keyboard.keys = []
    instruction_keyboard.rt = []
    _instruction_keyboard_allKeys = []
    # store start times for instruction
    instruction.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instruction.tStart = globalClock.getTime(format='float')
    instruction.status = STARTED
    thisExp.addData('instruction.started', instruction.tStart)
    instruction.maxDuration = None
    # keep track of which components have finished
    instructionComponents = instruction.components
    for thisComponent in instruction.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instruction" ---
    thisExp.currentRoutine = instruction
    instruction.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction_text_1* updates
        
        # if instruction_text_1 is starting this frame...
        if instruction_text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_text_1.frameNStart = frameN  # exact frame index
            instruction_text_1.tStart = t  # local t and not account for scr refresh
            instruction_text_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_text_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_text_1.started')
            # update status
            instruction_text_1.status = STARTED
            instruction_text_1.setAutoDraw(True)
        
        # if instruction_text_1 is active this frame...
        if instruction_text_1.status == STARTED:
            # update params
            pass
        
        # *instruction_keyboard* updates
        waitOnFlip = False
        
        # if instruction_keyboard is starting this frame...
        if instruction_keyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_keyboard.frameNStart = frameN  # exact frame index
            instruction_keyboard.tStart = t  # local t and not account for scr refresh
            instruction_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_keyboard, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_keyboard.started')
            # update status
            instruction_keyboard.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instruction_keyboard.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instruction_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instruction_keyboard.status == STARTED and not waitOnFlip:
            theseKeys = instruction_keyboard.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _instruction_keyboard_allKeys.extend(theseKeys)
            if len(_instruction_keyboard_allKeys):
                instruction_keyboard.keys = _instruction_keyboard_allKeys[-1].name  # just the last key pressed
                instruction_keyboard.rt = _instruction_keyboard_allKeys[-1].rt
                instruction_keyboard.duration = _instruction_keyboard_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instruction,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            instruction.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if instruction.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in instruction.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction" ---
    for thisComponent in instruction.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instruction
    instruction.tStop = globalClock.getTime(format='float')
    instruction.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instruction.stopped', instruction.tStop)
    # check responses
    if instruction_keyboard.keys in ['', [], None]:  # No response was made
        instruction_keyboard.keys = None
    thisExp.addData('instruction_keyboard.keys',instruction_keyboard.keys)
    if instruction_keyboard.keys != None:  # we had a response
        thisExp.addData('instruction_keyboard.rt', instruction_keyboard.rt)
        thisExp.addData('instruction_keyboard.duration', instruction_keyboard.duration)
    thisExp.nextEntry()
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    InMind = data.TrialHandler2(
        name='InMind',
        nReps=8, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('list/list.xlsx'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(InMind)  # add the loop to the experiment
    thisInMind = InMind.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInMind.rgb)
    if thisInMind != None:
        for paramName in thisInMind:
            globals()[paramName] = thisInMind[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisInMind in InMind:
        InMind.status = STARTED
        if hasattr(thisInMind, 'status'):
            thisInMind.status = STARTED
        currentLoop = InMind
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisInMind.rgb)
        if thisInMind != None:
            for paramName in thisInMind:
                globals()[paramName] = thisInMind[paramName]
        
        # --- Prepare to start Routine "shuffle_stim" ---
        # create an object to store info about Routine shuffle_stim
        shuffle_stim = data.Routine(
            name='shuffle_stim',
            components=[],
        )
        shuffle_stim.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from shuffle_code_3
        from random import shuffle
        
        # 1. 构造列表
        stim = [
            './img/1.jpg', './img/2.jpg', './img/3.jpg',
            './img/4.jpg', './img/5.jpg', './img/6.jpg'
        ] * 10
        
        # 加入两个 oddball
        stim += ['./img/101.jpg', './img/102.jpg']
        
        list_ok = False
        
        while not list_ok:
        
            # 初始化标志变量
            double_stim = False
            too_close = False
        
            # 2. 检查相邻重复
            for i in range(len(stim) - 1):
                if stim[i] == stim[i + 1]:
                    double_stim = True
                    break
        
            # 3. 检查 oddball 距离
            odd_1 = stim.index("./img/102.jpg")
            odd_2 = stim.index("./img/101.jpg")
        
            if abs(odd_1 - odd_2) < 2:
                too_close = True
        
            # 4. 如果不满足条件 → 重新 shuffle
            if double_stim or too_close:
                shuffle(stim)
            else:
                list_ok = True
        
        # 最终列表
        stimulus_list = stim
        
        
        
        # store start times for shuffle_stim
        shuffle_stim.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        shuffle_stim.tStart = globalClock.getTime(format='float')
        shuffle_stim.status = STARTED
        thisExp.addData('shuffle_stim.started', shuffle_stim.tStart)
        shuffle_stim.maxDuration = None
        # keep track of which components have finished
        shuffle_stimComponents = shuffle_stim.components
        for thisComponent in shuffle_stim.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "shuffle_stim" ---
        thisExp.currentRoutine = shuffle_stim
        shuffle_stim.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisInMind, 'status') and thisInMind.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=shuffle_stim,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                shuffle_stim.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if shuffle_stim.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in shuffle_stim.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "shuffle_stim" ---
        for thisComponent in shuffle_stim.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for shuffle_stim
        shuffle_stim.tStop = globalClock.getTime(format='float')
        shuffle_stim.tStopRefresh = tThisFlipGlobal
        thisExp.addData('shuffle_stim.stopped', shuffle_stim.tStop)
        # the Routine "shuffle_stim" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "prepare_marker" ---
        # create an object to store info about Routine prepare_marker
        prepare_marker = data.Routine(
            name='prepare_marker',
            components=[],
        )
        prepare_marker.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_3
        # 这个是为了脑电marker作准备
        # 首先是类型marker
        category_list = []
        
        for i in stimulus_list:
        
            if i == relpicture:
                category_list.append(201)
        
            elif i in ['./img/101.jpg', './img/102.jpg']:
                category_list.append(203)
        
            else:
                category_list.append(202)
                
        # 然后是具体刺marker
        # 比较笨哈我，真不熟悉python
        specific_list = []
        
        for i in stimulus_list:
            if i == './img/101.jpg':
                specific_list.append(101)
            elif i == './img/102.jpg':
                specific_list.append(102)
            elif i == './img/1.jpg':
                specific_list.append(1)
            elif i == './img/2.jpg':
                specific_list.append(2)
            elif i == './img/3.jpg':
                specific_list.append(3)
            elif i == './img/4.jpg':
                specific_list.append(4)
            elif i == './img/5.jpg':
                specific_list.append(5)
            else:
                specific_list.append(6)
        # store start times for prepare_marker
        prepare_marker.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        prepare_marker.tStart = globalClock.getTime(format='float')
        prepare_marker.status = STARTED
        thisExp.addData('prepare_marker.started', prepare_marker.tStart)
        prepare_marker.maxDuration = None
        # keep track of which components have finished
        prepare_markerComponents = prepare_marker.components
        for thisComponent in prepare_marker.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "prepare_marker" ---
        thisExp.currentRoutine = prepare_marker
        prepare_marker.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisInMind, 'status') and thisInMind.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=prepare_marker,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                prepare_marker.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if prepare_marker.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in prepare_marker.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "prepare_marker" ---
        for thisComponent in prepare_marker.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for prepare_marker
        prepare_marker.tStop = globalClock.getTime(format='float')
        prepare_marker.tStopRefresh = tThisFlipGlobal
        thisExp.addData('prepare_marker.stopped', prepare_marker.tStop)
        # the Routine "prepare_marker" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "KeepInMindSlide" ---
        # create an object to store info about Routine KeepInMindSlide
        KeepInMindSlide = data.Routine(
            name='KeepInMindSlide',
            components=[KeepInMindSlide_image_1, KeepInMindSlide_text_1],
        )
        KeepInMindSlide.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        KeepInMindSlide_image_1.setImage(relpicture)
        # store start times for KeepInMindSlide
        KeepInMindSlide.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        KeepInMindSlide.tStart = globalClock.getTime(format='float')
        KeepInMindSlide.status = STARTED
        thisExp.addData('KeepInMindSlide.started', KeepInMindSlide.tStart)
        KeepInMindSlide.maxDuration = None
        # keep track of which components have finished
        KeepInMindSlideComponents = KeepInMindSlide.components
        for thisComponent in KeepInMindSlide.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "KeepInMindSlide" ---
        thisExp.currentRoutine = KeepInMindSlide
        KeepInMindSlide.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.995:
            # if trial has changed, end Routine now
            if hasattr(thisInMind, 'status') and thisInMind.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *KeepInMindSlide_image_1* updates
            
            # if KeepInMindSlide_image_1 is starting this frame...
            if KeepInMindSlide_image_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                KeepInMindSlide_image_1.frameNStart = frameN  # exact frame index
                KeepInMindSlide_image_1.tStart = t  # local t and not account for scr refresh
                KeepInMindSlide_image_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(KeepInMindSlide_image_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KeepInMindSlide_image_1.started')
                # update status
                KeepInMindSlide_image_1.status = STARTED
                KeepInMindSlide_image_1.setAutoDraw(True)
            
            # if KeepInMindSlide_image_1 is active this frame...
            if KeepInMindSlide_image_1.status == STARTED:
                # update params
                pass
            
            # if KeepInMindSlide_image_1 is stopping this frame...
            if KeepInMindSlide_image_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > KeepInMindSlide_image_1.tStartRefresh + 1.995-frameTolerance:
                    # keep track of stop time/frame for later
                    KeepInMindSlide_image_1.tStop = t  # not accounting for scr refresh
                    KeepInMindSlide_image_1.tStopRefresh = tThisFlipGlobal  # on global time
                    KeepInMindSlide_image_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'KeepInMindSlide_image_1.stopped')
                    # update status
                    KeepInMindSlide_image_1.status = FINISHED
                    KeepInMindSlide_image_1.setAutoDraw(False)
            
            # *KeepInMindSlide_text_1* updates
            
            # if KeepInMindSlide_text_1 is starting this frame...
            if KeepInMindSlide_text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                KeepInMindSlide_text_1.frameNStart = frameN  # exact frame index
                KeepInMindSlide_text_1.tStart = t  # local t and not account for scr refresh
                KeepInMindSlide_text_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(KeepInMindSlide_text_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KeepInMindSlide_text_1.started')
                # update status
                KeepInMindSlide_text_1.status = STARTED
                KeepInMindSlide_text_1.setAutoDraw(True)
            
            # if KeepInMindSlide_text_1 is active this frame...
            if KeepInMindSlide_text_1.status == STARTED:
                # update params
                pass
            
            # if KeepInMindSlide_text_1 is stopping this frame...
            if KeepInMindSlide_text_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > KeepInMindSlide_text_1.tStartRefresh + 1.995-frameTolerance:
                    # keep track of stop time/frame for later
                    KeepInMindSlide_text_1.tStop = t  # not accounting for scr refresh
                    KeepInMindSlide_text_1.tStopRefresh = tThisFlipGlobal  # on global time
                    KeepInMindSlide_text_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'KeepInMindSlide_text_1.stopped')
                    # update status
                    KeepInMindSlide_text_1.status = FINISHED
                    KeepInMindSlide_text_1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=KeepInMindSlide,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                KeepInMindSlide.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if KeepInMindSlide.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in KeepInMindSlide.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "KeepInMindSlide" ---
        for thisComponent in KeepInMindSlide.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for KeepInMindSlide
        KeepInMindSlide.tStop = globalClock.getTime(format='float')
        KeepInMindSlide.tStopRefresh = tThisFlipGlobal
        thisExp.addData('KeepInMindSlide.stopped', KeepInMindSlide.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if KeepInMindSlide.maxDurationReached:
            routineTimer.addTime(-KeepInMindSlide.maxDuration)
        elif KeepInMindSlide.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.995000)
        
        # --- Prepare to start Routine "test_stimulus" ---
        # create an object to store info about Routine test_stimulus
        test_stimulus = data.Routine(
            name='test_stimulus',
            components=[],
        )
        test_stimulus.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from test_stimulus_code_3
        # 然后测试界面的图片呈现搞一搞随机化，因为这个是等额呈现并选择，所以应该不用很麻烦
        # 首先构造样本空间
        test_stim = [
            './img/1.jpg', './img/2.jpg', './img/3.jpg',
            './img/4.jpg', './img/5.jpg', './img/6.jpg'
        ]
        
        shuffle(test_stim)
        #因为python从0开始，但是实际按键从1开始所以这里加1
        correction_choice = test_stim.index(relpicture) + 1 
        # store start times for test_stimulus
        test_stimulus.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        test_stimulus.tStart = globalClock.getTime(format='float')
        test_stimulus.status = STARTED
        thisExp.addData('test_stimulus.started', test_stimulus.tStart)
        test_stimulus.maxDuration = None
        # keep track of which components have finished
        test_stimulusComponents = test_stimulus.components
        for thisComponent in test_stimulus.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "test_stimulus" ---
        thisExp.currentRoutine = test_stimulus
        test_stimulus.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisInMind, 'status') and thisInMind.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=test_stimulus,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                test_stimulus.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if test_stimulus.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in test_stimulus.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "test_stimulus" ---
        for thisComponent in test_stimulus.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for test_stimulus
        test_stimulus.tStop = globalClock.getTime(format='float')
        test_stimulus.tStopRefresh = tThisFlipGlobal
        thisExp.addData('test_stimulus.stopped', test_stimulus.tStop)
        # the Routine "test_stimulus" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "fixation" ---
        # create an object to store info about Routine fixation
        fixation = data.Routine(
            name='fixation',
            components=[fixation_polygon_1],
        )
        fixation.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for fixation
        fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        fixation.tStart = globalClock.getTime(format='float')
        fixation.status = STARTED
        thisExp.addData('fixation.started', fixation.tStart)
        fixation.maxDuration = None
        # keep track of which components have finished
        fixationComponents = fixation.components
        for thisComponent in fixation.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixation" ---
        thisExp.currentRoutine = fixation
        fixation.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.695:
            # if trial has changed, end Routine now
            if hasattr(thisInMind, 'status') and thisInMind.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_polygon_1* updates
            
            # if fixation_polygon_1 is starting this frame...
            if fixation_polygon_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_polygon_1.frameNStart = frameN  # exact frame index
                fixation_polygon_1.tStart = t  # local t and not account for scr refresh
                fixation_polygon_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_polygon_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_polygon_1.started')
                # update status
                fixation_polygon_1.status = STARTED
                fixation_polygon_1.setAutoDraw(True)
            
            # if fixation_polygon_1 is active this frame...
            if fixation_polygon_1.status == STARTED:
                # update params
                pass
            
            # if fixation_polygon_1 is stopping this frame...
            if fixation_polygon_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_polygon_1.tStartRefresh + 0.695-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_polygon_1.tStop = t  # not accounting for scr refresh
                    fixation_polygon_1.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation_polygon_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_polygon_1.stopped')
                    # update status
                    fixation_polygon_1.status = FINISHED
                    fixation_polygon_1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=fixation,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                fixation.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if fixation.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in fixation.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation" ---
        for thisComponent in fixation.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for fixation
        fixation.tStop = globalClock.getTime(format='float')
        fixation.tStopRefresh = tThisFlipGlobal
        thisExp.addData('fixation.stopped', fixation.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if fixation.maxDurationReached:
            routineTimer.addTime(-fixation.maxDuration)
        elif fixation.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.695000)
        
        # set up handler to look after randomisation of conditions etc
        RSVPList = data.TrialHandler2(
            name='RSVPList',
            nReps=62, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
            isTrials=True, 
        )
        thisExp.addLoop(RSVPList)  # add the loop to the experiment
        thisRSVPList = RSVPList.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisRSVPList.rgb)
        if thisRSVPList != None:
            for paramName in thisRSVPList:
                globals()[paramName] = thisRSVPList[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisRSVPList in RSVPList:
            RSVPList.status = STARTED
            if hasattr(thisRSVPList, 'status'):
                thisRSVPList.status = STARTED
            currentLoop = RSVPList
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisRSVPList.rgb)
            if thisRSVPList != None:
                for paramName in thisRSVPList:
                    globals()[paramName] = thisRSVPList[paramName]
            
            # --- Prepare to start Routine "ISI" ---
            # create an object to store info about Routine ISI
            ISI = data.Routine(
                name='ISI',
                components=[ISI_polygon_1],
            )
            ISI.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_4
            p_port.setData(0)
            port_sent = False
            prot_start = None
            # store start times for ISI
            ISI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            ISI.tStart = globalClock.getTime(format='float')
            ISI.status = STARTED
            thisExp.addData('ISI.started', ISI.tStart)
            ISI.maxDuration = None
            # keep track of which components have finished
            ISIComponents = ISI.components
            for thisComponent in ISI.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI" ---
            thisExp.currentRoutine = ISI
            ISI.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.095:
                # if trial has changed, end Routine now
                if hasattr(thisRSVPList, 'status') and thisRSVPList.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ISI_polygon_1* updates
                
                # if ISI_polygon_1 is starting this frame...
                if ISI_polygon_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ISI_polygon_1.frameNStart = frameN  # exact frame index
                    ISI_polygon_1.tStart = t  # local t and not account for scr refresh
                    ISI_polygon_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ISI_polygon_1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ISI_polygon_1.started')
                    # update status
                    ISI_polygon_1.status = STARTED
                    ISI_polygon_1.setAutoDraw(True)
                
                # if ISI_polygon_1 is active this frame...
                if ISI_polygon_1.status == STARTED:
                    # update params
                    pass
                
                # if ISI_polygon_1 is stopping this frame...
                if ISI_polygon_1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ISI_polygon_1.tStartRefresh + 0.095-frameTolerance:
                        # keep track of stop time/frame for later
                        ISI_polygon_1.tStop = t  # not accounting for scr refresh
                        ISI_polygon_1.tStopRefresh = tThisFlipGlobal  # on global time
                        ISI_polygon_1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ISI_polygon_1.stopped')
                        # update status
                        ISI_polygon_1.status = FINISHED
                        ISI_polygon_1.setAutoDraw(False)
                # Run 'Each Frame' code from code_4
                if port_sent == False and ISI_polygon_1.status == NOT_STARTED:
                    port_sent = True
                    port_srat = t
                    p_port.setData(specific_list[RSVPList.thisN])
                
                if port_sent == True and t > port_srat + 0.1 - frameTolerance:
                    p_port.setData(0)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=ISI,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    ISI.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if ISI.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in ISI.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI" ---
            for thisComponent in ISI.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for ISI
            ISI.tStop = globalClock.getTime(format='float')
            ISI.tStopRefresh = tThisFlipGlobal
            thisExp.addData('ISI.stopped', ISI.tStop)
            # Run 'End Routine' code from code_4
            thisExp.addData('trigger', specific_list[RSVPList.thisN])
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if ISI.maxDurationReached:
                routineTimer.addTime(-ISI.maxDuration)
            elif ISI.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.095000)
            
            # --- Prepare to start Routine "RSVP_2" ---
            # create an object to store info about Routine RSVP_2
            RSVP_2 = data.Routine(
                name='RSVP_2',
                components=[RSVP_image_1],
            )
            RSVP_2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            RSVP_image_1.setImage(stimulus_list[RSVPList.thisN])
            # Run 'Begin Routine' code from code_5
            p_port.setData(0)
            port_start = None
            port_sent = False
            # store start times for RSVP_2
            RSVP_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            RSVP_2.tStart = globalClock.getTime(format='float')
            RSVP_2.status = STARTED
            thisExp.addData('RSVP_2.started', RSVP_2.tStart)
            RSVP_2.maxDuration = None
            # keep track of which components have finished
            RSVP_2Components = RSVP_2.components
            for thisComponent in RSVP_2.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "RSVP_2" ---
            thisExp.currentRoutine = RSVP_2
            RSVP_2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.595:
                # if trial has changed, end Routine now
                if hasattr(thisRSVPList, 'status') and thisRSVPList.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *RSVP_image_1* updates
                
                # if RSVP_image_1 is starting this frame...
                if RSVP_image_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    RSVP_image_1.frameNStart = frameN  # exact frame index
                    RSVP_image_1.tStart = t  # local t and not account for scr refresh
                    RSVP_image_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(RSVP_image_1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RSVP_image_1.started')
                    # update status
                    RSVP_image_1.status = STARTED
                    RSVP_image_1.setAutoDraw(True)
                
                # if RSVP_image_1 is active this frame...
                if RSVP_image_1.status == STARTED:
                    # update params
                    pass
                
                # if RSVP_image_1 is stopping this frame...
                if RSVP_image_1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > RSVP_image_1.tStartRefresh + 0.595-frameTolerance:
                        # keep track of stop time/frame for later
                        RSVP_image_1.tStop = t  # not accounting for scr refresh
                        RSVP_image_1.tStopRefresh = tThisFlipGlobal  # on global time
                        RSVP_image_1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'RSVP_image_1.stopped')
                        # update status
                        RSVP_image_1.status = FINISHED
                        RSVP_image_1.setAutoDraw(False)
                # Run 'Each Frame' code from code_5
                if port_sent == False and RSVP_image_1.status == NOT_STARTED:
                    port_sent = True
                    p_port.setData(category_list[RSVPList.thisN])
                    port_start = t
                    
                if port_sent == True and t > port_start + 0.1 - frameTolerance:
                    p_port.setData(0)
                    
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=RSVP_2,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    RSVP_2.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if RSVP_2.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in RSVP_2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "RSVP_2" ---
            for thisComponent in RSVP_2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for RSVP_2
            RSVP_2.tStop = globalClock.getTime(format='float')
            RSVP_2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('RSVP_2.stopped', RSVP_2.tStop)
            # Run 'End Routine' code from code_5
            thisExp.addData('trigger',category_list[RSVPList.thisN])
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if RSVP_2.maxDurationReached:
                routineTimer.addTime(-RSVP_2.maxDuration)
            elif RSVP_2.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.595000)
            # mark thisRSVPList as finished
            if hasattr(thisRSVPList, 'status'):
                thisRSVPList.status = FINISHED
            # if awaiting a pause, pause now
            if RSVPList.status == PAUSED:
                thisExp.status = PAUSED
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[globalClock], 
                )
                # once done pausing, restore running status
                RSVPList.status = STARTED
            thisExp.nextEntry()
            
        # completed 62 repeats of 'RSVPList'
        RSVPList.status = FINISHED
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "KeepInMindRecog" ---
        # create an object to store info about Routine KeepInMindRecog
        KeepInMindRecog = data.Routine(
            name='KeepInMindRecog',
            components=[KeepInMindRecog_image_1, KeepInMindRecog_image_2, KeepInMindRecog_image_3, KeepInMindRecog_image_4, KeepInMindRecog_image_5, KeepInMindRecog_image_6, KeepInMindRecog_key_resp_1],
        )
        KeepInMindRecog.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        KeepInMindRecog_image_1.setImage(test_stim[0])
        KeepInMindRecog_image_2.setImage(test_stim[1])
        KeepInMindRecog_image_3.setImage(test_stim[2])
        KeepInMindRecog_image_4.setImage(test_stim[3])
        KeepInMindRecog_image_5.setImage(test_stim[4])
        KeepInMindRecog_image_6.setImage(test_stim[5])
        # create starting attributes for KeepInMindRecog_key_resp_1
        KeepInMindRecog_key_resp_1.keys = []
        KeepInMindRecog_key_resp_1.rt = []
        _KeepInMindRecog_key_resp_1_allKeys = []
        # Run 'Begin Routine' code from code_6
        p_port.setData(0)
        port_start = None
        port_sent = False
        # store start times for KeepInMindRecog
        KeepInMindRecog.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        KeepInMindRecog.tStart = globalClock.getTime(format='float')
        KeepInMindRecog.status = STARTED
        thisExp.addData('KeepInMindRecog.started', KeepInMindRecog.tStart)
        KeepInMindRecog.maxDuration = None
        # keep track of which components have finished
        KeepInMindRecogComponents = KeepInMindRecog.components
        for thisComponent in KeepInMindRecog.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "KeepInMindRecog" ---
        thisExp.currentRoutine = KeepInMindRecog
        KeepInMindRecog.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisInMind, 'status') and thisInMind.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *KeepInMindRecog_image_1* updates
            
            # if KeepInMindRecog_image_1 is starting this frame...
            if KeepInMindRecog_image_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                KeepInMindRecog_image_1.frameNStart = frameN  # exact frame index
                KeepInMindRecog_image_1.tStart = t  # local t and not account for scr refresh
                KeepInMindRecog_image_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(KeepInMindRecog_image_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KeepInMindRecog_image_1.started')
                # update status
                KeepInMindRecog_image_1.status = STARTED
                KeepInMindRecog_image_1.setAutoDraw(True)
            
            # if KeepInMindRecog_image_1 is active this frame...
            if KeepInMindRecog_image_1.status == STARTED:
                # update params
                pass
            
            # if KeepInMindRecog_image_1 is stopping this frame...
            if KeepInMindRecog_image_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > KeepInMindRecog_image_1.tStartRefresh + 1.995-frameTolerance:
                    # keep track of stop time/frame for later
                    KeepInMindRecog_image_1.tStop = t  # not accounting for scr refresh
                    KeepInMindRecog_image_1.tStopRefresh = tThisFlipGlobal  # on global time
                    KeepInMindRecog_image_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'KeepInMindRecog_image_1.stopped')
                    # update status
                    KeepInMindRecog_image_1.status = FINISHED
                    KeepInMindRecog_image_1.setAutoDraw(False)
            
            # *KeepInMindRecog_image_2* updates
            
            # if KeepInMindRecog_image_2 is starting this frame...
            if KeepInMindRecog_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                KeepInMindRecog_image_2.frameNStart = frameN  # exact frame index
                KeepInMindRecog_image_2.tStart = t  # local t and not account for scr refresh
                KeepInMindRecog_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(KeepInMindRecog_image_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KeepInMindRecog_image_2.started')
                # update status
                KeepInMindRecog_image_2.status = STARTED
                KeepInMindRecog_image_2.setAutoDraw(True)
            
            # if KeepInMindRecog_image_2 is active this frame...
            if KeepInMindRecog_image_2.status == STARTED:
                # update params
                pass
            
            # if KeepInMindRecog_image_2 is stopping this frame...
            if KeepInMindRecog_image_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > KeepInMindRecog_image_2.tStartRefresh + 1.995-frameTolerance:
                    # keep track of stop time/frame for later
                    KeepInMindRecog_image_2.tStop = t  # not accounting for scr refresh
                    KeepInMindRecog_image_2.tStopRefresh = tThisFlipGlobal  # on global time
                    KeepInMindRecog_image_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'KeepInMindRecog_image_2.stopped')
                    # update status
                    KeepInMindRecog_image_2.status = FINISHED
                    KeepInMindRecog_image_2.setAutoDraw(False)
            
            # *KeepInMindRecog_image_3* updates
            
            # if KeepInMindRecog_image_3 is starting this frame...
            if KeepInMindRecog_image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                KeepInMindRecog_image_3.frameNStart = frameN  # exact frame index
                KeepInMindRecog_image_3.tStart = t  # local t and not account for scr refresh
                KeepInMindRecog_image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(KeepInMindRecog_image_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KeepInMindRecog_image_3.started')
                # update status
                KeepInMindRecog_image_3.status = STARTED
                KeepInMindRecog_image_3.setAutoDraw(True)
            
            # if KeepInMindRecog_image_3 is active this frame...
            if KeepInMindRecog_image_3.status == STARTED:
                # update params
                pass
            
            # if KeepInMindRecog_image_3 is stopping this frame...
            if KeepInMindRecog_image_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > KeepInMindRecog_image_3.tStartRefresh + 1.995-frameTolerance:
                    # keep track of stop time/frame for later
                    KeepInMindRecog_image_3.tStop = t  # not accounting for scr refresh
                    KeepInMindRecog_image_3.tStopRefresh = tThisFlipGlobal  # on global time
                    KeepInMindRecog_image_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'KeepInMindRecog_image_3.stopped')
                    # update status
                    KeepInMindRecog_image_3.status = FINISHED
                    KeepInMindRecog_image_3.setAutoDraw(False)
            
            # *KeepInMindRecog_image_4* updates
            
            # if KeepInMindRecog_image_4 is starting this frame...
            if KeepInMindRecog_image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                KeepInMindRecog_image_4.frameNStart = frameN  # exact frame index
                KeepInMindRecog_image_4.tStart = t  # local t and not account for scr refresh
                KeepInMindRecog_image_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(KeepInMindRecog_image_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KeepInMindRecog_image_4.started')
                # update status
                KeepInMindRecog_image_4.status = STARTED
                KeepInMindRecog_image_4.setAutoDraw(True)
            
            # if KeepInMindRecog_image_4 is active this frame...
            if KeepInMindRecog_image_4.status == STARTED:
                # update params
                pass
            
            # if KeepInMindRecog_image_4 is stopping this frame...
            if KeepInMindRecog_image_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > KeepInMindRecog_image_4.tStartRefresh + 1.995-frameTolerance:
                    # keep track of stop time/frame for later
                    KeepInMindRecog_image_4.tStop = t  # not accounting for scr refresh
                    KeepInMindRecog_image_4.tStopRefresh = tThisFlipGlobal  # on global time
                    KeepInMindRecog_image_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'KeepInMindRecog_image_4.stopped')
                    # update status
                    KeepInMindRecog_image_4.status = FINISHED
                    KeepInMindRecog_image_4.setAutoDraw(False)
            
            # *KeepInMindRecog_image_5* updates
            
            # if KeepInMindRecog_image_5 is starting this frame...
            if KeepInMindRecog_image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                KeepInMindRecog_image_5.frameNStart = frameN  # exact frame index
                KeepInMindRecog_image_5.tStart = t  # local t and not account for scr refresh
                KeepInMindRecog_image_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(KeepInMindRecog_image_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KeepInMindRecog_image_5.started')
                # update status
                KeepInMindRecog_image_5.status = STARTED
                KeepInMindRecog_image_5.setAutoDraw(True)
            
            # if KeepInMindRecog_image_5 is active this frame...
            if KeepInMindRecog_image_5.status == STARTED:
                # update params
                pass
            
            # if KeepInMindRecog_image_5 is stopping this frame...
            if KeepInMindRecog_image_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > KeepInMindRecog_image_5.tStartRefresh + 1.995-frameTolerance:
                    # keep track of stop time/frame for later
                    KeepInMindRecog_image_5.tStop = t  # not accounting for scr refresh
                    KeepInMindRecog_image_5.tStopRefresh = tThisFlipGlobal  # on global time
                    KeepInMindRecog_image_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'KeepInMindRecog_image_5.stopped')
                    # update status
                    KeepInMindRecog_image_5.status = FINISHED
                    KeepInMindRecog_image_5.setAutoDraw(False)
            
            # *KeepInMindRecog_image_6* updates
            
            # if KeepInMindRecog_image_6 is starting this frame...
            if KeepInMindRecog_image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                KeepInMindRecog_image_6.frameNStart = frameN  # exact frame index
                KeepInMindRecog_image_6.tStart = t  # local t and not account for scr refresh
                KeepInMindRecog_image_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(KeepInMindRecog_image_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KeepInMindRecog_image_6.started')
                # update status
                KeepInMindRecog_image_6.status = STARTED
                KeepInMindRecog_image_6.setAutoDraw(True)
            
            # if KeepInMindRecog_image_6 is active this frame...
            if KeepInMindRecog_image_6.status == STARTED:
                # update params
                pass
            
            # if KeepInMindRecog_image_6 is stopping this frame...
            if KeepInMindRecog_image_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > KeepInMindRecog_image_6.tStartRefresh + 1.995-frameTolerance:
                    # keep track of stop time/frame for later
                    KeepInMindRecog_image_6.tStop = t  # not accounting for scr refresh
                    KeepInMindRecog_image_6.tStopRefresh = tThisFlipGlobal  # on global time
                    KeepInMindRecog_image_6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'KeepInMindRecog_image_6.stopped')
                    # update status
                    KeepInMindRecog_image_6.status = FINISHED
                    KeepInMindRecog_image_6.setAutoDraw(False)
            
            # *KeepInMindRecog_key_resp_1* updates
            waitOnFlip = False
            
            # if KeepInMindRecog_key_resp_1 is starting this frame...
            if KeepInMindRecog_key_resp_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                KeepInMindRecog_key_resp_1.frameNStart = frameN  # exact frame index
                KeepInMindRecog_key_resp_1.tStart = t  # local t and not account for scr refresh
                KeepInMindRecog_key_resp_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(KeepInMindRecog_key_resp_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KeepInMindRecog_key_resp_1.started')
                # update status
                KeepInMindRecog_key_resp_1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(KeepInMindRecog_key_resp_1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(KeepInMindRecog_key_resp_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if KeepInMindRecog_key_resp_1.status == STARTED and not waitOnFlip:
                theseKeys = KeepInMindRecog_key_resp_1.getKeys(keyList=['1', '2', '3', '4', '5', '6'], ignoreKeys=["escape"], waitRelease=False)
                _KeepInMindRecog_key_resp_1_allKeys.extend(theseKeys)
                if len(_KeepInMindRecog_key_resp_1_allKeys):
                    KeepInMindRecog_key_resp_1.keys = _KeepInMindRecog_key_resp_1_allKeys[-1].name  # just the last key pressed
                    KeepInMindRecog_key_resp_1.rt = _KeepInMindRecog_key_resp_1_allKeys[-1].rt
                    KeepInMindRecog_key_resp_1.duration = _KeepInMindRecog_key_resp_1_allKeys[-1].duration
                    # was this correct?
                    if (KeepInMindRecog_key_resp_1.keys == str(correction_choice)) or (KeepInMindRecog_key_resp_1.keys == correction_choice):
                        KeepInMindRecog_key_resp_1.corr = 1
                    else:
                        KeepInMindRecog_key_resp_1.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            # Run 'Each Frame' code from code_6
            if KeepInMindRecog_key_resp_1.corr == 1:
                marker = 242
                p_port.setData(marker)
                port_sent = True
                port_start = t
                thisExp.addData('trigger', marker)
            if KeepInMindRecog_key_resp_1.corr == 0:
                marker = 241
                p_port.setData(marker)
                port_sent = True
                port_start = t
                thisExp.addData('trigger', marker)
                
            if port_sent == True and t > port_start + 0.1 - frameTolerance:
                p_port.setData(0)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=KeepInMindRecog,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                KeepInMindRecog.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if KeepInMindRecog.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in KeepInMindRecog.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "KeepInMindRecog" ---
        for thisComponent in KeepInMindRecog.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for KeepInMindRecog
        KeepInMindRecog.tStop = globalClock.getTime(format='float')
        KeepInMindRecog.tStopRefresh = tThisFlipGlobal
        thisExp.addData('KeepInMindRecog.stopped', KeepInMindRecog.tStop)
        # check responses
        if KeepInMindRecog_key_resp_1.keys in ['', [], None]:  # No response was made
            KeepInMindRecog_key_resp_1.keys = None
            # was no response the correct answer?!
            if str(correction_choice).lower() == 'none':
               KeepInMindRecog_key_resp_1.corr = 1;  # correct non-response
            else:
               KeepInMindRecog_key_resp_1.corr = 0;  # failed to respond (incorrectly)
        # store data for InMind (TrialHandler)
        InMind.addData('KeepInMindRecog_key_resp_1.keys',KeepInMindRecog_key_resp_1.keys)
        InMind.addData('KeepInMindRecog_key_resp_1.corr', KeepInMindRecog_key_resp_1.corr)
        if KeepInMindRecog_key_resp_1.keys != None:  # we had a response
            InMind.addData('KeepInMindRecog_key_resp_1.rt', KeepInMindRecog_key_resp_1.rt)
            InMind.addData('KeepInMindRecog_key_resp_1.duration', KeepInMindRecog_key_resp_1.duration)
        # the Routine "KeepInMindRecog" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "judge" ---
        # create an object to store info about Routine judge
        judge = data.Routine(
            name='judge',
            components=[judge_text_1],
        )
        judge.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from judge_code
        if KeepInMindRecog_key_resp_1.corr == 1:      #如果键盘控件key_resp的值被判断（两个连续的等号表示判断）为等于1，被试做对
            feedback = 'congratulation'       #变量feedback呈现‘恭喜’
            font_color = 'green'
        else:                       #如果如果键盘控件key_resp的值被判断为不等于1，即为0，被试做错
            feedback = 'pity'       #变量feedback呈现‘遗憾'
            font_color = 'red'
        judge_text_1.setColor(font_color, colorSpace='rgb')
        judge_text_1.setText(feedback)
        # store start times for judge
        judge.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        judge.tStart = globalClock.getTime(format='float')
        judge.status = STARTED
        thisExp.addData('judge.started', judge.tStart)
        judge.maxDuration = None
        # keep track of which components have finished
        judgeComponents = judge.components
        for thisComponent in judge.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "judge" ---
        thisExp.currentRoutine = judge
        judge.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.995:
            # if trial has changed, end Routine now
            if hasattr(thisInMind, 'status') and thisInMind.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *judge_text_1* updates
            
            # if judge_text_1 is starting this frame...
            if judge_text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                judge_text_1.frameNStart = frameN  # exact frame index
                judge_text_1.tStart = t  # local t and not account for scr refresh
                judge_text_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(judge_text_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'judge_text_1.started')
                # update status
                judge_text_1.status = STARTED
                judge_text_1.setAutoDraw(True)
            
            # if judge_text_1 is active this frame...
            if judge_text_1.status == STARTED:
                # update params
                pass
            
            # if judge_text_1 is stopping this frame...
            if judge_text_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > judge_text_1.tStartRefresh + 1.995-frameTolerance:
                    # keep track of stop time/frame for later
                    judge_text_1.tStop = t  # not accounting for scr refresh
                    judge_text_1.tStopRefresh = tThisFlipGlobal  # on global time
                    judge_text_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'judge_text_1.stopped')
                    # update status
                    judge_text_1.status = FINISHED
                    judge_text_1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=judge,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                judge.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if judge.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in judge.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "judge" ---
        for thisComponent in judge.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for judge
        judge.tStop = globalClock.getTime(format='float')
        judge.tStopRefresh = tThisFlipGlobal
        thisExp.addData('judge.stopped', judge.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if judge.maxDurationReached:
            routineTimer.addTime(-judge.maxDuration)
        elif judge.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.995000)
        # mark thisInMind as finished
        if hasattr(thisInMind, 'status'):
            thisInMind.status = FINISHED
        # if awaiting a pause, pause now
        if InMind.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            InMind.status = STARTED
        thisExp.nextEntry()
        
    # completed 8 repeats of 'InMind'
    InMind.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "redo_or_not" ---
    # create an object to store info about Routine redo_or_not
    redo_or_not = data.Routine(
        name='redo_or_not',
        components=[],
    )
    redo_or_not.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_2
    acc = InMind.data['KeepInMindRecog_key_resp_1.corr']
    
    acc_rate = sum(acc) / len(acc)
    
    if acc_rate < 0.6:
        nrep = 1
    else:
        nrep = 0
    # store start times for redo_or_not
    redo_or_not.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    redo_or_not.tStart = globalClock.getTime(format='float')
    redo_or_not.status = STARTED
    thisExp.addData('redo_or_not.started', redo_or_not.tStart)
    redo_or_not.maxDuration = None
    # keep track of which components have finished
    redo_or_notComponents = redo_or_not.components
    for thisComponent in redo_or_not.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "redo_or_not" ---
    thisExp.currentRoutine = redo_or_not
    redo_or_not.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=redo_or_not,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            redo_or_not.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if redo_or_not.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in redo_or_not.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "redo_or_not" ---
    for thisComponent in redo_or_not.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for redo_or_not
    redo_or_not.tStop = globalClock.getTime(format='float')
    redo_or_not.tStopRefresh = tThisFlipGlobal
    thisExp.addData('redo_or_not.stopped', redo_or_not.tStop)
    thisExp.nextEntry()
    # the Routine "redo_or_not" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    redo = data.TrialHandler2(
        name='redo',
        nReps=nrep, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(redo)  # add the loop to the experiment
    thisRedo = redo.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRedo.rgb)
    if thisRedo != None:
        for paramName in thisRedo:
            globals()[paramName] = thisRedo[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisRedo in redo:
        redo.status = STARTED
        if hasattr(thisRedo, 'status'):
            thisRedo.status = STARTED
        currentLoop = redo
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisRedo.rgb)
        if thisRedo != None:
            for paramName in thisRedo:
                globals()[paramName] = thisRedo[paramName]
        
        # --- Prepare to start Routine "pretend_redo" ---
        # create an object to store info about Routine pretend_redo
        pretend_redo = data.Routine(
            name='pretend_redo',
            components=[pretend_redo_text],
        )
        pretend_redo.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for pretend_redo
        pretend_redo.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        pretend_redo.tStart = globalClock.getTime(format='float')
        pretend_redo.status = STARTED
        thisExp.addData('pretend_redo.started', pretend_redo.tStart)
        pretend_redo.maxDuration = None
        # keep track of which components have finished
        pretend_redoComponents = pretend_redo.components
        for thisComponent in pretend_redo.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "pretend_redo" ---
        thisExp.currentRoutine = pretend_redo
        pretend_redo.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisRedo, 'status') and thisRedo.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *pretend_redo_text* updates
            
            # if pretend_redo_text is starting this frame...
            if pretend_redo_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                pretend_redo_text.frameNStart = frameN  # exact frame index
                pretend_redo_text.tStart = t  # local t and not account for scr refresh
                pretend_redo_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pretend_redo_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pretend_redo_text.started')
                # update status
                pretend_redo_text.status = STARTED
                pretend_redo_text.setAutoDraw(True)
            
            # if pretend_redo_text is active this frame...
            if pretend_redo_text.status == STARTED:
                # update params
                pass
            
            # if pretend_redo_text is stopping this frame...
            if pretend_redo_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > pretend_redo_text.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    pretend_redo_text.tStop = t  # not accounting for scr refresh
                    pretend_redo_text.tStopRefresh = tThisFlipGlobal  # on global time
                    pretend_redo_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'pretend_redo_text.stopped')
                    # update status
                    pretend_redo_text.status = FINISHED
                    pretend_redo_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=pretend_redo,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                pretend_redo.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if pretend_redo.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in pretend_redo.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pretend_redo" ---
        for thisComponent in pretend_redo.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for pretend_redo
        pretend_redo.tStop = globalClock.getTime(format='float')
        pretend_redo.tStopRefresh = tThisFlipGlobal
        thisExp.addData('pretend_redo.stopped', pretend_redo.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if pretend_redo.maxDurationReached:
            routineTimer.addTime(-pretend_redo.maxDuration)
        elif pretend_redo.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        # mark thisRedo as finished
        if hasattr(thisRedo, 'status'):
            thisRedo.status = FINISHED
        # if awaiting a pause, pause now
        if redo.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            redo.status = STARTED
        thisExp.nextEntry()
        
    # completed nrep repeats of 'redo'
    redo.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "goodbye" ---
    # create an object to store info about Routine goodbye
    goodbye = data.Routine(
        name='goodbye',
        components=[goodbye_text_1, goodbye_keyboard_1],
    )
    goodbye.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for goodbye_keyboard_1
    goodbye_keyboard_1.keys = []
    goodbye_keyboard_1.rt = []
    _goodbye_keyboard_1_allKeys = []
    # store start times for goodbye
    goodbye.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    goodbye.tStart = globalClock.getTime(format='float')
    goodbye.status = STARTED
    thisExp.addData('goodbye.started', goodbye.tStart)
    goodbye.maxDuration = None
    # keep track of which components have finished
    goodbyeComponents = goodbye.components
    for thisComponent in goodbye.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "goodbye" ---
    thisExp.currentRoutine = goodbye
    goodbye.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *goodbye_text_1* updates
        
        # if goodbye_text_1 is starting this frame...
        if goodbye_text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            goodbye_text_1.frameNStart = frameN  # exact frame index
            goodbye_text_1.tStart = t  # local t and not account for scr refresh
            goodbye_text_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(goodbye_text_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'goodbye_text_1.started')
            # update status
            goodbye_text_1.status = STARTED
            goodbye_text_1.setAutoDraw(True)
        
        # if goodbye_text_1 is active this frame...
        if goodbye_text_1.status == STARTED:
            # update params
            pass
        
        # *goodbye_keyboard_1* updates
        waitOnFlip = False
        
        # if goodbye_keyboard_1 is starting this frame...
        if goodbye_keyboard_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            goodbye_keyboard_1.frameNStart = frameN  # exact frame index
            goodbye_keyboard_1.tStart = t  # local t and not account for scr refresh
            goodbye_keyboard_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(goodbye_keyboard_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'goodbye_keyboard_1.started')
            # update status
            goodbye_keyboard_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(goodbye_keyboard_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(goodbye_keyboard_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if goodbye_keyboard_1.status == STARTED and not waitOnFlip:
            theseKeys = goodbye_keyboard_1.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _goodbye_keyboard_1_allKeys.extend(theseKeys)
            if len(_goodbye_keyboard_1_allKeys):
                goodbye_keyboard_1.keys = _goodbye_keyboard_1_allKeys[-1].name  # just the last key pressed
                goodbye_keyboard_1.rt = _goodbye_keyboard_1_allKeys[-1].rt
                goodbye_keyboard_1.duration = _goodbye_keyboard_1_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=goodbye,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            goodbye.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if goodbye.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in goodbye.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "goodbye" ---
    for thisComponent in goodbye.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for goodbye
    goodbye.tStop = globalClock.getTime(format='float')
    goodbye.tStopRefresh = tThisFlipGlobal
    thisExp.addData('goodbye.stopped', goodbye.tStop)
    # check responses
    if goodbye_keyboard_1.keys in ['', [], None]:  # No response was made
        goodbye_keyboard_1.keys = None
    thisExp.addData('goodbye_keyboard_1.keys',goodbye_keyboard_1.keys)
    if goodbye_keyboard_1.keys != None:  # we had a response
        thisExp.addData('goodbye_keyboard_1.rt', goodbye_keyboard_1.rt)
        thisExp.addData('goodbye_keyboard_1.duration', goodbye_keyboard_1.duration)
    thisExp.nextEntry()
    # the Routine "goodbye" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    # stop any playback components
    if thisExp.currentRoutine is not None:
        for comp in thisExp.currentRoutine.getPlaybackComponents():
            comp.stop()
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
