/******************** 
 * Oddball_Ch3 *
 ********************/


// store info about the experiment session:
let expName = 'oddball_ch3';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(welcomeRoutineBegin());
flowScheduler.add(welcomeRoutineEachFrame());
flowScheduler.add(welcomeRoutineEnd());
flowScheduler.add(instructionRoutineBegin());
flowScheduler.add(instructionRoutineEachFrame());
flowScheduler.add(instructionRoutineEnd());
const InMindLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(InMindLoopBegin(InMindLoopScheduler));
flowScheduler.add(InMindLoopScheduler);
flowScheduler.add(InMindLoopEnd);












flowScheduler.add(redo_or_notRoutineBegin());
flowScheduler.add(redo_or_notRoutineEachFrame());
flowScheduler.add(redo_or_notRoutineEnd());
const redoLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(redoLoopBegin(redoLoopScheduler));
flowScheduler.add(redoLoopScheduler);
flowScheduler.add(redoLoopEnd);


flowScheduler.add(goodbyeRoutineBegin());
flowScheduler.add(goodbyeRoutineEachFrame());
flowScheduler.add(goodbyeRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'list/list.xlsx', 'path': 'list/list.xlsx'},
    {'name': './img/1.jpg', 'path': './img/1.jpg'},
    {'name': './img/2.jpg', 'path': './img/2.jpg'},
    {'name': './img/3.jpg', 'path': './img/3.jpg'},
    {'name': './img/4.jpg', 'path': './img/4.jpg'},
    {'name': './img/5.jpg', 'path': './img/5.jpg'},
    {'name': './img/6.jpg', 'path': './img/6.jpg'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2026.1.1';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var welcomeClock;
var welcome_text_1;
var welcome_keyboard_1;
var p_port;
var have_port;
var instructionClock;
var instruction_text_1;
var instruction_keyboard;
var shuffle_stimClock;
var prepare_markerClock;
var KeepInMindSlideClock;
var KeepInMindSlide_image_1;
var KeepInMindSlide_text_1;
var test_stimulusClock;
var fixationClock;
var fixation_polygon_1;
var ISIClock;
var ISI_polygon_1;
var RSVP_2Clock;
var RSVP_image_1;
var KeepInMindRecogClock;
var KeepInMindRecog_image_1;
var KeepInMindRecog_image_2;
var KeepInMindRecog_image_3;
var KeepInMindRecog_image_4;
var KeepInMindRecog_image_5;
var KeepInMindRecog_image_6;
var KeepInMindRecog_key_resp_1;
var judgeClock;
var judge_text_1;
var redo_or_notClock;
var pretend_redoClock;
var pretend_redo_text;
var goodbyeClock;
var goodbye_text_1;
var goodbye_keyboard_1;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "welcome"
  welcomeClock = new util.Clock();
  welcome_text_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcome_text_1',
    text: 'This is welcome\n\nPress “space” to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  welcome_keyboard_1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from wel_port_code
  class DummyPort {
      setData(val) {
      }
      setPin(pin, val) {
      }
      getData() {
          return 0;
      }
  }
  p_port = new DummyPort();
  have_port = false;
  
  // Initialize components for Routine "instruction"
  instructionClock = new util.Clock();
  instruction_text_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_text_1',
    text: 'This is the instruction\n\nPress “space” to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  instruction_keyboard = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "shuffle_stim"
  shuffle_stimClock = new util.Clock();
  // Initialize components for Routine "prepare_marker"
  prepare_markerClock = new util.Clock();
  // Initialize components for Routine "KeepInMindSlide"
  KeepInMindSlideClock = new util.Clock();
  KeepInMindSlide_image_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'KeepInMindSlide_image_1', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  KeepInMindSlide_text_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'KeepInMindSlide_text_1',
    text: 'Remember This face',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "test_stimulus"
  test_stimulusClock = new util.Clock();
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  fixation_polygon_1 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation_polygon_1', 
    vertices: 'cross', size:[0.1, 0.1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 2.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: 0, 
    interpolate: true, 
  });
  
  // Initialize components for Routine "ISI"
  ISIClock = new util.Clock();
  ISI_polygon_1 = new visual.Rect ({
    win: psychoJS.window, name: 'ISI_polygon_1', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 2.0, 
    lineColor: new util.Color('black'), 
    fillColor: new util.Color('black'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: 0, 
    interpolate: true, 
  });
  
  // Initialize components for Routine "RSVP_2"
  RSVP_2Clock = new util.Clock();
  RSVP_image_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'RSVP_image_1', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "KeepInMindRecog"
  KeepInMindRecogClock = new util.Clock();
  KeepInMindRecog_image_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'KeepInMindRecog_image_1', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.4), 0.2], 
    draggable: false,
    size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  KeepInMindRecog_image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'KeepInMindRecog_image_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0.2], 
    draggable: false,
    size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  KeepInMindRecog_image_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'KeepInMindRecog_image_3', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.4, 0.2], 
    draggable: false,
    size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  KeepInMindRecog_image_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'KeepInMindRecog_image_4', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.4), (- 0.2)], 
    draggable: false,
    size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  KeepInMindRecog_image_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'KeepInMindRecog_image_5', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, (- 0.2)], 
    draggable: false,
    size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  KeepInMindRecog_image_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'KeepInMindRecog_image_6', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.4, (- 0.2)], 
    draggable: false,
    size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  KeepInMindRecog_key_resp_1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "judge"
  judgeClock = new util.Clock();
  judge_text_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'judge_text_1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "redo_or_not"
  redo_or_notClock = new util.Clock();
  // Initialize components for Routine "pretend_redo"
  pretend_redoClock = new util.Clock();
  pretend_redo_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'pretend_redo_text',
    text: 'as if this is redo',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "goodbye"
  goodbyeClock = new util.Clock();
  goodbye_text_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'goodbye_text_1',
    text: 'This is goodbye\n\nPress the “space” to leave',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  goodbye_keyboard_1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var welcomeMaxDurationReached;
var _welcome_keyboard_1_allKeys;
var pulse_sent;
var pulse_start;
var welcomeMaxDuration;
var welcomeComponents;
function welcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'welcome' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    welcomeClock.reset();
    routineTimer.reset();
    welcomeMaxDurationReached = false;
    // update component parameters for each repeat
    welcome_keyboard_1.keys = undefined;
    welcome_keyboard_1.rt = undefined;
    _welcome_keyboard_1_allKeys = [];
    // Run 'Begin Routine' code from wel_port_code
    pulse_sent = false;
    pulse_start = null;
    p_port.setData(0);
    
    psychoJS.experiment.addData('welcome.started', globalClock.getTime());
    welcomeMaxDuration = null
    // keep track of which components have finished
    welcomeComponents = [];
    welcomeComponents.push(welcome_text_1);
    welcomeComponents.push(welcome_keyboard_1);
    
    welcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function welcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'welcome' ---
    // get current time
    t = welcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *welcome_text_1* updates
    if (t >= 0.0 && welcome_text_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_text_1.tStart = t;  // (not accounting for frame time here)
      welcome_text_1.frameNStart = frameN;  // exact frame index
      
      welcome_text_1.setAutoDraw(true);
    }
    
    
    // if welcome_text_1 is active this frame...
    if (welcome_text_1.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *welcome_keyboard_1* updates
    if (t >= 0.0 && welcome_keyboard_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_keyboard_1.tStart = t;  // (not accounting for frame time here)
      welcome_keyboard_1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { welcome_keyboard_1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { welcome_keyboard_1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { welcome_keyboard_1.clearEvents(); });
    }
    
    // if welcome_keyboard_1 is active this frame...
    if (welcome_keyboard_1.status === PsychoJS.Status.STARTED) {
      let theseKeys = welcome_keyboard_1.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _welcome_keyboard_1_allKeys = _welcome_keyboard_1_allKeys.concat(theseKeys);
      if (_welcome_keyboard_1_allKeys.length > 0) {
        welcome_keyboard_1.keys = _welcome_keyboard_1_allKeys[_welcome_keyboard_1_allKeys.length - 1].name;  // just the last key pressed
        welcome_keyboard_1.rt = _welcome_keyboard_1_allKeys[_welcome_keyboard_1_allKeys.length - 1].rt;
        welcome_keyboard_1.duration = _welcome_keyboard_1_allKeys[_welcome_keyboard_1_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // Run 'Each Frame' code from wel_port_code
    if (((pulse_sent === false) && (welcome_text_1.status === NOT_STARTED))) {
        pulse_sent = true;
        pulse_start = t;
        p_port.setData(1);
    }
    if (((pulse_sent === true) && (t > ((pulse_start + 0.1) - frameTolerance)))) {
        p_port.setData(0);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    welcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function welcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'welcome' ---
    welcomeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('welcome.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(welcome_keyboard_1.corr, level);
    }
    psychoJS.experiment.addData('welcome_keyboard_1.keys', welcome_keyboard_1.keys);
    if (typeof welcome_keyboard_1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('welcome_keyboard_1.rt', welcome_keyboard_1.rt);
        psychoJS.experiment.addData('welcome_keyboard_1.duration', welcome_keyboard_1.duration);
        routineTimer.reset();
        }
    
    welcome_keyboard_1.stop();
    // the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var instructionMaxDurationReached;
var _instruction_keyboard_allKeys;
var instructionMaxDuration;
var instructionComponents;
function instructionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instruction' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    instructionClock.reset();
    routineTimer.reset();
    instructionMaxDurationReached = false;
    // update component parameters for each repeat
    instruction_keyboard.keys = undefined;
    instruction_keyboard.rt = undefined;
    _instruction_keyboard_allKeys = [];
    psychoJS.experiment.addData('instruction.started', globalClock.getTime());
    instructionMaxDuration = null
    // keep track of which components have finished
    instructionComponents = [];
    instructionComponents.push(instruction_text_1);
    instructionComponents.push(instruction_keyboard);
    
    instructionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instruction' ---
    // get current time
    t = instructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruction_text_1* updates
    if (t >= 0.0 && instruction_text_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction_text_1.tStart = t;  // (not accounting for frame time here)
      instruction_text_1.frameNStart = frameN;  // exact frame index
      
      instruction_text_1.setAutoDraw(true);
    }
    
    
    // if instruction_text_1 is active this frame...
    if (instruction_text_1.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *instruction_keyboard* updates
    if (t >= 0.0 && instruction_keyboard.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction_keyboard.tStart = t;  // (not accounting for frame time here)
      instruction_keyboard.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instruction_keyboard.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instruction_keyboard.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instruction_keyboard.clearEvents(); });
    }
    
    // if instruction_keyboard is active this frame...
    if (instruction_keyboard.status === PsychoJS.Status.STARTED) {
      let theseKeys = instruction_keyboard.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _instruction_keyboard_allKeys = _instruction_keyboard_allKeys.concat(theseKeys);
      if (_instruction_keyboard_allKeys.length > 0) {
        instruction_keyboard.keys = _instruction_keyboard_allKeys[_instruction_keyboard_allKeys.length - 1].name;  // just the last key pressed
        instruction_keyboard.rt = _instruction_keyboard_allKeys[_instruction_keyboard_allKeys.length - 1].rt;
        instruction_keyboard.duration = _instruction_keyboard_allKeys[_instruction_keyboard_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instruction' ---
    instructionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('instruction.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(instruction_keyboard.corr, level);
    }
    psychoJS.experiment.addData('instruction_keyboard.keys', instruction_keyboard.keys);
    if (typeof instruction_keyboard.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instruction_keyboard.rt', instruction_keyboard.rt);
        psychoJS.experiment.addData('instruction_keyboard.duration', instruction_keyboard.duration);
        routineTimer.reset();
        }
    
    instruction_keyboard.stop();
    // the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var InMind;
function InMindLoopBegin(InMindLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    InMind = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 8, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'list/list.xlsx',
      seed: undefined, name: 'InMind'
    });
    psychoJS.experiment.addLoop(InMind); // add the loop to the experiment
    currentLoop = InMind;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    InMind.forEach(function() {
      snapshot = InMind.getSnapshot();
    
      InMindLoopScheduler.add(importConditions(snapshot));
      InMindLoopScheduler.add(shuffle_stimRoutineBegin(snapshot));
      InMindLoopScheduler.add(shuffle_stimRoutineEachFrame());
      InMindLoopScheduler.add(shuffle_stimRoutineEnd(snapshot));
      InMindLoopScheduler.add(prepare_markerRoutineBegin(snapshot));
      InMindLoopScheduler.add(prepare_markerRoutineEachFrame());
      InMindLoopScheduler.add(prepare_markerRoutineEnd(snapshot));
      InMindLoopScheduler.add(KeepInMindSlideRoutineBegin(snapshot));
      InMindLoopScheduler.add(KeepInMindSlideRoutineEachFrame());
      InMindLoopScheduler.add(KeepInMindSlideRoutineEnd(snapshot));
      InMindLoopScheduler.add(test_stimulusRoutineBegin(snapshot));
      InMindLoopScheduler.add(test_stimulusRoutineEachFrame());
      InMindLoopScheduler.add(test_stimulusRoutineEnd(snapshot));
      InMindLoopScheduler.add(fixationRoutineBegin(snapshot));
      InMindLoopScheduler.add(fixationRoutineEachFrame());
      InMindLoopScheduler.add(fixationRoutineEnd(snapshot));
      const RSVPListLoopScheduler = new Scheduler(psychoJS);
      InMindLoopScheduler.add(RSVPListLoopBegin(RSVPListLoopScheduler, snapshot));
      InMindLoopScheduler.add(RSVPListLoopScheduler);
      InMindLoopScheduler.add(RSVPListLoopEnd);
      InMindLoopScheduler.add(KeepInMindRecogRoutineBegin(snapshot));
      InMindLoopScheduler.add(KeepInMindRecogRoutineEachFrame());
      InMindLoopScheduler.add(KeepInMindRecogRoutineEnd(snapshot));
      InMindLoopScheduler.add(judgeRoutineBegin(snapshot));
      InMindLoopScheduler.add(judgeRoutineEachFrame());
      InMindLoopScheduler.add(judgeRoutineEnd(snapshot));
      InMindLoopScheduler.add(InMindLoopEndIteration(InMindLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var RSVPList;
function RSVPListLoopBegin(RSVPListLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    RSVPList = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 62, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'RSVPList'
    });
    psychoJS.experiment.addLoop(RSVPList); // add the loop to the experiment
    currentLoop = RSVPList;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    RSVPList.forEach(function() {
      snapshot = RSVPList.getSnapshot();
    
      RSVPListLoopScheduler.add(importConditions(snapshot));
      RSVPListLoopScheduler.add(ISIRoutineBegin(snapshot));
      RSVPListLoopScheduler.add(ISIRoutineEachFrame());
      RSVPListLoopScheduler.add(ISIRoutineEnd(snapshot));
      RSVPListLoopScheduler.add(RSVP_2RoutineBegin(snapshot));
      RSVPListLoopScheduler.add(RSVP_2RoutineEachFrame());
      RSVPListLoopScheduler.add(RSVP_2RoutineEnd(snapshot));
      RSVPListLoopScheduler.add(RSVPListLoopEndIteration(RSVPListLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function RSVPListLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(RSVPList);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function RSVPListLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function InMindLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(InMind);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function InMindLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var redo;
function redoLoopBegin(redoLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    redo = new TrialHandler({
      psychoJS: psychoJS,
      nReps: nrep, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'redo'
    });
    psychoJS.experiment.addLoop(redo); // add the loop to the experiment
    currentLoop = redo;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    redo.forEach(function() {
      snapshot = redo.getSnapshot();
    
      redoLoopScheduler.add(importConditions(snapshot));
      redoLoopScheduler.add(pretend_redoRoutineBegin(snapshot));
      redoLoopScheduler.add(pretend_redoRoutineEachFrame());
      redoLoopScheduler.add(pretend_redoRoutineEnd(snapshot));
      redoLoopScheduler.add(redoLoopEndIteration(redoLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function redoLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(redo);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function redoLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var shuffle_stimMaxDurationReached;
var shuffle_stimMaxDuration;
var shuffle_stimComponents;
function shuffle_stimRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'shuffle_stim' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    shuffle_stimClock.reset();
    routineTimer.reset();
    shuffle_stimMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from shuffle_code_3
    /* Syntax Error: Fix Python code */
    psychoJS.experiment.addData('shuffle_stim.started', globalClock.getTime());
    shuffle_stimMaxDuration = null
    // keep track of which components have finished
    shuffle_stimComponents = [];
    
    shuffle_stimComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function shuffle_stimRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'shuffle_stim' ---
    // get current time
    t = shuffle_stimClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    shuffle_stimComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function shuffle_stimRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'shuffle_stim' ---
    shuffle_stimComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('shuffle_stim.stopped', globalClock.getTime());
    // the Routine "shuffle_stim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var prepare_markerMaxDurationReached;
var _pj;
var category_list;
var specific_list;
var prepare_markerMaxDuration;
var prepare_markerComponents;
function prepare_markerRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'prepare_marker' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    prepare_markerClock.reset();
    routineTimer.reset();
    prepare_markerMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_3
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    category_list = [];
    for (var i, _pj_c = 0, _pj_a = stimulus_list, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        i = _pj_a[_pj_c];
        if ((i === relpicture)) {
            category_list.push(201);
        } else {
            if (_pj.in_es6(i, ["./img/101.jpg", "./img/102.jpg"])) {
                category_list.push(203);
            } else {
                category_list.push(202);
            }
        }
    }
    specific_list = [];
    for (var i, _pj_c = 0, _pj_a = stimulus_list, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        i = _pj_a[_pj_c];
        if ((i === "./img/101.jpg")) {
            specific_list.push(101);
        } else {
            if ((i === "./img/102.jpg")) {
                specific_list.push(102);
            } else {
                if ((i === "./img/1.jpg")) {
                    specific_list.push(1);
                } else {
                    if ((i === "./img/2.jpg")) {
                        specific_list.push(2);
                    } else {
                        if ((i === "./img/3.jpg")) {
                            specific_list.push(3);
                        } else {
                            if ((i === "./img/4.jpg")) {
                                specific_list.push(4);
                            } else {
                                if ((i === "./img/5.jpg")) {
                                    specific_list.push(5);
                                } else {
                                    specific_list.push(6);
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    psychoJS.experiment.addData('prepare_marker.started', globalClock.getTime());
    prepare_markerMaxDuration = null
    // keep track of which components have finished
    prepare_markerComponents = [];
    
    prepare_markerComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function prepare_markerRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'prepare_marker' ---
    // get current time
    t = prepare_markerClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    prepare_markerComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prepare_markerRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'prepare_marker' ---
    prepare_markerComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('prepare_marker.stopped', globalClock.getTime());
    // the Routine "prepare_marker" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var KeepInMindSlideMaxDurationReached;
var KeepInMindSlideMaxDuration;
var KeepInMindSlideComponents;
function KeepInMindSlideRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'KeepInMindSlide' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    KeepInMindSlideClock.reset(routineTimer.getTime());
    routineTimer.add(1.995000);
    KeepInMindSlideMaxDurationReached = false;
    // update component parameters for each repeat
    KeepInMindSlide_image_1.setImage(relpicture);
    psychoJS.experiment.addData('KeepInMindSlide.started', globalClock.getTime());
    KeepInMindSlideMaxDuration = null
    // keep track of which components have finished
    KeepInMindSlideComponents = [];
    KeepInMindSlideComponents.push(KeepInMindSlide_image_1);
    KeepInMindSlideComponents.push(KeepInMindSlide_text_1);
    
    KeepInMindSlideComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function KeepInMindSlideRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'KeepInMindSlide' ---
    // get current time
    t = KeepInMindSlideClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *KeepInMindSlide_image_1* updates
    if (t >= 0.0 && KeepInMindSlide_image_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      KeepInMindSlide_image_1.tStart = t;  // (not accounting for frame time here)
      KeepInMindSlide_image_1.frameNStart = frameN;  // exact frame index
      
      KeepInMindSlide_image_1.setAutoDraw(true);
    }
    
    
    // if KeepInMindSlide_image_1 is active this frame...
    if (KeepInMindSlide_image_1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.995 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (KeepInMindSlide_image_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      KeepInMindSlide_image_1.tStop = t;  // not accounting for scr refresh
      KeepInMindSlide_image_1.frameNStop = frameN;  // exact frame index
      // update status
      KeepInMindSlide_image_1.status = PsychoJS.Status.FINISHED;
      KeepInMindSlide_image_1.setAutoDraw(false);
    }
    
    
    // *KeepInMindSlide_text_1* updates
    if (t >= 0.0 && KeepInMindSlide_text_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      KeepInMindSlide_text_1.tStart = t;  // (not accounting for frame time here)
      KeepInMindSlide_text_1.frameNStart = frameN;  // exact frame index
      
      KeepInMindSlide_text_1.setAutoDraw(true);
    }
    
    
    // if KeepInMindSlide_text_1 is active this frame...
    if (KeepInMindSlide_text_1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.995 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (KeepInMindSlide_text_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      KeepInMindSlide_text_1.tStop = t;  // not accounting for scr refresh
      KeepInMindSlide_text_1.frameNStop = frameN;  // exact frame index
      // update status
      KeepInMindSlide_text_1.status = PsychoJS.Status.FINISHED;
      KeepInMindSlide_text_1.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    KeepInMindSlideComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function KeepInMindSlideRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'KeepInMindSlide' ---
    KeepInMindSlideComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('KeepInMindSlide.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (KeepInMindSlideMaxDurationReached) {
        KeepInMindSlideClock.add(KeepInMindSlideMaxDuration);
    } else {
        KeepInMindSlideClock.add(1.995000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var test_stimulusMaxDurationReached;
var test_stim;
var correction_choice;
var test_stimulusMaxDuration;
var test_stimulusComponents;
function test_stimulusRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'test_stimulus' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    test_stimulusClock.reset();
    routineTimer.reset();
    test_stimulusMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from test_stimulus_code_3
    test_stim = ["./img/1.jpg", "./img/2.jpg", "./img/3.jpg", "./img/4.jpg", "./img/5.jpg", "./img/6.jpg"];
    util.shuffle(test_stim);
    correction_choice = (util.index(test_stim, relpicture) + 1);
    
    psychoJS.experiment.addData('test_stimulus.started', globalClock.getTime());
    test_stimulusMaxDuration = null
    // keep track of which components have finished
    test_stimulusComponents = [];
    
    test_stimulusComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function test_stimulusRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'test_stimulus' ---
    // get current time
    t = test_stimulusClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    test_stimulusComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function test_stimulusRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'test_stimulus' ---
    test_stimulusComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('test_stimulus.stopped', globalClock.getTime());
    // the Routine "test_stimulus" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var fixationMaxDurationReached;
var fixationMaxDuration;
var fixationComponents;
function fixationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fixation' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    fixationClock.reset(routineTimer.getTime());
    routineTimer.add(0.695000);
    fixationMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('fixation.started', globalClock.getTime());
    fixationMaxDuration = null
    // keep track of which components have finished
    fixationComponents = [];
    fixationComponents.push(fixation_polygon_1);
    
    fixationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function fixationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fixation' ---
    // get current time
    t = fixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation_polygon_1* updates
    if (t >= 0.0 && fixation_polygon_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_polygon_1.tStart = t;  // (not accounting for frame time here)
      fixation_polygon_1.frameNStart = frameN;  // exact frame index
      
      fixation_polygon_1.setAutoDraw(true);
    }
    
    
    // if fixation_polygon_1 is active this frame...
    if (fixation_polygon_1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 0.695 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (fixation_polygon_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      fixation_polygon_1.tStop = t;  // not accounting for scr refresh
      fixation_polygon_1.frameNStop = frameN;  // exact frame index
      // update status
      fixation_polygon_1.status = PsychoJS.Status.FINISHED;
      fixation_polygon_1.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fixationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fixation' ---
    fixationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('fixation.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (fixationMaxDurationReached) {
        fixationClock.add(fixationMaxDuration);
    } else {
        fixationClock.add(0.695000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ISIMaxDurationReached;
var port_sent;
var prot_start;
var ISIMaxDuration;
var ISIComponents;
function ISIRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ISI' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    ISIClock.reset(routineTimer.getTime());
    routineTimer.add(0.095000);
    ISIMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_4
    p_port.setData(0);
    port_sent = false;
    prot_start = null;
    
    psychoJS.experiment.addData('ISI.started', globalClock.getTime());
    ISIMaxDuration = null
    // keep track of which components have finished
    ISIComponents = [];
    ISIComponents.push(ISI_polygon_1);
    
    ISIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var port_srat;
function ISIRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ISI' ---
    // get current time
    t = ISIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ISI_polygon_1* updates
    if (t >= 0.0 && ISI_polygon_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ISI_polygon_1.tStart = t;  // (not accounting for frame time here)
      ISI_polygon_1.frameNStart = frameN;  // exact frame index
      
      ISI_polygon_1.setAutoDraw(true);
    }
    
    
    // if ISI_polygon_1 is active this frame...
    if (ISI_polygon_1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 0.095 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (ISI_polygon_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      ISI_polygon_1.tStop = t;  // not accounting for scr refresh
      ISI_polygon_1.frameNStop = frameN;  // exact frame index
      // update status
      ISI_polygon_1.status = PsychoJS.Status.FINISHED;
      ISI_polygon_1.setAutoDraw(false);
    }
    
    // Run 'Each Frame' code from code_4
    if (((port_sent === false) && (ISI_polygon_1.status === NOT_STARTED))) {
        port_sent = true;
        port_srat = t;
        p_port.setData(specific_list[RSVPList.thisN]);
        psychoJS.experiment.addData("trigger", specific_list[RSVPList.thisN]);
    }
    if (((port_sent === true) && (t > ((port_srat + 0.1) - frameTolerance)))) {
        p_port.setData(0);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ISIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ISIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ISI' ---
    ISIComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('ISI.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (ISIMaxDurationReached) {
        ISIClock.add(ISIMaxDuration);
    } else {
        ISIClock.add(0.095000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var RSVP_2MaxDurationReached;
var port_start;
var RSVP_2MaxDuration;
var RSVP_2Components;
function RSVP_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'RSVP_2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    RSVP_2Clock.reset(routineTimer.getTime());
    routineTimer.add(0.595000);
    RSVP_2MaxDurationReached = false;
    // update component parameters for each repeat
    RSVP_image_1.setImage(stimulus_list[RSVPList.thisN]);
    // Run 'Begin Routine' code from code_5
    p_port.setData(0);
    port_start = null;
    port_sent = false;
    
    psychoJS.experiment.addData('RSVP_2.started', globalClock.getTime());
    RSVP_2MaxDuration = null
    // keep track of which components have finished
    RSVP_2Components = [];
    RSVP_2Components.push(RSVP_image_1);
    
    RSVP_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function RSVP_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'RSVP_2' ---
    // get current time
    t = RSVP_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *RSVP_image_1* updates
    if (t >= 0.0 && RSVP_image_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RSVP_image_1.tStart = t;  // (not accounting for frame time here)
      RSVP_image_1.frameNStart = frameN;  // exact frame index
      
      RSVP_image_1.setAutoDraw(true);
    }
    
    
    // if RSVP_image_1 is active this frame...
    if (RSVP_image_1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 0.595 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (RSVP_image_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      RSVP_image_1.tStop = t;  // not accounting for scr refresh
      RSVP_image_1.frameNStop = frameN;  // exact frame index
      // update status
      RSVP_image_1.status = PsychoJS.Status.FINISHED;
      RSVP_image_1.setAutoDraw(false);
    }
    
    // Run 'Each Frame' code from code_5
    if (((port_sent === false) && (RSVP_image_1.status === NOT_STARTED))) {
        port_sent = true;
        p_port.setData(category_list[RSVPList.thisN]);
        port_start = t;
    }
    if (((port_sent === true) && (t > ((port_start + 0.1) - frameTolerance)))) {
        p_port.setData(0);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    RSVP_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function RSVP_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'RSVP_2' ---
    RSVP_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('RSVP_2.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (RSVP_2MaxDurationReached) {
        RSVP_2Clock.add(RSVP_2MaxDuration);
    } else {
        RSVP_2Clock.add(0.595000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var KeepInMindRecogMaxDurationReached;
var _KeepInMindRecog_key_resp_1_allKeys;
var KeepInMindRecogMaxDuration;
var KeepInMindRecogComponents;
function KeepInMindRecogRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'KeepInMindRecog' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    KeepInMindRecogClock.reset();
    routineTimer.reset();
    KeepInMindRecogMaxDurationReached = false;
    // update component parameters for each repeat
    KeepInMindRecog_image_1.setImage(test_stim[0]);
    KeepInMindRecog_image_2.setImage(test_stim[1]);
    KeepInMindRecog_image_3.setImage(test_stim[2]);
    KeepInMindRecog_image_4.setImage(test_stim[3]);
    KeepInMindRecog_image_5.setImage(test_stim[4]);
    KeepInMindRecog_image_6.setImage(test_stim[5]);
    KeepInMindRecog_key_resp_1.keys = undefined;
    KeepInMindRecog_key_resp_1.rt = undefined;
    _KeepInMindRecog_key_resp_1_allKeys = [];
    psychoJS.experiment.addData('KeepInMindRecog.started', globalClock.getTime());
    KeepInMindRecogMaxDuration = null
    // keep track of which components have finished
    KeepInMindRecogComponents = [];
    KeepInMindRecogComponents.push(KeepInMindRecog_image_1);
    KeepInMindRecogComponents.push(KeepInMindRecog_image_2);
    KeepInMindRecogComponents.push(KeepInMindRecog_image_3);
    KeepInMindRecogComponents.push(KeepInMindRecog_image_4);
    KeepInMindRecogComponents.push(KeepInMindRecog_image_5);
    KeepInMindRecogComponents.push(KeepInMindRecog_image_6);
    KeepInMindRecogComponents.push(KeepInMindRecog_key_resp_1);
    
    KeepInMindRecogComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function KeepInMindRecogRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'KeepInMindRecog' ---
    // get current time
    t = KeepInMindRecogClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *KeepInMindRecog_image_1* updates
    if (t >= 0.0 && KeepInMindRecog_image_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      KeepInMindRecog_image_1.tStart = t;  // (not accounting for frame time here)
      KeepInMindRecog_image_1.frameNStart = frameN;  // exact frame index
      
      KeepInMindRecog_image_1.setAutoDraw(true);
    }
    
    
    // if KeepInMindRecog_image_1 is active this frame...
    if (KeepInMindRecog_image_1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.995 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (KeepInMindRecog_image_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      KeepInMindRecog_image_1.tStop = t;  // not accounting for scr refresh
      KeepInMindRecog_image_1.frameNStop = frameN;  // exact frame index
      // update status
      KeepInMindRecog_image_1.status = PsychoJS.Status.FINISHED;
      KeepInMindRecog_image_1.setAutoDraw(false);
    }
    
    
    // *KeepInMindRecog_image_2* updates
    if (t >= 0.0 && KeepInMindRecog_image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      KeepInMindRecog_image_2.tStart = t;  // (not accounting for frame time here)
      KeepInMindRecog_image_2.frameNStart = frameN;  // exact frame index
      
      KeepInMindRecog_image_2.setAutoDraw(true);
    }
    
    
    // if KeepInMindRecog_image_2 is active this frame...
    if (KeepInMindRecog_image_2.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.995 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (KeepInMindRecog_image_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      KeepInMindRecog_image_2.tStop = t;  // not accounting for scr refresh
      KeepInMindRecog_image_2.frameNStop = frameN;  // exact frame index
      // update status
      KeepInMindRecog_image_2.status = PsychoJS.Status.FINISHED;
      KeepInMindRecog_image_2.setAutoDraw(false);
    }
    
    
    // *KeepInMindRecog_image_3* updates
    if (t >= 0.0 && KeepInMindRecog_image_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      KeepInMindRecog_image_3.tStart = t;  // (not accounting for frame time here)
      KeepInMindRecog_image_3.frameNStart = frameN;  // exact frame index
      
      KeepInMindRecog_image_3.setAutoDraw(true);
    }
    
    
    // if KeepInMindRecog_image_3 is active this frame...
    if (KeepInMindRecog_image_3.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.995 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (KeepInMindRecog_image_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      KeepInMindRecog_image_3.tStop = t;  // not accounting for scr refresh
      KeepInMindRecog_image_3.frameNStop = frameN;  // exact frame index
      // update status
      KeepInMindRecog_image_3.status = PsychoJS.Status.FINISHED;
      KeepInMindRecog_image_3.setAutoDraw(false);
    }
    
    
    // *KeepInMindRecog_image_4* updates
    if (t >= 0.0 && KeepInMindRecog_image_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      KeepInMindRecog_image_4.tStart = t;  // (not accounting for frame time here)
      KeepInMindRecog_image_4.frameNStart = frameN;  // exact frame index
      
      KeepInMindRecog_image_4.setAutoDraw(true);
    }
    
    
    // if KeepInMindRecog_image_4 is active this frame...
    if (KeepInMindRecog_image_4.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.995 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (KeepInMindRecog_image_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      KeepInMindRecog_image_4.tStop = t;  // not accounting for scr refresh
      KeepInMindRecog_image_4.frameNStop = frameN;  // exact frame index
      // update status
      KeepInMindRecog_image_4.status = PsychoJS.Status.FINISHED;
      KeepInMindRecog_image_4.setAutoDraw(false);
    }
    
    
    // *KeepInMindRecog_image_5* updates
    if (t >= 0.0 && KeepInMindRecog_image_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      KeepInMindRecog_image_5.tStart = t;  // (not accounting for frame time here)
      KeepInMindRecog_image_5.frameNStart = frameN;  // exact frame index
      
      KeepInMindRecog_image_5.setAutoDraw(true);
    }
    
    
    // if KeepInMindRecog_image_5 is active this frame...
    if (KeepInMindRecog_image_5.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.995 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (KeepInMindRecog_image_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      KeepInMindRecog_image_5.tStop = t;  // not accounting for scr refresh
      KeepInMindRecog_image_5.frameNStop = frameN;  // exact frame index
      // update status
      KeepInMindRecog_image_5.status = PsychoJS.Status.FINISHED;
      KeepInMindRecog_image_5.setAutoDraw(false);
    }
    
    
    // *KeepInMindRecog_image_6* updates
    if (t >= 0.0 && KeepInMindRecog_image_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      KeepInMindRecog_image_6.tStart = t;  // (not accounting for frame time here)
      KeepInMindRecog_image_6.frameNStart = frameN;  // exact frame index
      
      KeepInMindRecog_image_6.setAutoDraw(true);
    }
    
    
    // if KeepInMindRecog_image_6 is active this frame...
    if (KeepInMindRecog_image_6.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.995 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (KeepInMindRecog_image_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      KeepInMindRecog_image_6.tStop = t;  // not accounting for scr refresh
      KeepInMindRecog_image_6.frameNStop = frameN;  // exact frame index
      // update status
      KeepInMindRecog_image_6.status = PsychoJS.Status.FINISHED;
      KeepInMindRecog_image_6.setAutoDraw(false);
    }
    
    
    // *KeepInMindRecog_key_resp_1* updates
    if (t >= 0.0 && KeepInMindRecog_key_resp_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      KeepInMindRecog_key_resp_1.tStart = t;  // (not accounting for frame time here)
      KeepInMindRecog_key_resp_1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { KeepInMindRecog_key_resp_1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { KeepInMindRecog_key_resp_1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { KeepInMindRecog_key_resp_1.clearEvents(); });
    }
    
    // if KeepInMindRecog_key_resp_1 is active this frame...
    if (KeepInMindRecog_key_resp_1.status === PsychoJS.Status.STARTED) {
      let theseKeys = KeepInMindRecog_key_resp_1.getKeys({
        keyList: typeof ['1','2','3','4','5','6'] === 'string' ? [['1','2','3','4','5','6']] : ['1','2','3','4','5','6'], 
        waitRelease: false
      });
      _KeepInMindRecog_key_resp_1_allKeys = _KeepInMindRecog_key_resp_1_allKeys.concat(theseKeys);
      if (_KeepInMindRecog_key_resp_1_allKeys.length > 0) {
        KeepInMindRecog_key_resp_1.keys = _KeepInMindRecog_key_resp_1_allKeys[_KeepInMindRecog_key_resp_1_allKeys.length - 1].name;  // just the last key pressed
        KeepInMindRecog_key_resp_1.rt = _KeepInMindRecog_key_resp_1_allKeys[_KeepInMindRecog_key_resp_1_allKeys.length - 1].rt;
        KeepInMindRecog_key_resp_1.duration = _KeepInMindRecog_key_resp_1_allKeys[_KeepInMindRecog_key_resp_1_allKeys.length - 1].duration;
        // was this correct?
        if (KeepInMindRecog_key_resp_1.keys == correction_choice) {
            KeepInMindRecog_key_resp_1.corr = 1;
        } else {
            KeepInMindRecog_key_resp_1.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    KeepInMindRecogComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function KeepInMindRecogRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'KeepInMindRecog' ---
    KeepInMindRecogComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('KeepInMindRecog.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (KeepInMindRecog_key_resp_1.keys === undefined) {
      if (['None','none',undefined].includes(correction_choice)) {
         KeepInMindRecog_key_resp_1.corr = 1;  // correct non-response
      } else {
         KeepInMindRecog_key_resp_1.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(KeepInMindRecog_key_resp_1.corr, level);
    }
    psychoJS.experiment.addData('KeepInMindRecog_key_resp_1.keys', KeepInMindRecog_key_resp_1.keys);
    psychoJS.experiment.addData('KeepInMindRecog_key_resp_1.corr', KeepInMindRecog_key_resp_1.corr);
    if (typeof KeepInMindRecog_key_resp_1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('KeepInMindRecog_key_resp_1.rt', KeepInMindRecog_key_resp_1.rt);
        psychoJS.experiment.addData('KeepInMindRecog_key_resp_1.duration', KeepInMindRecog_key_resp_1.duration);
        routineTimer.reset();
        }
    
    KeepInMindRecog_key_resp_1.stop();
    // the Routine "KeepInMindRecog" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var judgeMaxDurationReached;
var feedback;
var font_color;
var judgeMaxDuration;
var judgeComponents;
function judgeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'judge' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    judgeClock.reset(routineTimer.getTime());
    routineTimer.add(1.995000);
    judgeMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from judge_code
    if ((KeepInMindRecog_key_resp_1.corr === 1)) {
        feedback = "congratulation";
        font_color = "green";
    } else {
        feedback = "pity";
        font_color = "red";
    }
    
    judge_text_1.setColor(new util.Color(font_color));
    judge_text_1.setText(feedback);
    psychoJS.experiment.addData('judge.started', globalClock.getTime());
    judgeMaxDuration = null
    // keep track of which components have finished
    judgeComponents = [];
    judgeComponents.push(judge_text_1);
    
    judgeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function judgeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'judge' ---
    // get current time
    t = judgeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *judge_text_1* updates
    if (t >= 0.0 && judge_text_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      judge_text_1.tStart = t;  // (not accounting for frame time here)
      judge_text_1.frameNStart = frameN;  // exact frame index
      
      judge_text_1.setAutoDraw(true);
    }
    
    
    // if judge_text_1 is active this frame...
    if (judge_text_1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.995 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (judge_text_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      judge_text_1.tStop = t;  // not accounting for scr refresh
      judge_text_1.frameNStop = frameN;  // exact frame index
      // update status
      judge_text_1.status = PsychoJS.Status.FINISHED;
      judge_text_1.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    judgeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function judgeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'judge' ---
    judgeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('judge.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (judgeMaxDurationReached) {
        judgeClock.add(judgeMaxDuration);
    } else {
        judgeClock.add(1.995000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var redo_or_notMaxDurationReached;
var acc;
var acc_rate;
var nrep;
var redo_or_notMaxDuration;
var redo_or_notComponents;
function redo_or_notRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'redo_or_not' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    redo_or_notClock.reset();
    routineTimer.reset();
    redo_or_notMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_2
    acc = InMind.data["KeepInMindRecog_key_resp_1.corr"];
    acc_rate = (util.sum(acc) / acc.length);
    if ((acc_rate < 0.6)) {
        nrep = 1;
    } else {
        nrep = 0;
    }
    
    psychoJS.experiment.addData('redo_or_not.started', globalClock.getTime());
    redo_or_notMaxDuration = null
    // keep track of which components have finished
    redo_or_notComponents = [];
    
    redo_or_notComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function redo_or_notRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'redo_or_not' ---
    // get current time
    t = redo_or_notClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    redo_or_notComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function redo_or_notRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'redo_or_not' ---
    redo_or_notComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('redo_or_not.stopped', globalClock.getTime());
    // the Routine "redo_or_not" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var pretend_redoMaxDurationReached;
var pretend_redoMaxDuration;
var pretend_redoComponents;
function pretend_redoRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'pretend_redo' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    pretend_redoClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    pretend_redoMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('pretend_redo.started', globalClock.getTime());
    pretend_redoMaxDuration = null
    // keep track of which components have finished
    pretend_redoComponents = [];
    pretend_redoComponents.push(pretend_redo_text);
    
    pretend_redoComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function pretend_redoRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'pretend_redo' ---
    // get current time
    t = pretend_redoClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *pretend_redo_text* updates
    if (t >= 0.0 && pretend_redo_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pretend_redo_text.tStart = t;  // (not accounting for frame time here)
      pretend_redo_text.frameNStart = frameN;  // exact frame index
      
      pretend_redo_text.setAutoDraw(true);
    }
    
    
    // if pretend_redo_text is active this frame...
    if (pretend_redo_text.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (pretend_redo_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      pretend_redo_text.tStop = t;  // not accounting for scr refresh
      pretend_redo_text.frameNStop = frameN;  // exact frame index
      // update status
      pretend_redo_text.status = PsychoJS.Status.FINISHED;
      pretend_redo_text.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    pretend_redoComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function pretend_redoRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'pretend_redo' ---
    pretend_redoComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('pretend_redo.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (pretend_redoMaxDurationReached) {
        pretend_redoClock.add(pretend_redoMaxDuration);
    } else {
        pretend_redoClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var goodbyeMaxDurationReached;
var _goodbye_keyboard_1_allKeys;
var goodbyeMaxDuration;
var goodbyeComponents;
function goodbyeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'goodbye' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    goodbyeClock.reset();
    routineTimer.reset();
    goodbyeMaxDurationReached = false;
    // update component parameters for each repeat
    goodbye_keyboard_1.keys = undefined;
    goodbye_keyboard_1.rt = undefined;
    _goodbye_keyboard_1_allKeys = [];
    psychoJS.experiment.addData('goodbye.started', globalClock.getTime());
    goodbyeMaxDuration = null
    // keep track of which components have finished
    goodbyeComponents = [];
    goodbyeComponents.push(goodbye_text_1);
    goodbyeComponents.push(goodbye_keyboard_1);
    
    goodbyeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function goodbyeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'goodbye' ---
    // get current time
    t = goodbyeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *goodbye_text_1* updates
    if (t >= 0.0 && goodbye_text_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      goodbye_text_1.tStart = t;  // (not accounting for frame time here)
      goodbye_text_1.frameNStart = frameN;  // exact frame index
      
      goodbye_text_1.setAutoDraw(true);
    }
    
    
    // if goodbye_text_1 is active this frame...
    if (goodbye_text_1.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *goodbye_keyboard_1* updates
    if (t >= 0.0 && goodbye_keyboard_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      goodbye_keyboard_1.tStart = t;  // (not accounting for frame time here)
      goodbye_keyboard_1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { goodbye_keyboard_1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { goodbye_keyboard_1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { goodbye_keyboard_1.clearEvents(); });
    }
    
    // if goodbye_keyboard_1 is active this frame...
    if (goodbye_keyboard_1.status === PsychoJS.Status.STARTED) {
      let theseKeys = goodbye_keyboard_1.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _goodbye_keyboard_1_allKeys = _goodbye_keyboard_1_allKeys.concat(theseKeys);
      if (_goodbye_keyboard_1_allKeys.length > 0) {
        goodbye_keyboard_1.keys = _goodbye_keyboard_1_allKeys[_goodbye_keyboard_1_allKeys.length - 1].name;  // just the last key pressed
        goodbye_keyboard_1.rt = _goodbye_keyboard_1_allKeys[_goodbye_keyboard_1_allKeys.length - 1].rt;
        goodbye_keyboard_1.duration = _goodbye_keyboard_1_allKeys[_goodbye_keyboard_1_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    goodbyeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function goodbyeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'goodbye' ---
    goodbyeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('goodbye.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(goodbye_keyboard_1.corr, level);
    }
    psychoJS.experiment.addData('goodbye_keyboard_1.keys', goodbye_keyboard_1.keys);
    if (typeof goodbye_keyboard_1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('goodbye_keyboard_1.rt', goodbye_keyboard_1.rt);
        psychoJS.experiment.addData('goodbye_keyboard_1.duration', goodbye_keyboard_1.duration);
        routineTimer.reset();
        }
    
    goodbye_keyboard_1.stop();
    // the Routine "goodbye" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
