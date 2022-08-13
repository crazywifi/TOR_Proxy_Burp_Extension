#Created By lazyhacker22.blogspot.com
#Download Tor Windows Expert Bundle (https://www.torproject.org/download/tor/)

try:
    from burp import IBurpExtender
    from burp import ITab
    from javax.swing import (JTable, JScrollPane, JSplitPane, JButton, JPanel,
                             JTextField, JLabel, SwingConstants, JDialog, Box,
                             JCheckBox, JMenuItem, SwingUtilities, JOptionPane,
                             BoxLayout, JPopupMenu, JFileChooser, JTextPane, JFrame, JPanel)
    from java.awt import (Frame, Component, BorderLayout, FlowLayout, Dimension, Color, Font, Cursor)
    from java.net import (URI,URISyntaxException)
    import sys
    import subprocess
    import time
    import os




except ImportError as e:
    print e

operatingsystem = (hasattr(sys, 'getwindowsversion'))


class BurpExtender(IBurpExtender, ITab):


    def	registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        
        self.Lazyhacker22 = JPanel()
        self.Lazyhacker22.layout = BoxLayout(self.Lazyhacker22,BoxLayout.PAGE_AXIS)
        callbacks.setExtensionName("TOR_Proxy")
        print("TOR Proxy Extension is Loaded..")
        print("For Windows: Download Tor Windows Expert Bundle For (https://www.torproject.org/download/tor/)")
        print("For Linux: Install tor by terminal (sudo apt-get install tor).. The path of binary is '/usr/bin/tor'")
        callbacks.addSuiteTab(self)
        

        self.Tor_ProxyPathPanel = JPanel()
        self.myinputbox = JTextField(40)
        self.myinputbox.setText("Enter Tor Binary File Path")
        self.myinputbox.setForeground(Color.GRAY)
        self.submitbuttonbrowse = JButton("Browse", actionPerformed=self.submitbuttonbrowselistener)
        self.submitbutton = JButton("ON", actionPerformed=self.ON)
        self.submitbutton1 = JButton("OFF", actionPerformed=self.OFF)  
        self.Tor_ProxyPathPanel.add(self.myinputbox)
        self.Tor_ProxyPathPanel.add(self.submitbuttonbrowse)
        self.Tor_ProxyPathPanel.add(self.submitbutton)
        self.Tor_ProxyPathPanel.add(self.submitbutton1)
        self.Lazyhacker22.add(self.Tor_ProxyPathPanel)

        self.mylabel = JPanel()
        self.myname = JLabel()
        self.myname.setText("Created By lazyhacker22.blogspot.com (https://lazyhacker22.blogspot.com)")
        self.myname.setCursor(Cursor(Cursor.HAND_CURSOR))
        self.myname.setFont(Font("Serif", Font.BOLD, 20))
        self.myname.setForeground(Color.RED)
        self.mylabel.add(self.myname)
        self.Lazyhacker22.add(self.mylabel)

        
        self.mylabel1 = JPanel()
        self.myname1 = JLabel()
        self.myname1.setFont(Font("Serif", Font.BOLD, 15))
        self.myname1.setForeground(Color.RED)
        self.mylabel1.add(self.myname1)
        self.Lazyhacker22.add(self.mylabel1)

        

    def submitbuttonbrowselistener(self,e):
        chooseFile = JFileChooser()
        chooseFile.setFileSelectionMode(JFileChooser.FILES_ONLY)
        returnedFile = chooseFile.showDialog(self.Lazyhacker22, "TorPath")
        if returnedFile == JFileChooser.APPROVE_OPTION: 
            fileLoad = chooseFile.getSelectedFile()
            self.filepath = fileLoad.getAbsolutePath()
            self.myinputbox.text = self.filepath
            self.myinputbox.setForeground(Color.BLACK)


    def ON(self,e):
        #ON
        self.submitbutton.setBackground(Color.GREEN)
        self.submitbutton1.setBackground(Color.WHITE)
        TorPath = self.myinputbox.getText()

        if operatingsystem is True: 
            try:
                Netstat_cmd = 'netstat -nao | findstr ":9050"'
                port = os.system(Netstat_cmd)
                if port==0:
                    out = "Tor Proxy Is Already Running..Enjoy Your Anonymity.."
                    print(out)
                    self.myname.setText(out)
                    status = "Note: SOCKS Proxy Host (127.0.0.1) and Port (9050). Tick the 'Use SOCKS  Proxy' in User Options"
                    self.myname1.setText(status)
                       
                else:
                    cmd = TorPath
                    #print(cmd)
                    subprocess.Popen(cmd,shell=True)
                    time.sleep(5)
                    port = os.system(Netstat_cmd)
                    if port==0:
                        out = "Tor Proxy Is Started..Enjoy Your Anonymity.."
                        print(out)
                        self.myname.setText(out)
                        status = "Note: SOCKS Proxy Host (127.0.0.1) and Port (9050). Tick the 'Use SOCKS  Proxy' in User Options"
                        self.myname1.setText(status)
                    else:
                        out = "Note: Tor Proxy is not working, Please check the Tor binary is selected or not"
                        print(out)
                        self.myname1.setText(out)

            except Exception as e:
                print(e)

        else:
            try:
                Netstat_cmd = 'netstat -nao | grep ":9050"'
                port = os.system(Netstat_cmd)
                if port==0:
                    out = "Tor Proxy Is Already Running..Enjoy Your Anonymity.."
                    print(out)
                    self.myname.setText(out)
                    status = "Note: SOCKS Proxy Host (127.0.0.1) and Port (9050). Tick the 'Use SOCKS  Proxy' in User Options"
                    self.myname1.setText(status)
                       
                else:
                    cmd = TorPath
                    #print(cmd)
                    subprocess.Popen(cmd,shell=True)
                    time.sleep(5)
                    port = os.system(Netstat_cmd)
                    if port==0:
                        out = "Tor Proxy Is Started..Enjoy Your Anonymity.."
                        print(out)
                        self.myname.setText(out)
                        status = "Note: SOCKS Proxy Host (127.0.0.1) and Port (9050). Tick the 'Use SOCKS  Proxy' in User Options"
                        self.myname1.setText(status)
                    else:
                        out = "Note: Tor Proxy is not working, Please check the Tor binary is selected or not"
                        print(out)
                        self.myname1.setText(out)

            except Exception as e:
                print(e)            
            
        

            


    def OFF(self,e):
        #OFF
        self.submitbutton.setBackground(Color.WHITE)
        self.submitbutton1.setBackground(Color.GREEN)
        #self.myinputbox.text = "OFF"
        TorPath = self.myinputbox.getText()
        
        if operatingsystem is True:  
            try:
                Netstat_cmd = 'netstat -nao | findstr ":9050"'
                port = os.system(Netstat_cmd)
                if port!=0:
                    out= "Tor Proxy Is Already Stoped..Now, Government is watching you :)"
                    print(out)
                    self.myname.setText(out)
                    status = "Note: Untick the 'Use SOCKS  Proxy' in User Options"
                    self.myname1.setText(status)
                else:
                    cmd = "taskkill /IM tor.exe /F"
                    subprocess.Popen(cmd,shell=True)
                    time.sleep(4)
                    port = os.system(Netstat_cmd)
                    if port!=0:
                        out="Tor Proxy Is Stoped..Now, Government is watching you :)"
                        print(out)
                        self.myname.setText(out)
                        status = "Note: Untick the 'Use SOCKS  Proxy' in User Options"
                        self.myname1.setText(status)
                    else:
                        out="Note: Tor Proxy is not working, Please check the logic"
                        print(out)
                        self.myname1.setText(out)
        
            except Exception as e:
                print(e)


        else:
            try:
                Netstat_cmd = 'netstat -nao | grep ":9050"'
                port = os.system(Netstat_cmd)
                if port!=0:
                    out= "Tor Proxy Is Already Stoped..Now, Government is watching you :)"
                    print(out)
                    self.myname.setText(out)
                    status = "Note: Untick the 'Use SOCKS  Proxy' in User Options"
                    self.myname1.setText(status)
                else:
                    cmd = "killall tor"
                    subprocess.Popen(cmd,shell=True)
                    time.sleep(4)
                    port = os.system(Netstat_cmd)
                    if port!=0:
                        out="Tor Proxy Is Stoped..Now, Government is watching you :)"
                        print(out)
                        self.myname.setText(out)
                        status = "Note: Untick the 'Use SOCKS  Proxy' in User Options"
                        self.myname1.setText(status)
                    else:
                        out="Note: Tor Proxy is not working, Please check the logic"
                        print(out)
                        self.myname1.setText(out)
        
            except Exception as e:
                print(e)
            

    def getTabCaption(self):
        return "TOR_Proxy"

    def getUiComponent(self):
        return self.Lazyhacker22

 
