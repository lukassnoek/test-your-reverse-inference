#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.2),
    on Wed 19 Sep 2018 11:29:41 AM CEST
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'main'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'logs/%s_events.csv' % expInfo['participant']

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/media/lukas/goliath/test-your-reverse-inference/main.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='UVA', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='deg')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
welcome_txt = visual.TextStim(win=win, name='welcome_txt',
    text='Welcome!',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "show_img"
show_imgClock = core.Clock()
nr_correct = 0
img = visual.ImageStim(
    win=win, name='img',
    image='sin', mask=None,
    ori=0, pos=(0, 1.5), size=(10, 6.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
choice = visual.RatingScale(win=win, name='choice', marker='triangle', size=1.5, pos=[0.0, -0.6], choices=['WM', 'Neg-scene', 'faces', 'conflict'], tickHeight=-1, singleClick=True, showAccept=False)

# Initialize components for Routine "end"
endClock = core.Clock()
end_txt = visual.TextStim(win=win, name='end_txt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.6, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome"-------
t = 0
welcomeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
welcome_resp = event.BuilderKeyResponse()
# keep track of which components have finished
welcomeComponents = [welcome_txt, welcome_resp]
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_txt* updates
    if t >= 0.0 and welcome_txt.status == NOT_STARTED:
        # keep track of start time/frame for later
        welcome_txt.tStart = t
        welcome_txt.frameNStart = frameN  # exact frame index
        welcome_txt.setAutoDraw(True)
    
    # *welcome_resp* updates
    if t >= 0.0 and welcome_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        welcome_resp.tStart = t
        welcome_resp.frameNStart = frameN  # exact frame index
        welcome_resp.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if welcome_resp.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
img_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stims.csv'),
    seed=None, name='img_loop')
thisExp.addLoop(img_loop)  # add the loop to the experiment
thisImg_loop = img_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisImg_loop.rgb)
if thisImg_loop != None:
    for paramName in thisImg_loop:
        exec('{} = thisImg_loop[paramName]'.format(paramName))

for thisImg_loop in img_loop:
    currentLoop = img_loop
    # abbreviate parameter names if possible (e.g. rgb = thisImg_loop.rgb)
    if thisImg_loop != None:
        for paramName in thisImg_loop:
            exec('{} = thisImg_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "show_img"-------
    t = 0
    show_imgClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    
    img.setImage(contrast_img)
    choice.reset()
    # keep track of which components have finished
    show_imgComponents = [img, choice]
    for thisComponent in show_imgComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "show_img"-------
    while continueRoutine:
        # get current time
        t = show_imgClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *img* updates
        if t >= 0.0 and img.status == NOT_STARTED:
            # keep track of start time/frame for later
            img.tStart = t
            img.frameNStart = frameN  # exact frame index
            img.setAutoDraw(True)
        # *choice* updates
        if t >= 0.0 and choice.status == NOT_STARTED:
            # keep track of start time/frame for later
            choice.tStart = t
            choice.frameNStart = frameN  # exact frame index
            choice.setAutoDraw(True)
        continueRoutine &= choice.noResponse  # a response ends the trial
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in show_imgComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "show_img"-------
    for thisComponent in show_imgComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if choice.getRating() == correct_resp:
        nr_correct += 1
    # store data for img_loop (TrialHandler)
    img_loop.addData('choice.response', choice.getRating())
    # the Routine "show_img" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'img_loop'


# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
end_txt.setText(""" You had %i / 40 correct! """ % nr_correct)
# keep track of which components have finished
endComponents = [end_txt]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_txt* updates
    if t >= 0.0 and end_txt.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_txt.tStart = t
        end_txt.frameNStart = frameN  # exact frame index
        end_txt.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
