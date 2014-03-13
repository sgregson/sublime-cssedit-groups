import sublime, sublime_plugin, re

class CssGroupsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.groups = []
        self.view.find_all("/[\*\s ]*\n[\*\s ]*(.*)[\*\s ]*\n[\*\s ]*/$", 0, "$1", self.groups) #contents of comment block
        self.view.window().show_quick_panel(self.groups, self.goto_group, sublime.MONOSPACE_FONT)

    def goto_group(self, choice):
        if choice == -1:
            return

        group = self.groups[choice]
        jump_location = self.view.find("/\**\n[\*\s]*" + re.escape(group) + "[\*\s]*\n\**/$", 0) # handle duplicates of search term

        self.view.sel().clear()
        self.view.sel().add(jump_location)
        self.view.show_at_center(jump_location)
