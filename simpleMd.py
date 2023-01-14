import wx

class SimpleMd(wx.App):
    def __init__(self):
        super().__init__()
    def OnInit(self):
        frame = wx.Frame(None, -1, "Simple MD")
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.Editor = wx.TextCtrl(frame, -1, style=wx.TE_MULTILINE)
        self.Editor.Bind(wx.EVT_KEY_DOWN, self.on_key_press)
        self.Editor.Bind(wx.EVT_KEY_DOWN, self.on_enter)
        self.Editor.Bind(wx.EVT_KEY_DOWN, self.on_dash)

        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        new_file = wx.MenuItem(file_menu, wx.ID_NEW, "&New")
        file_menu.Append(wx.ID_NEW, "&New\CTRL+N")
        open_file = wx.MenuItem(file_menu, wx.ID_OPEN, "&Open")
        file_menu.Append(wx.ID_OPEN, "&Open\ctrl+O")
        save_file = wx.MenuItem(file_menu, wx.ID_SAVE, "&Save")
        file_menu.Append(wx.ID_SAVE, "&Save\ctrl+S")
        save_file_as = wx.MenuItem(file_menu, wx.ID_SAVEAS, "Save &As")
        file_menu.Append(wx.ID_SAVEAS, "Save &As\ctrl+shift+S")
        file_menu.AppendSeparator()
        exit_item= wx.MenuItem(file_menu, wx.ID_EXIT, "&Exit")
        file_menu.Append(wx.ID_EXIT, "&Exit\ALT+F4")
        menu_bar.Append(file_menu, "&File")
        # self.Bind(wx.EVT_MENU, self.OnNew, id=wx.ID_NEW)
        self.Bind(wx.EVT_MENU, self.OnOpen, id=wx.ID_OPEN)
        self.Bind(wx.EVT_MENU, self.OnSave, id=wx.ID_SAVE)
        self.Bind(wx.EVT_MENU, self.OnSaveAs, id=wx.ID_SAVEAS)

        edit_menu = wx.Menu()
        edit_menu.Append(wx.ID_UNDO, "&Undo\ctrl+Z")
        edit_menu.Append(wx.ID_REDO, "&Redo\CTRL+Y")
        edit_menu.AppendSeparator()
        edit_menu.Append(wx.ID_CUT, "Cu&t")
        edit_menu.Append(wx.ID_COPY, "&Copy\ctrl+C")
        edit_menu.Append(wx.ID_PASTE, "&Paste\ctrl+V")
        edit_menu.Append(wx.ID_DELETE, "&Delete\DEL")
        edit_menu.AppendSeparator()
        edit_menu.Append(wx.ID_SELECTALL, "Select &All\ctrl+A")
        menu_bar.Append(edit_menu, "&Edit")

        format_menu = wx.Menu()
        heading_1 = format_menu.Append(wx.ID_ANY, "Heading 1\tCtrl+1", "Insert a heading 1")
        heading_2 = format_menu.Append(wx.ID_ANY, "Heading 2\tCtrl+2", "Insert a heading 2")
        heading_3 = format_menu.Append(wx.ID_ANY, "Heading 3\tCtrl+3", "Insert a heading 3")
        heading_4 = format_menu.Append(wx.ID_ANY, "Heading 4\tCtrl+4", "Insert a heading 4")
        heading_5 = format_menu.Append(wx.ID_ANY, "Heading 5\tCtrl+5", "Insert a heading 5")
        heading_6 = format_menu.Append(wx.ID_ANY, "Heading 6\tCtrl+6", "Insert a heading 6")
        format_menu.AppendSeparator()
        bold_text = format_menu.Append(wx.ID_ANY, "Bold\tCtrl+B", "Insert bold text")
        italic_text = format_menu.Append(wx.ID_ANY, "Italic\tCtrl+I", "Insert italic text")
        format_menu.AppendSeparator()
        unordered_list = format_menu.Append(wx.ID_ANY, "Unordered List\tCtrl+U", "Insert an unordered list")
        ordered_list = format_menu.Append(wx.ID_ANY, "Ordered List\tCtrl+SHIFT+O", "Insert an ordered list")
        format_menu.AppendSeparator()
        blockquote = format_menu.Append(wx.ID_ANY, "Blockquote\tCtrl+Q", "Insert a blockquote")
        code_block = format_menu.Append(wx.ID_ANY, "Code Block\tCtrl+K", "Insert a code block")
        format_menu.AppendSeparator()
        link = format_menu.Append(wx.ID_ANY, "Link\tCtrl+L", "Insert a link")
        image = format_menu.Append(wx.ID_ANY, "Image\tCtrl+G", "Insert an image")
        self.Bind(wx.EVT_MENU, self.on_unordered_list, unordered_list)
        self.Bind(wx.EVT_MENU, self.on_ordered_list, ordered_list)
        self.Bind(wx.EVT_MENU, self.on_italic, italic_text)
        self.Bind(wx.EVT_MENU, self.on_bold, bold_text)
        self.Bind(wx.EVT_MENU, self.on_heading_1, heading_1)
        self.Bind(wx.EVT_MENU, self.on_heading2, heading_2)
        self.Bind(wx.EVT_MENU, self.on_heading3, heading_3)
        self.Bind(wx.EVT_MENU, self.on_heading4, heading_4)
        self.Bind(wx.EVT_MENU, self.on_heading5, heading_5)
        self.Bind(wx.EVT_MENU, self.on_heading6, heading_6)

        menu_bar.Append(format_menu, "&Format")
        frame.SetMenuBar(menu_bar)
        sizer.Add(self.Editor, 1, wx.EXPAND)
        frame.Show()
        frame.SetSizer(sizer)
        frame.Fit()
        return True

    def on_unordered_list(self, event=None):
        self.Editor.WriteText("- ")
        self.is_list = True
    def on_dash(self, event):
        if event.GetKeyCode() == wx.WXK_RETURN and self.is_list and event.ShiftDown():
            self.is_list = False
            self.Editor.WriteText("\n")
        elif event.GetKeyCode() == wx.WXK_RETURN and self.is_list:
            self.Editor.WriteText("\n- ")
        else:
            event.Skip()


    def on_ordered_list(self, event=None):
        self.Editor.WriteText("1. ")
        self.list_count = 2
    def on_enter(self, event):
        if event.GetKeyCode() == wx.WXK_RETURN and self.list_count > 0 and event.ShiftDown():
            self.list_count = 0
            self.Editor.WriteText("\n")
        elif event.GetKeyCode() == wx.WXK_RETURN and self.list_count > 0:
            self.Editor.WriteText("\n" + str(self.list_count) + ". ")
            self.list_count += 1
        else:
            event.Skip()

    def on_italic(self, event=None):
        self.Editor.WriteText("*")
    def on_bold(self, event=None):
        self.Editor.WriteText("**")
    def on_key_press(self, event):
        if event.GetKeyCode() == ord('1') and event.ControlDown():
            self.on_heading_1()
        else:
            event.Skip()
    
    def on_heading_1(self, event=None):
        self.Editor.WriteText("# ")

    def on_heading2(self, event=None):
        self.Editor.WriteText("## ")

    def on_heading3(self, event=None):
        self.Editor.WriteText("### ")

    def on_heading4(self, event=None):
        self.Editor.WriteText("#### ")

    def on_heading5(self, event=None):
        self.Editor.WriteText("##### ")

    def on_heading6(self, event=None):
        self.Editor.WriteText("###### ")


    def OnSaveAs(self, event):
        save_file_dialog = wx.FileDialog(None, "Save File As", "", "", "*.*", wx.FD_SAVE)
        if save_file_dialog.ShowModal() == wx.ID_OK:
            save_file_name = save_file_dialog.GetPath()
            save_file_dialog.Destroy()
            save_file = open(save_file_name, "w")
            save_file.write(editor.GetValue())
            save_file.close()


    def OnOpen(self, event):
        open_file_dialog = wx.FileDialog(None, "Open File", "", "", "*.*", wx.FD_OPEN)
        if open_file_dialog.ShowModal() == wx.ID_OK:
            open_file_name = open_file_dialog.GetPath()
            open_file_dialog.Destroy()
            open_file = open(open_file_name, "r")
            open_file_contents = open_file.read()
            open_file.close()
            editor.SetValue(open_file_contents)
    def OnSave(self, event):
        save_file_dialog = wx.FileDialog(None, "Save File", "", "", "*.*", wx.FD_SAVE)
        if save_file_dialog.ShowModal() == wx.ID_OK:
            save_file_name = save_file_dialog.GetPath()
            save_file_dialog.Destroy()
            save_file = open(save_file_name, "w")
            save_file.write(editor.GetValue())
            save_file.close()
if __name__ == "__main__":
    app = SimpleMd()
    app.MainLoop()
