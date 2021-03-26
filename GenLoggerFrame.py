# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.1 on Fri Mar 19 10:57:37 2021
#

import wx
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


from queue import Queue
from LabJackHandler import *
from PlotGraph import *
import time
import math
import numpy as np

class GenLoggerFrame(wx.Frame):
    __CHANNELS          = [ "AIN0", "AIN1" ]
    # __FREQ_LIMIT        = 3000.0
    __FREQ_LIMIT        = 600.0
    # __FREQ_LIMIT        = 300.0
    __SCAN_RATE         = 2*__FREQ_LIMIT   # Resolve up to 300Hz
    __NUM_CHANNELS      = len(__CHANNELS)

    def __init__(self, *args, **kwds):
        # begin wxGlade: GenLoggerFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((1044, 646))
        self.SetTitle("Generator Test")

        self.mainPanel = wx.Panel(self, wx.ID_ANY)
        self.mainPanel.SetMinSize((1024, 800))

        mainSizer = wx.FlexGridSizer(3, 1, 0, 0)

        self.configSizer = wx.FlexGridSizer(1, 8, 0, 8)
        mainSizer.Add(self.configSizer, 1, wx.ALL | wx.EXPAND, 5)

        self.portCombo = wx.ComboBox(self.mainPanel, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.configSizer.Add(self.portCombo, 0, wx.EXPAND, 0)

        self.refreshButton = wx.Button(self.mainPanel, wx.ID_ANY, "Rescan Channels")
        self.configSizer.Add(self.refreshButton, 0, 0, 0)

        self.startButton = wx.Button(self.mainPanel, wx.ID_ANY, "Start")
        self.configSizer.Add(self.startButton, 0, 0, 0)

        self.stopButton = wx.Button(self.mainPanel, wx.ID_ANY, "Stop")
        self.configSizer.Add(self.stopButton, 0, 0, 0)

        self.startlogButton = wx.Button(self.mainPanel, wx.ID_ANY, "Start Log")
        self.configSizer.Add(self.startlogButton, 0, 0, 0)

        self.stoplogButton = wx.Button(self.mainPanel, wx.ID_ANY, "Stop Log")
        self.configSizer.Add(self.stoplogButton, 0, 0, 0)

        self.loggingStatus = wx.StaticText(self.mainPanel, wx.ID_ANY, "[Logging]")
        self.loggingStatus.Hide()
        self.configSizer.Add(self.loggingStatus, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.gentestFrame = wx.Button(self.mainPanel, wx.ID_ANY, "Exit")
        self.configSizer.Add(self.gentestFrame, 0, 0, 0)

        plotSizer = wx.FlexGridSizer(2, 1, 0, 0)
        mainSizer.Add(plotSizer, 1, wx.ALL | wx.EXPAND, 0)

        self.frequencySizer = wx.FlexGridSizer(2, 1, 0, 0)
        plotSizer.Add(self.frequencySizer, 1, wx.ALL | wx.EXPAND, 0)

        titleFrequencySizer = wx.FlexGridSizer(1, 7, 0, 0)
        self.frequencySizer.Add(titleFrequencySizer, 1, wx.EXPAND, 0)

        self.enableFFTCheckbox1 = wx.CheckBox(self.mainPanel, wx.ID_ANY, "Phase 1")
        self.enableFFTCheckbox1.SetValue(1)
        titleFrequencySizer.Add(self.enableFFTCheckbox1, 0, 0, 0)

        self.enableFFTCheckbox2 = wx.CheckBox(self.mainPanel, wx.ID_ANY, "Phase 2")
        self.enableFFTCheckbox2.SetValue(1)
        titleFrequencySizer.Add(self.enableFFTCheckbox2, 0, 0, 0)

        label_1 = wx.StaticText(self.mainPanel, wx.ID_ANY, "Frequency FFT")
        titleFrequencySizer.Add(label_1, 0, wx.ALIGN_CENTER, 0)

        label_3 = wx.StaticText(self.mainPanel, wx.ID_ANY, "THD Phase1:")
        titleFrequencySizer.Add(label_3, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.frequencyTHDtext1 = wx.TextCtrl(self.mainPanel, wx.ID_ANY, "")
        titleFrequencySizer.Add(self.frequencyTHDtext1, 0, 0, 0)

        label_4 = wx.StaticText(self.mainPanel, wx.ID_ANY, "THD Phase2")
        titleFrequencySizer.Add(label_4, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.frequencyTHDtext2 = wx.TextCtrl(self.mainPanel, wx.ID_ANY, "")
        titleFrequencySizer.Add(self.frequencyTHDtext2, 0, 0, 0)

        self.dummyFrequencyPanel = wx.Panel(self.mainPanel, wx.ID_ANY)
        self.frequencySizer.Add(self.dummyFrequencyPanel, 1, wx.EXPAND, 0)

        self.graphSizer = wx.FlexGridSizer(2, 1, 0, 0)
        plotSizer.Add(self.graphSizer, 1, wx.ALL | wx.EXPAND, 0)

        titleGraphSizer = wx.FlexGridSizer(1, 3, 0, 0)
        self.graphSizer.Add(titleGraphSizer, 1, wx.EXPAND, 0)

        self.enableGraphCheckbox1 = wx.CheckBox(self.mainPanel, wx.ID_ANY, "Phase 1")
        self.enableGraphCheckbox1.SetValue(1)
        titleGraphSizer.Add(self.enableGraphCheckbox1, 0, 0, 0)

        self.enableGraphCheckbox2 = wx.CheckBox(self.mainPanel, wx.ID_ANY, "Phase 2")
        self.enableGraphCheckbox2.SetValue(1)
        titleGraphSizer.Add(self.enableGraphCheckbox2, 0, 0, 0)

        label_2 = wx.StaticText(self.mainPanel, wx.ID_ANY, "Graph")
        titleGraphSizer.Add(label_2, 0, wx.ALIGN_CENTER, 0)

        self.dummyGraphPanel = wx.Panel(self.mainPanel, wx.ID_ANY)
        self.graphSizer.Add(self.dummyGraphPanel, 1, wx.EXPAND, 0)

        mainSizer.Add((20, 20), 0, 0, 0)

        titleGraphSizer.AddGrowableCol(2)

        self.graphSizer.AddGrowableRow(1)
        self.graphSizer.AddGrowableCol(0)

        titleFrequencySizer.AddGrowableCol(2)

        self.frequencySizer.AddGrowableRow(1)
        self.frequencySizer.AddGrowableCol(0)

        plotSizer.AddGrowableRow(0)
        plotSizer.AddGrowableRow(1)
        plotSizer.AddGrowableCol(0)

        self.configSizer.AddGrowableCol(0)

        mainSizer.AddGrowableRow(1)
        mainSizer.AddGrowableCol(0)
        self.mainPanel.SetSizer(mainSizer)

        self.Layout()

        self.Bind(wx.EVT_COMBOBOX, self.OnSelectLabjackCombo, self.portCombo)
        self.Bind(wx.EVT_BUTTON, self.OnRefreshPorts, self.refreshButton)
        self.Bind(wx.EVT_BUTTON, self.OnStartButton, self.startButton)
        self.Bind(wx.EVT_BUTTON, self.OnStopButton, self.stopButton)
        self.Bind(wx.EVT_BUTTON, self.OnStartLogButton, self.startlogButton)
        self.Bind(wx.EVT_BUTTON, self.OnStopLogButton, self.stoplogButton)
        self.Bind(wx.EVT_BUTTON, self.OnExitButton, self.gentestFrame)
        self.Bind(wx.EVT_CHECKBOX, self.OnFFTCheckbox1, self.enableFFTCheckbox1)
        self.Bind(wx.EVT_CHECKBOX, self.OnFFTCheckbox2, self.enableFFTCheckbox2)
        self.Bind(wx.EVT_CHECKBOX, self.OnGraphCheckbox1, self.enableGraphCheckbox1)
        self.Bind(wx.EVT_CHECKBOX, self.OnGraphCheckbox2, self.enableGraphCheckbox2)
        self.Bind(wx.EVT_CLOSE, self.OnClose, self)
        # end wxGlade

        self.__labjack_port = None
        self.__labjack = None
        self.__plotitems = []
        self.__packet_thread_id = None
        self.__queue = Queue()
        self.__log_file = None

        wx.CallLater(2000, self.OnRefreshPortsHelper)

        # Create FFT views
        phase_fft = PlotGraph(parent=self.mainPanel, name="Freq FFT", style=0)
        phase_fft.SetParams({
            "plottype": "fft",
            "points": self.__SCAN_RATE,
            "xmin": 0,
            "xmax": self.__FREQ_LIMIT,
            "ymin": -20,
            "ymax": 80,
            "yconvert": lambda y: 10*math.log10(y) if y != 0 else 0,
            "zero": 1,
            "results":  "thd",  # Return THD from each fft SetValue
        })

        phase_fft.SetChannelColor("AIN0", wx.RED)
        phase_fft.SetChannelColor("AIN1", wx.BLUE)

        self.__plotitems.append(phase_fft)

        self.frequencySizer.Detach(self.dummyFrequencyPanel)
        self.frequencySizer.Add(phase_fft, proportion=1, border=0, flag=wx.EXPAND)

        # Create freq plot
        freq_plot = PlotGraph(parent=self.mainPanel, name="Frequency", style=0)
        freq_plot.SetParams({
            "points": self.__FREQ_LIMIT,
            "xmin": 0,
            "xmax": self.__FREQ_LIMIT,
            "ymin": -20,
            "ymax": 20,
            "xlabelfun": lambda x: "%.2f" % (x/self.__SCAN_RATE),
        })

        freq_plot.SetChannelColor("AIN0", wx.RED)
        freq_plot.SetChannelColor("AIN1", wx.BLUE)

        self.__plotitems.append(freq_plot)

        self.graphSizer.Detach(self.dummyGraphPanel)
        self.graphSizer.Add(freq_plot, proportion=1, border=0, flag=wx.EXPAND)

    def OnRefreshPorts(self, event):  # wxGlade: GenLoggerFrame.<event_handler>
        self.OnRefreshPortsHelper()
        event.Skip()

    def OnRefreshPortsHelper(self):
        busy = wx.BusyCursor()

        self.portCombo.Clear()
        item = 0
        labjacks = GetLabJackHandler().AvailableDevices(force=True)
        for sn in labjacks:
            for connection in labjacks[sn]['connections']:
                self.portCombo.Insert("%s:%s" % (sn, connection), item)

        if self.portCombo.GetSelection() == wx.NOT_FOUND and self.portCombo.GetCount() != 0:
            self.portCombo.SetValue(self.portCombo.GetString(0))

        del busy

    def OnSelectLabjackCombo(self, event):  # wxGlade: GenLoggerFrame.<event_handler>
        event.Skip()

    def OnStartButton(self, event):  # wxGlade: GenLoggerFrame.<event_handler>
        selected = self.portCombo.GetValue()

        if selected is not None:
            sn, connection = selected.split(':')

            self.__labjack = GetLabJackHandler().Open(sn, connection=connection)
            self.__data = {}

            # Start the collector
            rc = self.__labjack.StreamStart(channels=self.__CHANNELS, scan_rate=self.__SCAN_RATE, scans_per_read=int(self.__SCAN_RATE/self.__NUM_CHANNELS), callback=self.__capture_data)
            # print("StreamStart returned %d" % rc)

            if rc != 0:
                self.__timestamp = None
                self.__pointcount = 0
                self.__packet_thread_id = Thread(target=self.__packet_thread)
                self.__packet_thread_id.start()
            else:
                wx.MessageBox(u"Unable to start packet thread", u"Packet Thread")

        event.Skip()

    def __capture_data(self, handle, data):
##        # One complete line cycle that is at 60 Hz
##        times=np.linspace(-5, 5, int(self.__SCAN_RATE * 2))
##        signal=np.sin(times * np.pi * 2)
##        phases = []
##        phase_index = 0
##
##        # Create one scan_rate set of data
##        for point in range(int(self.__SCAN_RATE)):
##            # Two points for AIN0 and AIN1
##            phases.append(signal[phase_index])
##            phases.append(-signal[phase_index])
##            phase_index = (phase_index + 1) % len(signal)
##
##        self.__queue.put([phases, 0])
##        print("phases len %d" % len(phases))
##        return

        self.__queue.put(data)

##        if data is not None:
##            self.__pointcount += len(data[0])
##
##            if self.__timestamp is None:
##                self.__timestamp = time.time()
##            else:
##                now = time.time()
##                elapsed = now - self.__timestamp
##                # print("%.4f points per second (%d)" % (self.__pointcount / elapsed, len(data[0])))

    # This receives the data packets from the LabJack Streams
    def __packet_thread(self):
        running = True
        while running:
            packet = self.__queue.get()
            if packet is None:
                # All done - shut down
                running = False

            else:
                data = packet[0]

                # Send the two channels to the plots
                if self.enableFFTCheckbox1.IsChecked():
                    results = self.__plotitems[0].SetValue([ data[n] for n in range(0, len(data), 2) ], channel="AIN0")
                    if "thd" in results:
                        wx.CallAfter(self.frequencyTHDtext1.SetValue, "%.1f" % results["thd"])

                if self.enableFFTCheckbox2.IsChecked():
                    results = self.__plotitems[0].SetValue([ data[n] for n in range(1, len(data), 2) ], channel="AIN1")
                    if "thd" in results:
                        wx.CallAfter(self.frequencyTHDtext2.SetValue, "%.1f" % results["thd"])

                if self.enableGraphCheckbox1.IsChecked():
                    self.__plotitems[1].SetValue([ data[n] for n in range(0, len(data), 2) ], channel="AIN0")

                if self.enableGraphCheckbox2.IsChecked():
                    self.__plotitems[1].SetValue([ data[n] for n in range(1, len(data), 2) ], channel="AIN1")

                # Send data to log file if requested
                if self.__log_file is not None:
                    for index in range(0, len(data), 2):
                        self.__log_file.write("%.4f,%.4f\n" % (data[index], data[index+1]))

    def OnStopButton(self, event):  # wxGlade: GenLoggerFrame.<event_handler>
        self.StopCapture()
        event.Skip()

    def StopCapture(self):
        if self.__labjack is not None and self.__packet_thread_id is not None:
            self.__labjack.StreamStop()
            self.__packet_thread_id.join()
            self.__packet_thread_id = None

    def OnExitButton(self, event):  # wxGlade: GenLoggerFrame.<event_handler>
        self.CloseLogger()
        wx.Exit()
        event.Skip()

    def CloseLogger(self):
        # print("CloseLogger...")
        self.StopCapture()

        for plotitem in self.__plotitems:
            plotitem.Stop()

        if self.__labjack != None:
            self.__labjack.Close()
            self.__labjack = None

    def OnClose(self, event):  # wxGlade: GenLoggerFrame.<event_handler>
        self.CloseLogger()
        event.Skip()

    def OnFFTCheckbox1(self, event):  # wxGlade: GenLoggerFrame.<event_handler>
        self.__plotitems[0].DeleteChannel(self.__CHANNELS[0])
        self.frequencyTHDtext1.Clear()
        event.Skip()

    def OnFFTCheckbox2(self, event):  # wxGlade: GenLoggerFrame.<event_handler>
        self.__plotitems[0].DeleteChannel(self.__CHANNELS[1])
        self.frequencyTHDtext2.Clear()
        event.Skip()

    def OnGraphCheckbox1(self, event):  # wxGlade: GenLoggerFrame.<event_handler>
        self.__plotitems[1].DeleteChannel(self.__CHANNELS[0])
        event.Skip()

    def OnGraphCheckbox2(self, event):  # wxGlade: GenLoggerFrame.<event_handler>
        self.__plotitems[1].DeleteChannel(self.__CHANNELS[1])
        event.Skip()

    def OnStartLogButton(self, event):  # wxGlade: GenLoggerFrame.<event_handler>
        if self.__log_file is not None:
            with wx.MessageDialog(self, u"Already Logging.  Replace current log file?", caption=u"Close Current Log File", style=wx.CENTER | wx.YES | wx.CANCEL) as question:
                if question.showModal() == wx.ID_YES:
                    self.__log_file.close()
                    self.__log_file = None

        if self.__log_file == None:
            with wx.FileDialog(self, "Create log file", wildcard="LOG files (*.log)|*.log",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

                if fileDialog.ShowModal() != wx.ID_CANCEL:
                    # save the current contents in the file
                    pathname = fileDialog.GetPath()
                    try:
                        self.__log_file = open(pathname, "w+")
                        # Put date/time in comment
                        self.__log_file.write(u",,Started %s\n" % str(wx.DateTime.Now()))
                        self.loggingStatus.Show()
                        self.configSizer.Layout()

                    except IOError:
                        wx.LogError("Cannot log to file '%s'." % pathname)

        event.Skip()

    def OnStopLogButton(self, event):  # wxGlade: GenLoggerFrame.<event_handler>
        if self.__log_file is not None:
            self.__log_file.close()
            self.__log_file = None
            self.loggingStatus.Hide()
            self.configSizer.Layout()

        event.Skip()
# end of class GenLoggerFrame
