#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Spectrum
# Generated: Thu Mar 17 14:26:56 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import sip
import sys
import threading
import time


class spectrum(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Spectrum")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Spectrum")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "spectrum")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.function_3 = function_3 = 0
        self.function_2 = function_2 = 0
        self.function_1 = function_1 = 0
        self.variable_qtgui_label_0_1 = variable_qtgui_label_0_1 = function_3
        self.variable_qtgui_label_0_0 = variable_qtgui_label_0_0 = function_1
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = function_2
        self.samp_rate = samp_rate = 1e6
        self.frequency_rx = frequency_rx = 476.0e6

        ##################################################
        # Blocks
        ##################################################
        self.probe_signal_2 = blocks.probe_signal_f()
        self.probe_signal_1 = blocks.probe_signal_f()
        self.avg_mag_sqrd = analog.probe_avg_mag_sqrd_c(0, 1)
        self._variable_qtgui_label_0_1_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._variable_qtgui_label_0_1_formatter = None
        else:
          self._variable_qtgui_label_0_1_formatter = lambda x: x
        
        self._variable_qtgui_label_0_1_tool_bar.addWidget(Qt.QLabel("variable_qtgui_label_0_1"+": "))
        self._variable_qtgui_label_0_1_label = Qt.QLabel(str(self._variable_qtgui_label_0_1_formatter(self.variable_qtgui_label_0_1)))
        self._variable_qtgui_label_0_1_tool_bar.addWidget(self._variable_qtgui_label_0_1_label)
        self.top_layout.addWidget(self._variable_qtgui_label_0_1_tool_bar)
          
        self._variable_qtgui_label_0_0_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._variable_qtgui_label_0_0_formatter = None
        else:
          self._variable_qtgui_label_0_0_formatter = lambda x: x
        
        self._variable_qtgui_label_0_0_tool_bar.addWidget(Qt.QLabel("variable_qtgui_label_0_0"+": "))
        self._variable_qtgui_label_0_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_0_formatter(self.variable_qtgui_label_0_0)))
        self._variable_qtgui_label_0_0_tool_bar.addWidget(self._variable_qtgui_label_0_0_label)
        self.top_layout.addWidget(self._variable_qtgui_label_0_0_tool_bar)
          
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._variable_qtgui_label_0_formatter = None
        else:
          self._variable_qtgui_label_0_formatter = lambda x: x
        
        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel("variable_qtgui_label_0"+": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.top_layout.addWidget(self._variable_qtgui_label_0_tool_bar)
          
        self.single_pole_iir_filter_xx_0 = filter.single_pole_iir_filter_ff(0.05, 1)
        self.qtgui_number_sink_0_0 = qtgui.number_sink(
                gr.sizeof_float,
                0,
                qtgui.NUM_GRAPH_VERT,
        	1
        )
        self.qtgui_number_sink_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0.set_title("Power")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                  "", "", "", "", ""]
        colors = [("blue", "red"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0.set_min(i, -20)
            self.qtgui_number_sink_0_0.set_max(i, 2)
            self.qtgui_number_sink_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_0_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
                gr.sizeof_float,
                0.10,
                qtgui.NUM_GRAPH_VERT,
        	1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("Power")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                  "", "", "", "", ""]
        colors = [("blue", "red"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, 0)
            self.qtgui_number_sink_0.set_max(i, 2)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	frequency_rx, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if complex == type(float()):
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.osmosdr_source = osmosdr.source( args="numchan=" + str(1) + " " + "bladerf=0" )
        self.osmosdr_source.set_sample_rate(samp_rate)
        self.osmosdr_source.set_center_freq(frequency_rx, 0)
        self.osmosdr_source.set_freq_corr(0, 0)
        self.osmosdr_source.set_dc_offset_mode(0, 0)
        self.osmosdr_source.set_iq_balance_mode(2, 0)
        self.osmosdr_source.set_gain_mode(False, 0)
        self.osmosdr_source.set_gain(3, 0)
        self.osmosdr_source.set_if_gain(0, 0)
        self.osmosdr_source.set_bb_gain(20, 0)
        self.osmosdr_source.set_antenna("", 0)
        self.osmosdr_source.set_bandwidth(6e6, 0)
          
        self.nlog10_ff = blocks.nlog10_ff(10, 1, 0)
        def _function_3_probe():
            while True:
                val = self.probe_signal_2.level()
                try:
                    self.set_function_3(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _function_3_thread = threading.Thread(target=_function_3_probe)
        _function_3_thread.daemon = True
        _function_3_thread.start()
        def _function_2_probe():
            while True:
                val = self.avg_mag_sqrd.level()
                try:
                    self.set_function_2(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _function_2_thread = threading.Thread(target=_function_2_probe)
        _function_2_thread.daemon = True
        _function_2_thread.start()
        def _function_1_probe():
            while True:
                val = self.probe_signal_1.level()
                try:
                    self.set_function_1(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _function_1_thread = threading.Thread(target=_function_1_probe)
        _function_1_thread.daemon = True
        _function_1_thread.start()
        self.blocks_keep_one_in_n = blocks.keep_one_in_n(gr.sizeof_float*1, int(samp_rate / 30))
        self.blocks_complex_to_mag_squared_0_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.probe_signal_1, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.qtgui_number_sink_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0_0_0, 0), (self.single_pole_iir_filter_xx_0, 0))    
        self.connect((self.blocks_keep_one_in_n, 0), (self.nlog10_ff, 0))    
        self.connect((self.nlog10_ff, 0), (self.probe_signal_2, 0))    
        self.connect((self.nlog10_ff, 0), (self.qtgui_number_sink_0_0, 0))    
        self.connect((self.osmosdr_source, 0), (self.avg_mag_sqrd, 0))    
        self.connect((self.osmosdr_source, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.osmosdr_source, 0), (self.blocks_complex_to_mag_squared_0_0_0, 0))    
        self.connect((self.osmosdr_source, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.single_pole_iir_filter_xx_0, 0), (self.blocks_keep_one_in_n, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "spectrum")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_function_3(self):
        return self.function_3

    def set_function_3(self, function_3):
        self.function_3 = function_3
        self.set_variable_qtgui_label_0_1(self._variable_qtgui_label_0_1_formatter(self.function_3))

    def get_function_2(self):
        return self.function_2

    def set_function_2(self, function_2):
        self.function_2 = function_2
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(self.function_2))

    def get_function_1(self):
        return self.function_1

    def set_function_1(self, function_1):
        self.function_1 = function_1
        self.set_variable_qtgui_label_0_0(self._variable_qtgui_label_0_0_formatter(self.function_1))

    def get_variable_qtgui_label_0_1(self):
        return self.variable_qtgui_label_0_1

    def set_variable_qtgui_label_0_1(self, variable_qtgui_label_0_1):
        self.variable_qtgui_label_0_1 = variable_qtgui_label_0_1
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_1_label, "setText", Qt.Q_ARG("QString", str(self.variable_qtgui_label_0_1)))

    def get_variable_qtgui_label_0_0(self):
        return self.variable_qtgui_label_0_0

    def set_variable_qtgui_label_0_0(self, variable_qtgui_label_0_0):
        self.variable_qtgui_label_0_0 = variable_qtgui_label_0_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_0_label, "setText", Qt.Q_ARG("QString", str(self.variable_qtgui_label_0_0)))

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", str(self.variable_qtgui_label_0)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_keep_one_in_n.set_n(int(self.samp_rate / 30))
        self.osmosdr_source.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.frequency_rx, self.samp_rate)

    def get_frequency_rx(self):
        return self.frequency_rx

    def set_frequency_rx(self, frequency_rx):
        self.frequency_rx = frequency_rx
        self.osmosdr_source.set_center_freq(self.frequency_rx, 0)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.frequency_rx, self.samp_rate)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = spectrum()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets
